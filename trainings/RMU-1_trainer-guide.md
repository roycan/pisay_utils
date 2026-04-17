# RMU-1 Trainer Guide: Digital Records Tracking and Mail Management

## Session Metadata

| Field | Value |
|-------|-------|
| **Unit** | Records Management Unit (RMU) |
| **Session ID** | RMU-1 |
| **Session Title** | Digital Records Tracking and Mail Management |
| **Duration** | 1 hour 30 minutes (90 minutes) |
| **Prerequisites** | Session 0 (Google Workspace Fundamentals) |
| **Google Workspace Tools** | Google Sheets, Google Forms, Google Drive |
| **LibreOffice Equivalent** | LibreOffice Calc, LibreOffice Writer (optional - to be deployed campus-wide) |
| **Manual Reference** | FAM 13.1 Records Management V2_Rev2 |
| **Target Audience** | RMU staff, Records Officer, Receiving Clerks |

## Time Allocation Breakdown

| Component | Time | Notes |
|-----------|------|-------|
| **Pre-Session Video** (asynchronous) | 10-15 min | Sent 2-3 days before session |
| **In-Person Session** | 75 min | |
| ├─ Quick Q&A on Video | 5 min | Address questions from pre-session video |
| ├─ Joint Discussion | 15 min | Collaborative example with real data |
| ├─ Audience Practice | 20 min | Guided hands-on exercise |
| ├─ Contest Activity | 25 min | Independent challenge for gamification |
| └─ Wrap-up & Scoring | 10 min | Review, answer key, leaderboard update |

## Learning Objectives

By the end of this session, participants will be able to:

1. Create a digital logbook/registry in Google Sheets with the required fields per FAM 13.1 Section 3.4b
2. Auto-generate document control numbers using Google Sheets formulas (format: YYMMXX)
3. Track incoming and outgoing mail with proper timestamps and status
4. Use Google Forms for digital Records Requisition and Acknowledgement Slip
5. Organize documents in Google Drive following the Filing Chart system per FAM 13.1 Section 3.15
6. Apply LibreOffice Calc as an offline backup for the digital logbook (optional)

## Materials Needed

- Computers/laptops with internet access
- Access to PSHS Google Workspace domain
- Sample incoming mail documents (for practice)
- Printed quick reference cards (one per participant)
- Projector for demonstration
- Whiteboard or digital equivalent

## Pre-Session Video Content Summary

The pre-session video (10-15 minutes) covers:
1. **Analogy** (30 sec): Physical logbook → Google Sheet
2. **Keywords & Concepts** (2 min): Control number, timestamp, auto-fill, data validation
3. **Pattern Demonstration** (8-10 min): Building the digital registry step-by-step
4. **Quick Check Question** (30 sec): "What formula would you use to auto-generate a control number in the format YYMMXX?"

---

## In-Person Session Script

### 1. Welcome and Quick Q&A (5 minutes)

**Trainer Script:**

"Good morning/afternoon, everyone! Welcome to RMU-1: Digital Records Tracking and Mail Management.

Before we dive in, let's address any questions you might have from the pre-session video. Who has questions about the analogy, the keywords, or the pattern demonstration I showed?"

**Anticipated Questions & Answers:**

| Question | Answer |
|----------|--------|
| "Why can't we just keep using the physical logbook?" | A physical logbook has limitations: only one person can write at a time, it can be lost or damaged, and searching for old entries is time-consuming. A Google Sheet allows multiple people to work simultaneously, is backed up automatically, and you can search/filter in seconds. |
| "What happens if the internet goes down?" | That's why we have LibreOffice as backup. You can download the Sheet as .ods and work offline. When internet returns, you can re-upload or copy your entries back. (Note: LibreOffice will be deployed campus-wide before full training rollout) |
| "How do we ensure the control numbers don't duplicate?" | We'll use a formula that automatically increments the series number. The sheet tracks the last used number, so each new entry gets the next one. |
| "Can other units see our logbook?" | No, you control the sharing permissions. You can share with specific people or keep it private to RMU. |

**Trainer Script:**

"Great questions! Remember, the goal isn't to replace everything overnight—it's to make your work more efficient while maintaining compliance with FAM 13.1. Let's move to our joint discussion."

---

### 2. Joint Discussion: Building the Digital Registry (15 minutes)

**Trainer Script:**

"Now let's build our digital registry together. I'll share my screen, and we'll create a Google Sheet that matches the logbook requirements from FAM 13.1 Section 3.4b.

