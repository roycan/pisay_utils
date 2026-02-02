
import os

def generate_manuals_page():
    manuals_dir = 'manuals'
    output_file = 'manuals.html'

    manuals_by_category = {}

    for root, dirs, files in os.walk(manuals_dir):
        # Skip the top-level directory itself
        if root == manuals_dir:
            continue

        category = os.path.basename(root)
        
        # Don't include editable copy folders
        if 'editable copy' in category:
            continue

        if category not in manuals_by_category:
            manuals_by_category[category] = []
        
        for file in files:
            manuals_by_category[category].append(os.path.join(root, file))

    with open(output_file, 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PSHS-MC Downloadable Manuals</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            text-align: center;
            background-color: #003366;
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .manuals-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .manual-card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .manual-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }
        .manual-title {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #003366;
        }
        .manual-link {
            display: inline-block;
            background-color: #0066cc;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin: 5px;
        }
        .manual-link:hover {
            background-color: #0052a3;
        }
        .file-info {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }
        .category-title {
            font-size: 24px;
            font-weight: bold;
            color: #003366;
            margin-top: 40px;
            margin-bottom: 20px;
            border-bottom: 2px solid #003366;
            padding-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Philippine Science High School - Main Campus</h1>
        <h2>Downloadable Manuals</h2>
    </div>
""")

        for category, files in sorted(manuals_by_category.items()):
            f.write(f'<h2 class="category-title">{category}</h2>')
            f.write('<div class="manuals-grid">')
            for file_path in sorted(files):
                file_name = os.path.basename(file_path)
                # a title that's the filename without the extension
                title = os.path.splitext(file_name)[0]
                # remove underscores from title
                title = title.replace("_", " ")

                f.write(f"""
        <div class="manual-card">
            <div class="manual-title">{title}</div>
            <div class="file-info">File: {file_name}</div>
            <a href="{file_path}" class="manual-link" target="_blank">Open Local File</a>
        </div>""")
            f.write('</div>')

        f.write("""
</body>
</html>""")

if __name__ == '__main__':
    generate_manuals_page()
    print("manuals.html generated successfully.")

