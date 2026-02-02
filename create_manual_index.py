#!/usr/bin/env python3
import os
import json

# Create forms directory
os.makedirs("forms", exist_ok=True)

# Form data with proper names
forms_data = [
    {"title": "Leave Form RDL", "filename": "LEAVE-FORM-RDL.xlsx", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2025/08/LEAVE-FORM-RDL.xlsx"},
    {"title": "Overtime Authority 2024", "filename": "Overtime-Authority-2024.docx", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2024/09/Overtime-Authority-2024.docx"},
    {"title": "Locator Slip", "filename": "LOCATOR-SLIP.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2020/02/LOCATOR-SLIP.pdf"},
    {"title": "Personnel Record Request Form", "filename": "PERSONNEL-RECORD-REQUEST-FORM_.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2024/09/PERSONNEL-RECORD-REQUEST-FORM_.pdf"},
    {"title": "Request For Change Of Official Time", "filename": "Request-for-change-of-official-time.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/Request-for-change-of-official-time.pdf"},
    {"title": "SALN Form", "filename": "190227102316.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/190227102316.pdf"},
    {"title": "SALN 2015", "filename": "saln_2015.xls", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/saln_2015.xls"},
    {"title": "PDS Form 212 Revised 2017", "filename": "PDS_CS_Form_No_212_Revised2017.xlsx", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/PDS_CS_Form_No_212_Revised2017.xlsx"},
    {"title": "Personnel Record Request Form", "filename": "PERSONNEL-RECORD-REQUEST-FORM.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2024/06/PERSONNEL-RECORD-REQUEST-FORM.pdf"},
    {"title": "Employment Requirements", "filename": "EMPLOYMENT-REQUIREMENTS.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/EMPLOYMENT-REQUIREMENTS.pdf"},
    {"title": "JO Requirements", "filename": "JO-REQUIREMENTS.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/JO-REQUIREMENTS.pdf"},
    {"title": "Car Sticker Application Employee", "filename": "Application-Car-Sticker-Employee.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/Application-Car-Sticker-Employee.pdf"},
    {"title": "Car Sticker Application Students", "filename": "Application-Car-Sticker-Students.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/Application-Car-Sticker-Students.pdf"},
    {"title": "Application For Use Of Facilities", "filename": "Application-for-use-of-facilities.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/Application-for-use-of-facilities.pdf"},
    {"title": "IT Job Request Form", "filename": "PSHS-00-F-ITU-01-IT-Job-Request-Form-1-1.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/PSHS-00-F-ITU-01-IT-Job-Request-Form-1-1.pdf"},
    {"title": "Request For Repair Form", "filename": "REQUEST-FOR-REPAIR-FORM-1.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/REQUEST-FOR-REPAIR-FORM-1.pdf"},
    {"title": "PR Form", "filename": "PR-FORM.pdf", "url": "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/PR-FORM.pdf"}
]

# Update index.html with form data
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PSHS-MC Downloadable Forms</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            text-align: center;
            background-color: #003366;
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .forms-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }}
        .form-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        .form-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }}
        .form-title {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #003366;
        }}
        .form-link {{
            display: inline-block;
            background-color: #0066cc;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin: 5px;
        }}
        .form-link:hover {{
            background-color: #0052a3;
        }}
        .file-info {{
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }}
        .manual-note {{
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Philippine Science High School - Main Campus</h1>
        <h2>Downloadable Forms</h2>
    </div>

    <div class="manual-note">
        <strong>Manual Download Required:</strong> Due to website protection, you need to manually download each form:
        <br>1. Click "Download from Website" to open the form URL
        <br>2. Save the file to the "forms" folder
        <br>3. Use "Open Local File" once downloaded
    </div>

    <div class="forms-grid">"""

for form in forms_data:
    html_content += f"""
        <div class="form-card">
            <div class="form-title">{form['title']}</div>
            <div class="file-info">File: {form['filename']}</div>
            <a href="{form['url']}" class="form-link" target="_blank">Download from Website</a>
            <a href="forms/{form['filename']}" class="form-link" target="_blank">Open Local File</a>
        </div>"""

html_content += """
    </div>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(html_content)

print("Created index.html with manual download links")
print("Open index.html in your browser to access the forms")
print("You'll need to manually download each form from the website links provided")