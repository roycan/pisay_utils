#!/usr/bin/env python3
import requests
import os
from urllib.parse import urlparse, urljoin
import json

def download_file(url, folder="forms"):
    """Download a file from URL to the specified folder"""
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        session = requests.Session()
        response = session.get(url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()
        
        # Get filename from URL
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = "document"
        
        filepath = os.path.join(folder, filename)
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Downloaded: {filename}")
        return filename
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def main():
    # You'll need to manually add the form URLs here
    form_urls = [
        # Add URLs here like:
        # "https://mc.pshs.edu.ph/wp-content/uploads/form1.pdf",
        # "https://mc.pshs.edu.ph/wp-content/uploads/form2.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2025/08/LEAVE-FORM-RDL.xlsx",
        "https://mc.pshs.edu.ph/wp-content/uploads/2024/09/Overtime-Authority-2024.docx",
        "https://mc.pshs.edu.ph/wp-content/uploads/2020/02/LOCATOR-SLIP.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2024/09/PERSONNEL-RECORD-REQUEST-FORM_.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2018/12/Request-for-change-of-official-time.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2019/02/190227102316.pdf",
        "http://csc.gov.ph/2014-02-21-08-28-23/pdf-files/category/193-statement-of-assets,-liabilities,-and-net-worth-saln-form-for-the-year-2012-and-onwards.html",
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
        "https://mc.pshs.edu.ph/wp-content/uploads/2019/03/REQUEST-FOR-REPAIR-FORM-1.pdf",
        "https://mc.pshs.edu.ph/wp-content/uploads/2020/10/PR-FORM.pdf"
    ]
    
    if not form_urls:
        print("Please add form URLs to the form_urls list in this script")
        print("Visit https://mc.pshs.edu.ph/sample-page/ and copy the download links")
        return
    
    downloaded_files = []
    for url in form_urls:
        filename = download_file(url)
        if filename:
            downloaded_files.append(filename)
    
    # Save list of downloaded files for index generation
    with open('downloaded_files.json', 'w') as f:
        json.dump(downloaded_files, f)
    
    print(f"Downloaded {len(downloaded_files)} files")

if __name__ == "__main__":
    main()