Per the manual, our registry must have these fields:
1. Date and Time Received
2. Control Number
3. Source or Sender
4. Subject Matter
5. Date Released
6. Personnel/Office Assigned
7. Remarks

Let's create this together."

#### Step-by-Step Demo Script

**Step 1: Create the Google Sheet**

1. Open Google Drive (drive.google.com)
2. Click **+ New** → **Google Sheets**
3. Name the sheet: `RMU_Digital_Registry_2026`
4. Click **Share** → Change to **Anyone with the link can edit** (for training purposes; in production, restrict to RMU staff)

**Step 2: Set Up Column Headers**

1. In cell A1, type: `Date/Time Received`
2. In cell B1, type: `Control Number`
3. In cell C1, type: `Source/Sender`
4. In cell D1, type: `Subject Matter`
5. In cell E1, type: `Date Released`
6. In cell F1, type: `Personnel/Office Assigned`
7. In cell G1, type: `Remarks`

**Step 3: Format Columns**

1. Select column A → Click **Format** → **Number** → **Date time**
2. Select column E → Click **Format** → **Number** → **Date**
3. Select columns B, C, D, F, G → Click **Format** → **Number** → **Plain text**
4. Select row 1 → Click **Bold** → Apply a background color (light gray or PSHS blue)

**Step 4: Auto-Generate Control Numbers**

**Trainer Script:**

"This is the most important part. Per FAM 13.1 Section 3.4b, our control number format is: `YYMMXX` where YY is the year, MM is the month, and XX is the document count for that month. For example, `260401` means the 1st document received in April 2026.

We'll use a formula to auto-generate this. Here's how:"

1. In cell B2, enter this formula:
   ```
   =IF(A2="", "", TEXT(A2, "YYMM") & TEXT(COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*"), "00"))
   ```

**Explanation of the formula:**
- `IF(A2="", "", ...)` — If no date is entered, leave the cell blank
- `TEXT(A2, "YYMM")` — Extracts the year and month from the date (e.g., 2604 for April 2026)
- `COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*")` — Counts how many documents have been received this month
- `TEXT(..., "00")` — Formats the series number as 2 digits (01, 02, 03, etc.)

2. Drag the formula down for at least 50 rows (or more based on expected monthly volume)

**Step 5: Add Data Validation for "Personnel/Office Assigned"**

**Trainer Script:**

"To ensure consistency in the 'Personnel/Office Assigned' column, let's create a dropdown list of valid offices."

1. In a separate sheet (or at the bottom of the current sheet), create a list of offices:
   - Campus Director
   - Executive Director
   - HRU
   - GSU
   - ACU
   - PRU
   - ITU
   - HSU
   - LIB
   - REG
   - RHU
   - Other

2. Select column F (Personnel/Office Assigned)
3. Click **Data** → **Data validation**
4. Under **Criteria**, select **Dropdown (from a range)**
5. Select the range containing your office list
6. Check **Show dropdown list in cell**
7. Click **Done**

**Step 6: Add Conditional Formatting for Status**

**Trainer Script:**

"Let's add visual cues. If a document has been received but not yet released (Date Released is blank), let's highlight it in yellow. If it's been released, let's highlight it in green."

1. Select the entire data range (A2:G100)
2. Click **Format** → **Conditional formatting**
3. Add rule 1:
   - Format cells if: **Custom formula is**
   - Formula: `=AND(A2<>"", E2="")`
   - Formatting style: Yellow background
4. Add rule 2:
   - Format cells if: **Custom formula is**
   - Formula: `=E2<>""`
   - Formatting style: Light green background
5. Click **Done**

**Step 7: Freeze the Header Row**

1. Click **View** → **Freeze** → **1 row**
2. This keeps your headers visible as you scroll

**Trainer Script:**

"Excellent! Our digital registry is now set up. Let's enter a sample record together."

**Sample Entry:**
- Date/Time Received: `4/16/2026 9:00:00`
- Control Number: (auto-generated) `260401`
- Source/Sender: `DOST Main Office`
- Subject Matter: `Memorandum on 2026 Budget Allocation`
- Date Released: (leave blank for now)
- Personnel/Office Assigned: `ACU`
- Remarks: `Urgent - requires immediate action`

---

### 3. Audience Practice: Guided Exercise (20 minutes)

**Trainer Script:**

"Now it's your turn! I'll give you a set of sample incoming mail documents, and you'll practice entering them into your own digital registry. I'll walk you through each step."

