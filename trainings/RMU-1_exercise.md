# RMU-1 Hands-On Exercise: Digital Records Tracking and Mail Management

**Duration:** 20 minutes
**Format:** Guided step-by-step exercise
**Prerequisites:** Watched pre-session video, Session 0 completed

---

## Exercise Scenario

You are the Records Officer on duty at PSHS-MC. It's April 16, 2026, and several documents have arrived this morning. Your task is to enter these documents into a digital registry using Google Sheets.

---

## Step-by-Step Instructions

### Step 1: Create Your Google Sheet (2 minutes)

1. Open your web browser and go to `drive.google.com`
2. Click the **+ New** button in the top-left corner
3. Select **Google Sheets** from the dropdown menu
4. A new, untitled spreadsheet will open
5. Click on "Untitled spreadsheet" at the top and rename it to: `YourName_Practice_Registry`
6. Click **Share** → Change to **Anyone with the link can edit** (for training purposes)

**Expected Outcome:** You have a blank Google Sheet named with your name.

[SCREENSHOT: Blank Google Sheet with cursor in the title field]

---

### Step 2: Set Up Column Headers (2 minutes)

1. In cell **A1**, type: `Date/Time Received`
2. In cell **B1**, type: `Control Number`
3. In cell **C1**, type: `Source/Sender`
4. In cell **D1**, type: `Subject Matter`
5. In cell **E1**, type: `Date Released`
6. In cell **F1**, type: `Personnel/Office Assigned`
7. In cell **G1**, type: `Remarks`

**Expected Outcome:** You should have 7 column headers in row 1.

[SCREENSHOT: Row 1 with all 7 column headers]

---

### Step 3: Format the Columns (2 minutes)

1. Click on the **A** at the top of column A to select the entire column
2. Go to **Format** → **Number** → **Date time**
3. Click on the **E** at the top of column E to select the entire column
4. Go to **Format** → **Number** → **Date**
5. Click on the **B** at the top of column B, hold Shift, and click on **G** to select columns B through G
6. Go to **Format** → **Number** → **Plain text**
7. Click on the **1** at the left of row 1 to select the entire row
8. Click the **Bold** button (B icon) in the toolbar
9. Click the **Fill color** button (paint bucket icon) and choose a light color (light gray or light blue)

**Expected Outcome:** Column A is formatted for date/time, Column E for date, other columns as plain text, and row 1 is bold with a colored background.

[SCREENSHOT: Formatted columns with bold, colored header row]

---

### Step 4: Enter the Control Number Formula (3 minutes)

1. Click on cell **B2**
2. Copy and paste this formula exactly:

```
=IF(A2="", "", TEXT(A2, "YYMM") & TEXT(COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*"), "00"))
```

3. Press **Enter**
4. Click on cell **B2** again
5. Click the small square in the bottom-right corner of the cell (the fill handle)
6. Drag it down to cell **B11** (or further if you prefer)

**Expected Outcome:** The formula is applied to cells B2 through B11. Cells should appear blank (since no dates are entered yet).

[SCREENSHOT: Formula entered in B2 and dragged down]

---

### Step 5: Create the Office List for Data Validation (2 minutes)

1. Scroll down to row **20** (or any empty area below your data)
2. In cell **A20**, type: `Valid Offices`
3. In cell **A21**, type: `Campus Director`
4. In cell **A22**, type: `Executive Director`
5. In cell **A23**, type: `HRU`
6. In cell **A24**, type: `GSU`
7. In cell **A25**, type: `ACU`
8. In cell **A26**, type: `PRU`
9. In cell **A27**, type: `ITU`
10. In cell **A28**, type: `HSU`
11. In cell **A29**, type: `LIB`
12. In cell **A30**, type: `REG`
13. In cell **A31**, type: `RHU`
14. In cell **A32**, type: `RMU`
15. In cell **A33**, type: `Other`

**Expected Outcome:** You have a list of 14 valid offices in cells A21 through A33.

[SCREENSHOT: Office list in cells A21-A33]

---

### Step 6: Apply Data Validation (2 minutes)

1. Click on the **F** at the top of column F to select the entire "Personnel/Office Assigned" column
2. Go to **Data** → **Data validation**
3. A dialog box will appear on the right side
4. Under **Criteria**, click the dropdown and select **Dropdown (from a range)**
5. Click the grid icon next to the range field
6. Select cells **A21 through A33** (your office list)
7. Click **OK**
8. Make sure **Show dropdown list in cell** is checked
9. Click **Done**

**Expected Outcome:** When you click in any cell in column F, a dropdown arrow appears with the list of offices.

[SCREENSHOT: Data validation dialog box with office range selected]

---

### Step 7: Enter the 5 Sample Documents (5 minutes)

Enter each document in the corresponding row:

**Document 1 (Row 2):**
- **A2 (Date/Time Received):** `4/16/2026 9:15:00`
- **C2 (Source/Sender):** `DepEd Regional Office`
- **D2 (Subject Matter):** `Invitation to Regional Education Summit`
- **F2 (Personnel/Office Assigned):** Select `Campus Director` from the dropdown
- **G2 (Remarks):** `Response needed by April 30`

*Observe:* Cell B2 should now show `260401` (auto-generated control number)

**Document 2 (Row 3):**
- **A3 (Date/Time Received):** `4/16/2026 9:30:00`
- **C3 (Source/Sender):** `PSHS System Office`
- **D3 (Subject Matter):** `Updated QMS Manual (FAM 13.1 Revision)`
- **F3 (Personnel/Office Assigned):** Select `RMU` from the dropdown
- **G3 (Remarks):** `For review and implementation`

*Observe:* Cell B3 should now show `260402`

