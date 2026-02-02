#!/usr/bin/env python3
import os
import json

def create_manual_download_guide():
    """Create a guide for manual downloading"""
    
    form_urls = [
        "https://mc.pshs.edu.ph/wp-content/uploads/2025/08/LEAVE-FORM-RDL.xlsx",
        "https://mc.pshs.edu.ph/wp-content/uploads/2024/09/Overtime-Authority-2024.docx",
        "https://mc.pshs.edu.ph/wp-content/uploads/2020/02/LOCATOR-SLIP.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2024/09/PERSONNEL-RECORD-REQUEST-FORM_.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/Request-for-change-of-official-time.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/190227102316.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/saln_2015.xls",
        "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/PDS_CS_Form_No_212_Revised2017.xlsx",
        "https://mc.pshs.edu.ph/wp-content/uploads/2024/06/PERSONNEL-RECORD-REQUEST-FORM.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/EMPLOYMENT-REQUIREMENTS.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/JO-REQUIREMENTS.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/Application-Car-Sticker-Employee.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/Application-Car-Sticker-Students.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/Application-for-use-of-facilities.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/PSHS-00-F-ITU-01-IT-Job-Request-Form-1-1.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/REQUEST-FOR-REPAIR-FORM-1.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/PR-FORM.pdf"
    ]
    
    # Create forms directory
    if not os.path.exists("forms"):
        os.makedirs("forms")
    
    # Create download script
    script_content = """#!/bin/bash
# Manual download script for PSHS-MC forms
# Run this script to download all forms using wget

mkdir -p forms
cd forms

echo "Downloading PSHS-MC forms..."
"""
    
    for i, url in enumerate(form_urls, 1):
        filename = os.path.basename(url.split('/')[-1])
        script_content += f'\necho "Downloading {i}/{len(form_urls)}: {filename}"\n'
        script_content += f'wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "{url}" -O "{filename}" || echo "Failed to download {filename}"\n'
    
    script_content += '\necho "Download complete!"\ncd ..\npython3 generate_index.py\n'
    
    with open('download_all.sh', 'w') as f:
        f.write(script_content)
    
    os.chmod('download_all.sh', 0o755)
    
    print("Created download_all.sh script")
    print("Run: ./download_all.sh")

if __name__ == "__main__":
    create_manual_download_guide()