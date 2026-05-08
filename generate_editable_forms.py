#!/usr/bin/env python3
"""
Scan the manuals/ and forms/ directories for editable forms (.xlsx, .docx, .doc, .xls)
and generate both a Markdown catalog and a standalone HTML page.
"""
import os
import json
from pathlib import Path

EDITABLE_EXTENSIONS = {'.xlsx', '.docx', '.doc', '.xls', '.ods'}

MANUAL_SHORT_NAMES = {
    'CURRICULUM AND INSTRUCTION MANUAL (CIM) Ver2': 'CIM',
    'FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2': 'FAM',
    'QUALITY MANUAL (QM) Ver2': 'QM',
    'STUDENT AFFAIRS MANUAL (SAM) Ver2': 'SAM',
    'STUDENT SERVICES MANUAL (SSM) Ver2': 'SSM',
    'SYTEM OFFICE SERVICES MANUAL (SOM) Ver2': 'SOM',
}


def scan_editable_forms(base_dir='manuals'):
    """Scan for all editable forms and return structured data."""
    results = []
    base_path = Path(base_dir)

    for root, dirs, files in os.walk(base_path):
        root_path = Path(root)

        # Determine the manual name
        parts = root_path.relative_to(base_path).parts
        manual_full = parts[0] if parts else ''
        manual_short = MANUAL_SHORT_NAMES.get(manual_full, manual_full)

        # Determine the unit (e.g., GSU, HRU, ITU, etc.)
        unit = ''
        if len(parts) >= 3 and 'Forms' in parts:
            forms_idx = None
            for i, p in enumerate(parts):
                if p == 'Forms':
                    forms_idx = i
                    break
            if forms_idx is not None and len(parts) > forms_idx + 1:
                next_part = parts[forms_idx + 1]
                if 'editable' in next_part.lower():
                    if forms_idx > 0:
                        unit = parts[forms_idx - 1] if parts[forms_idx - 1] != 'Forms' else ''
                else:
                    unit = next_part

        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EDITABLE_EXTENSIONS:
                rel_path = root_path.relative_to(base_path) / f
                results.append({
                    'name': f,
                    'manual': manual_short,
                    'manual_full': manual_full,
                    'unit': unit,
                    'type': ext.lstrip('.').upper(),
                    'path': str(rel_path),
                })

    # Also scan the forms/ directory for editable files
    forms_path = Path('forms')
    if forms_path.exists():
        for f in forms_path.iterdir():
            if f.is_file() and f.suffix.lower() in EDITABLE_EXTENSIONS:
                results.append({
                    'name': f.name,
                    'manual': 'HR/Admin',
                    'manual_full': 'HR/Administrative Forms',
                    'unit': '',
                    'type': f.suffix.lstrip('.').upper(),
                    'path': 'forms/' + f.name,
                })

    # Sort by manual, then unit, then name
    results.sort(key=lambda x: (x['manual'], x['unit'], x['name']))
    return results


def generate_markdown_catalog(forms, output_path='EDITABLE_FORMS_CATALOG.md'):
    """Generate a Markdown catalog of all editable forms."""
    lines = [
        '# Editable Forms Catalog',
        '',
        '> Auto-generated catalog of all editable forms available in the PSHS-MC repository.',
        '> Total: **{}** editable forms'.format(len(forms)),
        '',
        '---',
        '',
    ]

    current_manual = ''
    current_unit = ''

    for form in forms:
        if form['manual'] != current_manual:
            current_manual = form['manual']
            current_unit = ''
            lines.append('## {}'.format(form['manual_full']))
            lines.append('')

        if form['unit'] and form['unit'] != current_unit:
            current_unit = form['unit']
            lines.append('### {}'.format(current_unit))
            lines.append('')

        lines.append('- [{}](../{}) ({})'.format(form['name'], form['path'], form['type']))
        lines.append('')

    # Summary table
    lines.append('---')
    lines.append('')
    lines.append('## Summary by Manual')
    lines.append('')
    lines.append('| Manual | Editable Forms Count |')
    lines.append('|--------|---------------------|')

    manual_counts = {}
    for form in forms:
        manual = form['manual']
        manual_counts[manual] = manual_counts.get(manual, 0) + 1

    for manual, count in sorted(manual_counts.items()):
        lines.append('| {} | {} |'.format(manual, count))
    lines.append('| **Total** | **{}** |'.format(len(forms)))
    lines.append('')

    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))

    print('Generated Markdown catalog: {}'.format(output_path))


