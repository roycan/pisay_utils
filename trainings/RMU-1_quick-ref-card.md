# RMU-1 Quick Reference Card
## Digital Records Tracking and Mail Management

---

## SIDE A: Step-by-Step Guide

### How to Enter a New Document in the Digital Registry

**1. Open the Registry**
- Go to `drive.google.com`
- Open `RMU_Digital_Registry_2026`

**2. Enter the Document Details**
- **Column A (Date/Time Received):** Type the date and time (e.g., `4/16/2026 9:15:00`)
- **Column B (Control Number):** Auto-generates automatically (e.g., `260401`)
- **Column C (Source/Sender):** Type who sent the document
- **Column D (Subject Matter):** Type what the document is about
- **Column E (Date Released):** Leave blank until document is released
- **Column F (Personnel/Office Assigned):** Select from dropdown menu
- **Column G (Remarks):** Type any additional notes

**3. Save**
- Google Sheets auto-saves. No need to click save!

**4. Mark as Released (When Done)**
- Enter the release date in Column E
- Row color changes from yellow to green

---

### How to Find a Document

**Method 1: Search**
- Press `Ctrl + F` (Windows) or `Cmd + F` (Mac)
- Type the control number, sender, or subject
- Press Enter to find

**Method 2: Filter**
- Click **Data** → **Create a filter**
- Click the filter arrow in any column
- Select the criteria you want to filter by
- Click **OK**

**Method 3: Sort**
- Click **Data** → **Sort range**
- Choose the column to sort by
- Select A-Z or Z-A

---

### How to Work Offline (LibreOffice - Optional)

**1. Download for Offline Use**
- Open your Google Sheet
- Click **File** → **Download** → **OpenDocument Spreadsheet (.ods)**

**2. Open in LibreOffice Calc**
- Double-click the downloaded `.ods` file
- LibreOffice Calc will open automatically

**3. Work Offline**
- Enter data as normal
- Save your changes

**4. Upload When Online**
- Go to `drive.google.com`
- Drag and drop the `.ods` file
- Google will convert it back to Sheets format

*Note: LibreOffice will be deployed campus-wide before full training rollout*

---

## SIDE B: Shortcuts, Tips & Help

### Keyboard Shortcuts

| Action | Windows | Mac |
|--------|---------|-----|
| Undo | `Ctrl + Z` | `Cmd + Z` |
| Redo | `Ctrl + Y` | `Cmd + Y` |
| Copy | `Ctrl + C` | `Cmd + C` |
| Paste | `Ctrl + V` | `Cmd + V` |
| Find | `Ctrl + F` | `Cmd + F` |
| Insert date | `Ctrl + ;` | `Cmd + ;` |
| Insert time | `Ctrl + Shift + ;` | `Cmd + Shift + ;` |
| Edit cell | `F2` | `F2` |
| Save | `Ctrl + S` | `Cmd + S` |

---

### The Control Number Formula

```
=IF(A2="", "", TEXT(A2, "YYMM") & TEXT(COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*"), "00"))
```

**What it does:**
- Checks if there's a date in Column A
- Extracts year and month (e.g., 2604 for April 2026)
- Counts documents received this month
- Formats as 2 digits (01, 02, 03...)
- Combines everything: `260401`

**Example output:**
- First document in April 2026: `260401`
- Tenth document in April 2026: `260410`
- First document in May 2026: `260501`

---

### Common Tasks

| Task | How to Do It |
|------|--------------|
| Add a new row | Right-click row number → Insert 1 below |
| Delete a row | Right-click row number → Delete row |
| Resize column | Drag border between column letters |
| Freeze header row | Click **View** → **Freeze** → **1 row** |
| Share the sheet | Click **Share** → Enter email addresses |
| Print the registry | Click **File** → **Print** |
| Export to PDF | Click **File** → **Download** → **PDF Document** |
| Check version history | Click **File** → **Version history** → **See version history** |

---

### Color Coding Guide

| Color | Meaning |
|-------|---------|
| 🟡 Yellow | Document received but NOT yet released |
| 🟢 Green | Document has been released/completed |
| ⚪ White | No data entered yet |

---

### Common Mistakes to Avoid

| Mistake | Why It's a Problem | Fix |
|---------|-------------------|-----|
| Typing control number manually | May cause duplicates | Let the formula auto-generate it |
| Entering date as text (e.g., "April 16") | Formula won't work | Use date format (4/16/2026) |
| Forgetting to enter time | Can't track when exactly received | Include time (9:15:00) |
| Not using dropdown for office | Inconsistent data | Always select from dropdown |
| Deleting the formula | Control numbers won't generate | Don't delete cell B2 and below |

---

### Where to Find Help

**For Google Sheets:**
- Help Center: `sheets.google.com/support`
- Press `?` in any Google Sheet for quick help

**For LibreOffice:**
- Help Center: `help.libreoffice.org`
- Press `F1` in LibreOffice for context help

**For PSHS Policies:**
- FAM 13.1 Records Management Manual
- Contact your RMU Head or Records Officer

**For Technical Issues:**
- Contact ITU at `itu@pshs.edu.ph` (or your campus ITU email)

---

### Quick Reference: Required Fields (FAM 13.1 Section 3.4b)

| Field | Description | Format |
|-------|-------------|--------|
| Date/Time Received | When document arrived | Date + Time |
| Control Number | Unique identifier | YYMMXX (auto) |
| Source/Sender | Who sent it | Text |
| Subject Matter | What it's about | Text |
| Date Released | When it was sent out | Date |
| Personnel/Office Assigned | Who needs to act | Dropdown |
| Remarks | Additional notes | Text |

---

### Emergency: What to Do If...

| Situation | Solution |
|-----------|----------|
| Internet is down | Download as .ods and work in LibreOffice (once deployed) |
| Formula isn't working | Check cell references and format |
| Accidentally deleted data | Use **File** → **Version history** to restore |
| Can't find a document | Use Ctrl+F to search by control number |
| Need to share with someone | Click **Share** and enter their email |
| Sheet is locked | Contact the owner (usually RMU Head) |

---

### Remember the Analogy

**Physical Logbook → Google Sheet**

| Physical Logbook | Google Sheet |
|------------------|--------------|
| Write by hand | Type on keyboard |
| One person at a time | Multiple people simultaneously |
| Can be lost/damaged | Backed up automatically |
| Hard to search | Search in seconds |
| Manual control numbers | Auto-generated control numbers |
| Paper pages | Infinite rows |

---

**PSHS-MC Records Management Unit**
*Training: RMU-1 Digital Records Tracking and Mail Management*
*Reference: FAM 13.1 Records Management V2_Rev2*

---

**Print this card front-and-back and keep it at your desk!**