#### Exercise Scenario

"You are the Records Officer on duty today. The following 5 documents have arrived. Enter them into your digital registry:"

**Document 1:**
- Received: April 16, 2026 at 9:15 AM
- From: DepEd Regional Office
- Subject: Invitation to Regional Education Summit
- Assigned to: Campus Director
- Remarks: Response needed by April 30

**Document 2:**
- Received: April 16, 2026 at 9:30 AM
- From: PSHS System Office
- Subject: Updated QMS Manual (FAM 13.1 Revision)
- Assigned to: RMU
- Remarks: For review and implementation

**Document 3:**
- Received: April 16, 2026 at 10:00 AM
- From: Supplier (ABC Office Supplies)
- Subject: Delivery of printer paper and ink
- Assigned to: GSU
- Remarks: Invoice attached

**Document 4:**
- Received: April 16, 2026 at 10:45 AM
- From: Anonymous
- Subject: Concern about cafeteria food quality
- Assigned to: GSU
- Remarks: Per FAM 3.4a, forward to concerned office

**Document 5:**
- Received: April 16, 2026 at 11:00 AM
- From: PSHS Alumni Association
- Subject: Proposal for Alumni Homecoming 2026
- Assigned to: Campus Director
- Remarks: For consideration

#### Step-by-Step Guidance

**Step 1: Create Your Sheet (2 minutes)**
1. Open Google Drive
2. Create a new Google Sheet
3. Name it: `YourName_Practice_Registry`
4. Set up the 7 column headers as demonstrated

**Step 2: Apply the Control Number Formula (3 minutes)**
1. Enter the formula in cell B2
2. Drag it down for at least 10 rows
3. Verify it generates correct control numbers

**Step 3: Enter the 5 Documents (10 minutes)**
1. Enter Document 1 in row 2
2. Enter Document 2 in row 3
3. Continue for all 5 documents
4. Observe the auto-generated control numbers

**Step 4: Update Status (3 minutes)**
1. For Document 3 (GSU - printer paper), enter today's date in "Date Released" (assume GSU has already acted on it)
2. Observe the color change (yellow → green)
3. For Document 2 (RMU - QMS Manual), also mark as released

**Step 5: Search and Filter (2 minutes)**
1. Use the filter feature (click **Data** → **Create a filter**)
2. Filter by "Personnel/Office Assigned" = Campus Director
3. Count how many documents are assigned to Campus Director
4. Clear the filter

**Trainer Circulation:**

While participants work, circulate to:
- Check that formulas are entered correctly
- Ensure data is being entered in the right format
- Answer individual questions
- Provide encouragement

---

### 4. Contest Activity: Independent Challenge (25 minutes)

**Trainer Script:**

"Now for the contest activity! This is your chance to demonstrate what you've learned independently. Remember, this counts toward your unit's score in the inter-unit competition!"

#### Contest Rules

1. **Time Limit:** 20 minutes
2. **Resources Allowed:** Your quick reference card, your practice sheet, Google Help (no asking the trainer or other participants)
3. **Scoring Criteria:**
   - **Completion (40 points):** All required entries completed
   - **Accuracy (40 points):** All data entered correctly, formulas working
   - **Independence (20 points):** Completed without assistance

#### Contest Scenario

"You are the Records Officer on April 20, 2026. The following 8 documents have arrived throughout the day. Your task is to:

1. Create a new Google Sheet named `RMU_Contest_Registry_YourName`
2. Set up the digital registry with all 7 required fields
3. Apply the auto-generating control number formula
4. Add data validation for "Personnel/Office Assigned"
5. Enter all 8 documents
6. Mark 3 of them as released (your choice which ones)
7. Filter to show only documents assigned to HRU
8. Count how many documents are still pending (not released)
9. Write the answer in cell H1: "Pending documents: X"

**The 8 Documents:**

| # | Date/Time | Source/Sender | Subject | Assigned To | Remarks |
|---|-----------|---------------|---------|-------------|---------|
| 1 | 4/20/2026 8:00 AM | CHED | Memorandum on Tuition Fee Guidelines | ACU | For review and compliance |
| 2 | 4/20/2026 8:30 AM | PSHS System | Invitation to Annual Planning Workshop | Campus Director | RSVP by April 25 |
| 3 | 4/20/2026 9:00 AM | Job Applicant | Application for Faculty Position | HRU | Include resume and credentials |
| 4 | 4/20/2026 9:45 AM | DOST | Notice of Grant Approval | PRU | For procurement of equipment |
| 5 | 4/20/2026 10:30 AM | Parent | Complaint about dormitory facilities | RHU | Urgent - investigate |
| 6 | 4/20/2026 11:15 AM | IT Vendor | Proposal for Network Upgrade | ITU | For technical evaluation |
| 7 | 4/20/2026 1:00 PM | Student Council | Request for Funding of Science Fair | ACU | Budget proposal attached |
| 8 | 4/20/2026 2:30 PM | Anonymous | Report on missing lab equipment | GSU | For investigation |