def generate_html_page(forms, output_path='editable-forms.html'):
    """Generate a standalone HTML page for browsing editable forms."""
    # Group forms by manual for the page
    manuals = {}
    for form in forms:
        manual = form['manual']
        if manual not in manuals:
            manuals[manual] = []
        manuals[manual].append(form)

    # Build JSON data for the search/filter functionality
    forms_json = json.dumps([{
        'name': f['name'],
        'manual': f['manual'],
        'unit': f['unit'],
        'type': f['type'],
        'path': f['path'],
    } for f in forms], ensure_ascii=False)

    # Pre-build dynamic HTML parts
    excel_count = len([f for f in forms if f['type'] in ('XLSX', 'XLS', 'ODS')])
    word_count = len([f for f in forms if f['type'] in ('DOCX', 'DOC')])

    manual_options = ''.join(
        '<option value="{}">{}</option>'.format(m, m)
        for m in sorted(manuals.keys())
    )

    nav_links = ''.join(
        '<a href="#" onclick="scrollToManual(\'{}\')">{}</a>'.format(m, m)
        for m in sorted(manuals.keys())
    )

    html_parts = []
    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PSHS-MC Editable Forms</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }
        .header {
            background: linear-gradient(135deg, #1a237e, #283593);
            color: white;
            padding: 2rem 1rem;
            text-align: center;
        }
        .header h1 { font-size: 1.8rem; margin-bottom: 0.5rem; }
        .header p { opacity: 0.9; font-size: 1rem; }
        .header .stats {
            margin-top: 1rem;
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
        }
        .header .stat {
            background: rgba(255,255,255,0.15);
            padding: 0.5rem 1.5rem;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        .container { max-width: 1200px; margin: 0 auto; padding: 1rem; }
        .controls {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            align-items: center;
        }
        .controls input {
            flex: 1;
            min-width: 200px;
            padding: 0.6rem 1rem;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        .controls input:focus { border-color: #1a237e; outline: none; }
        .controls select {
            padding: 0.6rem 1rem;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 1rem;
            background: white;
        }
        .controls select:focus { border-color: #1a237e; outline: none; }
        .nav-links {
            margin: 1rem 0;
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        .nav-links a {
            padding: 0.4rem 1rem;
            background: white;
            border-radius: 20px;
            text-decoration: none;
            color: #1a237e;
            font-weight: 500;
            font-size: 0.85rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            transition: all 0.2s;
        }
        .nav-links a:hover { background: #1a237e; color: white; }
        .manual-section {
            background: white;
            border-radius: 8px;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .manual-header {
            background: #e8eaf6;
            padding: 0.8rem 1.2rem;
            font-weight: 600;
            font-size: 1.1rem;
            color: #1a237e;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .manual-header:hover { background: #c5cae9; }
        .manual-header .count {
            background: #1a237e;
            color: white;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.8rem;
        }
        .manual-body { padding: 0; }
        .unit-group { border-bottom: 1px solid #eee; }
        .unit-header {
            padding: 0.5rem 1.2rem;
            background: #f8f9fa;
            font-weight: 500;
            color: #555;
            font-size: 0.95rem;
        }
        .form-row {
            display: flex;
            align-items: center;
            padding: 0.6rem 1.2rem;
            border-bottom: 1px solid #f0f0f0;
            transition: background 0.2s;
        }
        .form-row:hover { background: #f8f9ff; }
        .form-row:last-child { border-bottom: none; }
        .form-name {
            flex: 1;
            font-size: 0.9rem;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .form-name a { color: #1a237e; text-decoration: none; }
        .form-name a:hover { text-decoration: underline; }
        .badge {
            display: inline-block;
            padding: 0.15rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
            color: white;
            margin-left: 0.5rem;
            white-space: nowrap;
        }
        .footer {
            text-align: center;
            padding: 2rem;
            color: #999;
            font-size: 0.85rem;
        }
        .footer a { color: #1a237e; text-decoration: none; }
        .no-results {
            text-align: center;
            padding: 3rem;
            color: #999;
            font-size: 1.1rem;
        }
        @media (max-width: 768px) {
            .controls { flex-direction: column; }
            .controls input { min-width: 100%; }
            .header h1 { font-size: 1.4rem; }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>📋 PSHS-MC Editable Forms</h1>
        <p>Philippine Science High School - Main Campus</p>
        <div class="stats">
            <span class="stat">📊 """ + str(excel_count) + """ Excel/Calc files</span>
            <span class="stat">📝 """ + str(word_count) + """ Word files</span>
            <span class="stat">📁 """ + str(len(forms)) + """ Total editable forms</span>
        </div>
    </div>

    <div class="container">
        <div class="controls">
            <input type="text" id="search" placeholder="🔍 Search forms by name, form code, or unit..." oninput="filterForms()">
            <select id="manualFilter" onchange="filterForms()">
                <option value="">All Manuals</option>
                """ + manual_options + """
            </select>
            <select id="typeFilter" onchange="filterForms()">
                <option value="">All Types</option>
                <option value="XLSX">Excel (.xlsx)</option>
                <option value="XLS">Excel (.xls)</option>
                <option value="DOCX">Word (.docx)</option>
                <option value="DOC">Word (.doc)</option>
            </select>
        </div>

        <div class="nav-links">
            <a href="#" onclick="scrollToManual('')">All</a>
            """ + nav_links + """
            <a href="index.html">← Back to Forms</a>
            <a href="manuals.html">← Manuals</a>
        </div>

        <div id="results"></div>
    </div>

    <div class="footer">
        <p>PSHS-MC Forms & Manuals Repository |
        <a href="index.html">Forms</a> |
        <a href="manuals.html">Manuals</a> |
        <a href="editable-forms.html">Editable Forms</a>
        </p>
    </div>

    <script>
        var allForms = """ + forms_json + """;

        function renderForms(formsToRender) {
            var container = document.getElementById('results');

            if (formsToRender.length === 0) {
                container.innerHTML = '<div class="no-results">No editable forms found matching your search.</div>';
                return;
            }

            // Group by manual, then unit
            var grouped = {};
            formsToRender.forEach(function(f) {
                if (!grouped[f.manual]) grouped[f.manual] = {};
                var unit = f.unit || 'General';
                if (!grouped[f.manual][unit]) grouped[f.manual][unit] = [];
                grouped[f.manual][unit].push(f);
            });

            var html = '';
            for (var manual in grouped) {
                var totalForms = 0;
                for (var u in grouped[manual]) totalForms += grouped[manual][u].length;
                var safeId = manual.replace(/[^a-zA-Z]/g, '');
                html += '<div class="manual-section" id="manual-' + safeId + '">';
                html += '<div class="manual-header" onclick="toggleSection(this)">';
                html += '<span>' + manual + '</span>';
                html += '<span class="count">' + totalForms + ' forms</span>';
                html += '</div>';
                html += '<div class="manual-body">';

                for (var unit in grouped[manual]) {
                    if (unit !== 'General') {
                        html += '<div class="unit-group"><div class="unit-header">' + unit + '</div>';
                    } else {
                        html += '<div class="unit-group">';
                    }
                    grouped[manual][unit].forEach(function(f) {
                        var color = (f.type === 'XLSX' || f.type === 'XLS') ? '#217346' : '#2b579a';
                        html += '<div class="form-row">';
                        html += '<span class="form-name"><a href="' + f.path + '" target="_blank">' + f.name + '</a></span>';
                        html += '<span class="badge" style="background:' + color + '">' + f.type + '</span>';
                        html += '</div>';
                    });
                    html += '</div>';
                }

                html += '</div></div>';
            }

            container.innerHTML = html;
        }

        function toggleSection(header) {
            var body = header.parentElement.querySelector('.manual-body');
            body.style.display = body.style.display === 'none' ? 'block' : 'none';
        }

        function filterForms() {
            var search = document.getElementById('search').value.toLowerCase();
            var manualFilter = document.getElementById('manualFilter').value;
            var typeFilter = document.getElementById('typeFilter').value;

            var filtered = allForms.filter(function(f) {
                var matchSearch = !search ||
                    f.name.toLowerCase().indexOf(search) !== -1 ||
                    f.unit.toLowerCase().indexOf(search) !== -1 ||
                    f.manual.toLowerCase().indexOf(search) !== -1;
                var matchManual = !manualFilter || f.manual === manualFilter;
                var matchType = !typeFilter || f.type === typeFilter;
                return matchSearch && matchManual && matchType;
            });

            renderForms(filtered);
        }

        function scrollToManual(manual) {
            if (manual) {
                document.getElementById('manualFilter').value = manual;
            } else {
                document.getElementById('manualFilter').value = '';
            }
            filterForms();
        }

        // Initial render
        renderForms(allForms);
    </script>
</body>
</html>""")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(html_parts))

    print('Generated HTML page: {}'.format(output_path))


def main():
    print('Scanning for editable forms...')
    forms = scan_editable_forms()
    print('Found {} editable forms'.format(len(forms)))

    generate_markdown_catalog(forms)
    generate_html_page(forms)

    # Also save the raw data as JSON for potential future use
    with open('editable_forms.json', 'w', encoding='utf-8') as f:
        json.dump(forms, f, ensure_ascii=False, indent=2)
    print('Generated JSON data: editable_forms.json')


if __name__ == '__main__':
    main()