**Document 3 (Row 4):**
- **A4 (Date/Time Received):** `4/16/2026 10:00:00`
- **C4 (Source/Sender):** `Supplier (ABC Office Supplies)`
- **D4 (Subject Matter):** `Delivery of printer paper and ink`
- **F4 (Personnel/Office Assigned):** Select `GSU` from the dropdown
- **G4 (Remarks):** `Invoice attached`

*Observe:* Cell B4 should now show `260403`

**Document 4 (Row 5):**
- **A5 (Date/Time Received):** `4/16/2026 10:45:00`
- **C5 (Source/Sender):** `Anonymous`
- **D5 (Subject Matter):** `Concern about cafeteria food quality`
- **F5 (Personnel/Office Assigned):** Select `GSU` from the dropdown
- **G5 (Remarks):** `Per FAM 3.4a, forward to concerned office`

*Observe:* Cell B5 should now show `260404`

**Document 5 (Row 6):**
- **A6 (Date/Time Received):** `4/16/2026 11:00:00`
- **C6 (Source/Sender):** `PSHS Alumni Association`
- **D6 (Subject Matter):** `Proposal for Alumni Homecoming 2026`
- **F6 (Personnel/Office Assigned):** Select `Campus Director` from the dropdown
- **G6 (Remarks):** `For consideration`

*Observe:* Cell B6 should now show `260405`

**Expected Outcome:** All 5 documents are entered, and control numbers 260401 through 260405 are auto-generated.

[SCREENSHOT: All 5 documents entered with control numbers]

---

### Step 8: Update Document Status (2 minutes)

1. For **Document 3** (Row 4 - GSU printer paper delivery), assume GSU has already received and processed it. Enter today's date in cell **E4**: `4/16/2026`
2. For **Document 2** (Row 3 - RMU QMS Manual), assume it has been reviewed. Enter today's date in cell **E3**: `4/16/2026`

**Expected Outcome:**
- Rows 3 and 4 should now have dates in the "Date Released" column
- Rows 2, 5, and 6 should still have blank "Date Released" cells

[SCREENSHOT: Documents 2 and 3 marked as released]

---

### Step 9: Add Conditional Formatting (Optional - if time permits)

1. Select cells **A2 through G11**
2. Go to **Format** → **Conditional formatting**
3. **Rule 1:**
   - Format cells if: **Custom formula is**
   - Formula: `=AND(A2<>"", E2="")`
   - Formatting style: Click the fill color icon and choose **yellow**
   - Click **Done**
4. **Rule 2:**
   - Click **Add another rule**
   - Format cells if: **Custom formula is**
   - Formula: `=E2<>""`
   - Formatting style: Click the fill color icon and choose **light green**
   - Click **Done**

**Expected Outcome:**
- Rows 2, 5, and 6 (documents not yet released) should have a yellow background
- Rows 3 and 4 (documents released) should have a light green background

[SCREENSHOT: Conditional formatting applied - yellow for pending, green for released]

---

### Step 10: Use the Filter Feature (2 minutes)

1. Click anywhere in your data (cells A2 through G6)
2. Go to **Data** → **Create a filter**
3. Filter arrows should appear in each header cell
4. Click the filter arrow in cell **F1** (Personnel/Office Assigned)
5. Uncheck **Select all**
6. Check only **Campus Director**
7. Click **OK**

**Expected Outcome:** Only rows 2 and 6 should be visible (documents assigned to Campus Director).

[SCREENSHOT: Filtered view showing only Campus Director documents]

8. Click the filter arrow in cell **F1** again
9. Click **Clear** to show all documents

**Expected Outcome:** All 5 documents are visible again.

---

## Self-Check Answers

After completing the exercise, verify your work against these expected results:

### Question 1: What control number was generated for Document 1?
**Answer:** `260401`

### Question 2: What control number was generated for Document 5?
**Answer:** `260405`

### Question 3: How many documents are assigned to Campus Director?
**Answer:** 2 (Documents 1 and 5)

### Question 4: How many documents are still pending (not released)?
**Answer:** 3 (Documents 1, 4, and 5)

### Question 5: What is the subject of the document from the anonymous sender?
**Answer:** Concern about cafeteria food quality

---

## Challenge Variations

### Basic Challenge (Completed Above)
- Enter 5 documents with auto-generated control numbers
- Apply basic formatting

### Intermediate Challenge (If You Finish Early)
- Add conditional formatting for visual status tracking
- Create a summary at the bottom showing:
  - Total documents received: `=COUNTA(A2:A11)`
  - Documents released: `=COUNTA(E2:E11)`
  - Documents pending: `=COUNTA(A2:A11) - COUNTA(E2:E11)`

### Advanced Challenge (For Extra Practice)
- Create a second sheet named "Summary"
- Use the `IMPORTRANGE` function to pull data from your main sheet
- Create a pivot table showing documents by assigned office
- Add a chart showing the distribution of documents across units

---

## Troubleshooting

If you encounter issues, check these common problems:

| Problem | Solution |
|---------|----------|
| Control number shows `#REF!` | Check that the formula references `$B$1:B1` (mixed references) |
| Control number doesn't appear | Make sure you entered a date in column A first |
| Dropdown list doesn't appear | Verify data validation is applied to the correct range and "Show dropdown list in cell" is checked |
| Date format is wrong | Go to Format → Number and select the correct format |
| Can't see all columns | Adjust column widths by dragging the borders between column letters |

---

## Next Steps

After completing this exercise:
1. Share your sheet with the trainer for verification
2. Ask any questions you have
3. Prepare for the contest activity (independent challenge)
4. Take your quick reference card for future reference

---

**End of RMU-1 Hands-On Exercise**
