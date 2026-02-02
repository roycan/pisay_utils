#!/usr/bin/env python3
import os
import json
from pathlib import Path

def generate_index():
    """Generate index.html with downloaded forms"""
    
    forms_dir = "forms"
    if not os.path.exists(forms_dir):
        print("Forms directory not found. Run download_forms.py first.")
        return
    
    # Get all files in forms directory
    form_files = []
    for file in os.listdir(forms_dir):
        if os.path.isfile(os.path.join(forms_dir, file)):
            # Create a readable title from filename
            title = file.replace('_', ' ').replace('-', ' ')
            title = title.rsplit('.', 1)[0]  # Remove extension
            title = title.title()
            
            form_files.append({
                'title': title,
                'filename': file,
                'description': f"PSHS-MC Form - {title}"
            })
    
    # Generate JavaScript array for forms
    forms_js = "const forms = " + json.dumps(form_files, indent=8) + ";"
    
    # Read the template
    with open('index.html', 'r') as f:
        html_content = f.read()
    
    # Replace the empty forms array with actual data
    html_content = html_content.replace(
        'const forms = [\n            // Example format:\n            // {\n            //     title: "Application Form",\n            //     filename: "application_form.pdf",\n            //     description: "Main application form for new students"\n            // }\n        ];',
        forms_js
    )
    
    # Write updated index.html
    with open('index.html', 'w') as f:
        f.write(html_content)
    
    print(f"Generated index.html with {len(form_files)} forms")
    print("Open index.html in your browser to access the forms")

if __name__ == "__main__":
    generate_index()