**Additional Challenge (Bonus 10 points):**
- Create a simple formula in cell I1 that counts how many documents are assigned to HRU
- Hint: Use the COUNTIF function

#### Submission Instructions

1. When finished, share your sheet with the trainer (edit access)
2. Raise your hand to indicate completion
3. The trainer will verify your work and record your score

---

### 5. Wrap-up, Answer Key, and Scoring (10 minutes)

#### Answer Key

**Expected Control Numbers (assuming April 2026):**
- Document 1: 260401
- Document 2: 260402
- Document 3: 260403
- Document 4: 260404
- Document 5: 260405
- Document 6: 260406
- Document 7: 260407
- Document 8: 260408

**Filter for HRU:**
- Only Document 3 should appear

**Pending Documents Count:**
- If you marked 3 as released, then 5 are pending
- Answer in cell H1: "Pending documents: 5"

**Bonus Formula:**
```
=COUNTIF(F2:F9, "HRU")
```
- Expected result: 1

#### Scoring Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **Completion** | 40 pts | All 8 documents entered, all 7 columns set up, formula applied |
| **Accuracy** | 40 pts | Control numbers correct, data entered accurately, filter working |
| **Independence** | 20 pts | Completed without asking for help |
| **Bonus** | 10 pts | COUNTIF formula correct |
| **Total** | 110 pts | |

#### Leaderboard Update

**Trainer Script:**

"Let's update our leaderboard! I'll record each unit's scores based on how many participants completed the contest successfully."

| Unit | Participants | Completed | Average Score | Total Points |
|------|--------------|-----------|---------------|--------------|
| RMU | ___ | ___ | ___ | ___ |
| HSU | ___ | ___ | ___ | ___ |
| LIB | ___ | ___ | ___ | ___ |
| ... | ... | ... | ... | ... |

*(Fill in during actual training)*

---

## Troubleshooting Tips

### Common Mistakes and Solutions

| Mistake | Solution |
|---------|----------|
| **Control number formula shows #REF! error** | Check that the formula references the correct range. The `$B$1:B1` part should use mixed references (absolute for the start, relative for the end). |
| **Control numbers not incrementing** | Make sure the COUNTIF function is checking the correct pattern. The wildcard `*` after the YYMM ensures it counts all entries for that month. |
| **Date format not showing time** | Select the cell, go to Format → Number → Date time (not just Date). |
| **Data validation dropdown not appearing** | Make sure you selected the entire column before applying data validation. Also check that "Show dropdown list in cell" is checked. |
| **Conditional formatting not working** | Verify that the formula is correct and that you're applying it to the right range. Use the "Apply to range" field to specify the exact cells. |
| **Can't find my sheet in Google Drive** | Check that you named it correctly. Use the search bar at the top of Drive. |
| **Formula is visible instead of the result** | Press Enter after typing the formula. If it still shows text, check that the cell is formatted as "Automatic" not "Plain text". |

### Tips for Success

1. **Always save your work** — Google Sheets auto-saves, but it's good practice to verify
2. **Use keyboard shortcuts** — Ctrl+Z to undo, Ctrl+C/V to copy/paste
3. **Test your formulas** — Enter sample data to verify they work before relying on them
4. **Keep a backup** — Download your sheet as .ods (LibreOffice) regularly (once LibreOffice is deployed)
5. **Use comments** — Right-click a cell → Insert comment to add notes without cluttering the data

---

## Extension Activities (If Time Permits)

### Activity 1: Google Forms for Records Requisition

**Trainer Script:**

"Per FAM 13.1 Section 4.6, we have a Records Requisition and Acknowledgement Slip. Let's create a digital version using Google Forms."

1. Go to forms.google.com
2. Click **+ Blank**
3. Name the form: `Records Requisition and Acknowledgement Slip`
4. Add questions:
   - Name of Requesting Party (Short answer)
   - Office/Unit (Dropdown)
   - Record/Document Requested (Paragraph)
   - Purpose (Paragraph)
   - Date Needed (Date)
