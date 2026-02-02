# PSHS-MC Forms Downloader

This project helps you download and organize forms from the PSHS-MC website.

## Setup Instructions

Since the school website has Cloudflare protection, you'll need to manually collect the form URLs first.

### Step 1: Collect Form URLs
1. Visit https://mc.pshs.edu.ph/sample-page/
2. Right-click on each form link and copy the link address
3. Open `download_forms.py` and add the URLs to the `form_urls` list

Example:
```python
form_urls = [
    "https://mc.pshs.edu.ph/wp-content/uploads/form1.pdf",
    "https://mc.pshs.edu.ph/wp-content/uploads/form2.pdf",
    # Add more URLs here
]
```

### Step 2: Install Requirements
```bash
pip install requests
```

### Step 3: Download Forms
```bash
python3 download_forms.py
```

### Step 4: Generate Index Page
```bash
python3 generate_index.py
```

### Step 5: Access Forms
Open `index.html` in your browser to access all downloaded forms in a nice interface.

## File Structure
```
├── download_forms.py    # Script to download forms
├── generate_index.py    # Script to generate HTML index
├── index.html          # Web interface for forms
├── forms/              # Downloaded forms directory
└── README.md           # This file
```

## Manual Alternative
If you prefer to download forms manually:
1. Create a `forms/` directory
2. Download forms from the website and save them in the `forms/` directory
3. Run `python3 generate_index.py` to create the index page