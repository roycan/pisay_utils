#!/bin/bash
# Manual download script for PSHS-MC forms
# Run this script to download all forms using wget

mkdir -p forms
cd forms

echo "Downloading PSHS-MC forms..."

echo "Downloading 1/17: LEAVE-FORM-RDL.xlsx"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2025/08/LEAVE-FORM-RDL.xlsx" -O "LEAVE-FORM-RDL.xlsx" || echo "Failed to download LEAVE-FORM-RDL.xlsx"

echo "Downloading 2/17: Overtime-Authority-2024.docx"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2024/09/Overtime-Authority-2024.docx" -O "Overtime-Authority-2024.docx" || echo "Failed to download Overtime-Authority-2024.docx"

echo "Downloading 3/17: LOCATOR-SLIP.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2020/02/LOCATOR-SLIP.pdf" -O "LOCATOR-SLIP.pdf" || echo "Failed to download LOCATOR-SLIP.pdf"

echo "Downloading 4/17: PERSONNEL-RECORD-REQUEST-FORM_.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2024/09/PERSONNEL-RECORD-REQUEST-FORM_.pdf" -O "PERSONNEL-RECORD-REQUEST-FORM_.pdf" || echo "Failed to download PERSONNEL-RECORD-REQUEST-FORM_.pdf"

echo "Downloading 5/17: Request-for-change-of-official-time.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/Request-for-change-of-official-time.pdf" -O "Request-for-change-of-official-time.pdf" || echo "Failed to download Request-for-change-of-official-time.pdf"

echo "Downloading 6/17: 190227102316.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/190227102316.pdf" -O "190227102316.pdf" || echo "Failed to download 190227102316.pdf"

echo "Downloading 7/17: saln_2015.xls"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/saln_2015.xls" -O "saln_2015.xls" || echo "Failed to download saln_2015.xls"

echo "Downloading 8/17: PDS_CS_Form_No_212_Revised2017.xlsx"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/PDS_CS_Form_No_212_Revised2017.xlsx" -O "PDS_CS_Form_No_212_Revised2017.xlsx" || echo "Failed to download PDS_CS_Form_No_212_Revised2017.xlsx"

echo "Downloading 9/17: PERSONNEL-RECORD-REQUEST-FORM.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2024/06/PERSONNEL-RECORD-REQUEST-FORM.pdf" -O "PERSONNEL-RECORD-REQUEST-FORM.pdf" || echo "Failed to download PERSONNEL-RECORD-REQUEST-FORM.pdf"

echo "Downloading 10/17: EMPLOYMENT-REQUIREMENTS.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/EMPLOYMENT-REQUIREMENTS.pdf" -O "EMPLOYMENT-REQUIREMENTS.pdf" || echo "Failed to download EMPLOYMENT-REQUIREMENTS.pdf"

echo "Downloading 11/17: JO-REQUIREMENTS.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/JO-REQUIREMENTS.pdf" -O "JO-REQUIREMENTS.pdf" || echo "Failed to download JO-REQUIREMENTS.pdf"

echo "Downloading 12/17: Application-Car-Sticker-Employee.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/Application-Car-Sticker-Employee.pdf" -O "Application-Car-Sticker-Employee.pdf" || echo "Failed to download Application-Car-Sticker-Employee.pdf"

echo "Downloading 13/17: Application-Car-Sticker-Students.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/Application-Car-Sticker-Students.pdf" -O "Application-Car-Sticker-Students.pdf" || echo "Failed to download Application-Car-Sticker-Students.pdf"

echo "Downloading 14/17: Application-for-use-of-facilities.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/Application-for-use-of-facilities.pdf" -O "Application-for-use-of-facilities.pdf" || echo "Failed to download Application-for-use-of-facilities.pdf"

echo "Downloading 15/17: PSHS-00-F-ITU-01-IT-Job-Request-Form-1-1.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/PSHS-00-F-ITU-01-IT-Job-Request-Form-1-1.pdf" -O "PSHS-00-F-ITU-01-IT-Job-Request-Form-1-1.pdf" || echo "Failed to download PSHS-00-F-ITU-01-IT-Job-Request-Form-1-1.pdf"

echo "Downloading 16/17: REQUEST-FOR-REPAIR-FORM-1.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/REQUEST-FOR-REPAIR-FORM-1.pdf" -O "REQUEST-FOR-REPAIR-FORM-1.pdf" || echo "Failed to download REQUEST-FOR-REPAIR-FORM-1.pdf"

echo "Downloading 17/17: PR-FORM.pdf"
wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" --referer="https://mc.pshs.edu.ph/sample-page/" "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/PR-FORM.pdf" -O "PR-FORM.pdf" || echo "Failed to download PR-FORM.pdf"

echo "Download complete!"
cd ..
python3 generate_index.py