5. Click **Send** → Copy the link
6. Share the link with units for digital requests

### Activity 2: Google Drive Folder Structure

**Trainer Script:**

"Per FAM 13.1 Section 3.15, we need to organize files according to the Filing Chart. Let's set up a Google Drive folder structure."

1. In Google Drive, create a folder: `RMU_Records_2026`
2. Inside, create subfolders:
   - `01_Incoming_Mail`
   - `02_Outgoing_Mail`
   - `03_Issuances_Directives`
   - `04_Certified_Copies`
   - `05_Inactive_Records`
3. Share the folder with appropriate RMU staff

### Activity 3: LibreOffice Backup (Optional)

**Trainer Script:**

"For those who want to practice working offline, let's try LibreOffice. This is optional since LibreOffice will be installed campus-wide before the actual training rollout."

1. Open your Google Sheet
2. Click **File** → **Download** → **OpenDocument Spreadsheet (.ods)**
3. Open the downloaded file in LibreOffice Calc
4. Make a few edits
5. Save the file
6. When internet returns, you can upload it back to Google Drive

---

## Assessment and Follow-up

### Immediate Assessment

The contest activity serves as the immediate practical assessment. Participants who score 80% or higher have demonstrated competency.

### 60-Day Follow-up (Per FAM 4.7 Section 4.6)

Two months after training, the RMU Head should complete a Training Effectiveness Form to assess:

1. **Application on the Job:** Are staff using the digital registry in daily operations?
2. **Efficiency Gains:** Has the time to process mail decreased?
3. **Error Reduction:** Have errors in control numbering or data entry decreased?
4. **Challenges Encountered:** What difficulties are staff facing?
5. **Additional Training Needed:** What topics need reinforcement?

### Recommended Next Steps

1. **Implement the digital registry** in daily operations within 1 week
2. **Train additional RMU staff** who didn't attend this session
3. **Create unit-specific folders** in Google Drive per the Filing Chart
4. **Set up a weekly backup routine** using LibreOffice .ods format (once LibreOffice is deployed)
5. **Schedule RMU-2** (Records Inventory, Disposition, and Electronic Records) for next month

---

## Pre-Training Setup Recommendations

Before the first RMU-1 session:

1. **Create a shared Google Drive folder** for all RMU training materials
2. **Set up a template sheet** that participants can copy (saves time during training)
3. **Test the control number formula** with actual PSHS-MC data to ensure it works as expected
4. **Prepare the leaderboard** in Google Sheets with read-only access for all participants
5. **Set up a "RMU Help" channel** in Google Chat for ongoing questions

---

## Video Production Tips

For the pre-session video:

1. **Use a screen recording tool** like Loom, OBS, or Google Meet recording
2. **Keep the video under 15 minutes** to maintain engagement
3. **Add captions** for accessibility
4. **Host on Google Drive** and share the link 48 hours before the session
5. **Test the video** on multiple devices before distribution

---

## Follow-Up Support

After the session:

1. **Schedule a 15-minute check-in** 1 week later to address issues
2. **Create a shared "RMU Help" channel** in Google Chat for ongoing questions
3. **Appoint "digital champions"** in RMU who can help colleagues
4. **Collect feedback** on the training materials for continuous improvement

---

## References

- **FAM 13.1 Records Management V2_Rev2** — Sections 3.4b (Registry Sheet), 3.7 (Electronic Records), 3.15 (File Classification), 4.2 (Handling Incoming Electronic Communications), 4.6 (Request of Inactive Records)
- **Google Sheets Help Center** — sheets.google.com/support
- **Google Forms Help Center** — forms.google.com/support
- **LibreOffice Documentation** — help.libreoffice.org

---

## Trainer Notes

- **Pace:** Adjust the timing based on participant comfort level. If participants are struggling with formulas, spend more time on Step 4 and reduce time on extensions.
- **Analogies:** Emphasize the physical logbook → digital logbook analogy throughout. This helps participants relate the new tool to their existing knowledge.
- **Real Data:** If possible, use actual anonymized data from RMU for the practice and contest activities. This makes the training more relevant.
- **Gamification:** Keep the leaderboard visible and update it after each session. This motivates participants and creates healthy competition.
- **Follow-up:** Schedule a check-in with the RMU Head 2 weeks after training to address any issues and ensure adoption.

---

**End of RMU-1 Trainer Guide**
