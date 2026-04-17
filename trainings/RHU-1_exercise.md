# RHU-1 Hands-On Exercise: Residence Hall Administration and Monitoring

**Duration:** 7 minutes
**Format:** Guided step-by-step exercise
**Prerequisites:** Watched pre-session video, Session 0 completed

---

## Exercise Scenario

You are an RHU staff member preparing for the upcoming school year. Your task is to practice creating digital tools for residence hall administration using Google Workspace.

---

## Step-by-Step Instructions

### Part 1: Create a Simple Application Form (2 minutes)

#### Task 1: Create the Form

1. Open your web browser and go to `forms.google.com`
2. Click **+ Blank**
3. In the form title, type: `Practice Residence Hall Application`
4. Add the following questions:

**Question 1:**
- Title: Student Information
- Question: Full Name (Short answer)

**Question 2:**
- Question: Student ID (Short answer)

**Question 3:**
- Question: Grade Level (Dropdown)
- Options: Grade 7, Grade 8, Grade 9, Grade 10, Grade 11, Grade 12

**Question 4:**
- Question: Contact Number (Short answer)

5. Click **Send** → Click the **Link** tab → Click **Shorten URL**
6. Copy the link and share with a colleague

**Expected Outcome:** You have a Google Form with 4 questions and a shareable link.

[SCREENSHOT: Google Form with 4 questions]

---

### Part 2: Create a Resident Tracker (2 minutes)

#### Task 2: Create the Spreadsheet

1. Go to `drive.google.com`
2. Click **+ New** → **Google Sheets**
3. Name the sheet: `Practice_Resident_Tracker`

4. Set up column headers in row 1:
   - Cell A1: `Student Name`
   - Cell B1: `Room Assignment`
   - Cell C1: `Contract Status`
   - Cell D1: `Notes`

5. Format the header row:
   - Select row 1 → Click **Bold** → Add a background color (light gray or light blue)

6. Add data validation for Contract Status:
   - Select column C
   - Click **Data** → **Data validation**
   - Choose **Dropdown**
   - Options: `Pending`, `Active`, `Terminated`
   - Check **Show dropdown list in cell**
   - Click **Done**

7. Add conditional formatting:
   - Select columns A through D
   - Click **Format** → **Conditional formatting**
   - Add rule 1:
     - Format cells if: **Custom formula is**
     - Formula: `=$C2="Active"`
     - Formatting: Light green background
   - Click **Done**

8. Enter 2 sample residents:
   - Row 2: Juan dela Cruz, Room 101, Active, No issues
   - Row 3: Maria Santos, Room 102, Pending, Awaiting contract

**Expected Outcome:** You have a resident tracker with data validation and conditional formatting.

[SCREENSHOT: Resident tracker with 2 sample residents]

---

### Part 3: Create a Simple Checklist (2 minutes)

#### Task 3: Create the Checklist Form

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Practice Room Checklist`

4. Add the following questions:

**Question 1:**
- Title: Room Information
- Question: Room Number (Short answer)

**Question 2:**
- Title: Cleanliness
- Question: Floor is clean (Checkbox)
- Options: `Passed`, `Needs Improvement`

**Question 3:**
- Question: Bed is properly made (Checkbox)
- Options: `Passed`, `Needs Improvement`

**Question 4:**
- Question: Overall Condition (Dropdown)
- Options: `Excellent`, `Good`, `Fair`, `Poor`

5. Click **Responses** tab → Click **Link to Sheets**
6. Create a new spreadsheet: `Practice_Checklist_Responses`
7. Click **Create**

8. Submit a test response:
   - Go back to the form
   - Fill in: Room 101, Floor: Passed, Bed: Passed, Overall: Good
   - Click **Submit**

9. View the response spreadsheet to verify data was collected

**Expected Outcome:** You have a checklist form with 4 questions and responses collected in a spreadsheet.

[SCREENSHOT: Checklist form and response spreadsheet]

---

### Part 4: Upload to Google Drive (1 minute)

#### Task 4: Organize Files

1. Go to `drive.google.com`
2. Click **+ New** → **Folder**
3. Name the folder: `RHU_Practice_YourName` (replace "YourName" with your actual name)

4. Upload the files you created:
   - Click the folder to open it
   - Click **+ New** → **File upload**
   - Select the Google Form link (or create a document with the link)
   - Upload the resident tracker spreadsheet
   - Upload the checklist response spreadsheet

5. Share the folder with the trainer:
   - Right-click the folder → **Share**
   - Enter trainer's email address
   - Choose **Editor** access
   - Click **Send**

**Expected Outcome:** All files are organized in a folder and shared with the trainer.

[SCREENSHOT: Google Drive folder with uploaded files]

---

## Self-Check Answers

After completing the exercise, verify your work against these expected results:

### Question 1: Did you create an application form with at least 3 questions?
**Answer:** Yes, if you have a Google Form with student information questions.

### Question 2: Did you create a resident tracker with data validation?
**Answer:** Yes, if you have a spreadsheet with a dropdown for Contract Status.

### Question 3: Did you add conditional formatting to the resident tracker?
**Answer:** Yes, if Active contracts show in green (or your chosen color).

### Question 4: Did you create a checklist form?
**Answer:** Yes, if you have a Google Form with checklist items.

### Question 5: Did you submit a test response to the checklist?
**Answer:** Yes, if the response appears in the linked spreadsheet.

### Question 6: Did you organize all files in a Google Drive folder?
**Answer:** Yes, if you have a folder named `RHU_Practice_YourName` with all files.

---

## Challenge Variations

### Basic Challenge (Completed Above)
- Create an application form
- Create a resident tracker
- Create a checklist form
- Upload all files to Google Drive

### Intermediate Challenge (If You Finish Early)
- Add a formula to calculate the number of active residents
- Create a simple contract template in Google Docs
- Add more questions to the application form (health information, emergency contacts)

### Advanced Challenge (For Extra Practice)
- Create a leave pass tracker with duration calculation formula
- Set up a Google Form for leave pass requests
- Create a dashboard showing summary statistics for all RHU data

---

## Troubleshooting

If you encounter issues, check these common problems:

| Problem | Solution |
|---------|----------|
| Form responses not appearing | Check that "Link to Sheets" is configured in Form Settings |
| Conditional formatting not working | Verify formula syntax and that it's applied to the correct range |
| Data validation dropdown not showing | Ensure "Show dropdown list in cell" is checked |
| Can't find uploaded files | Check the folder you created or search by filename |
| Formula shows error | Check that referenced cells contain the correct data type |
| Can't share folder | Verify recipient has PSHS Google account and correct email address |

---

## SSM References

Remember these key references from the manuals:

**SSM 5.1 Evaluation of Students Application for Residence Hall Accommodation:**
- Section 3.3: Evaluation for Admission (grade level, scholarship, distance)
- Section 4.0: Procedures (application distribution, evaluation, notification)
- Section 5.0: List of Forms (Application Form, Contract, Appliance Form, Waiver)

**SSM 5.2 Residence Hall Accommodation:**
- Section 4.2.1: Leave Pass/Return Slip Procedure
- Section 4.3.1: Room Upkeep (Good Housekeeping Checklist)
- Section 5.0: List of Forms (Contract, Leave Pass, Checklist)

---

## Next Steps

After completing this exercise:
1. Share your `RHU_Practice_YourName` folder with the trainer for verification
2. Ask any questions you have
3. Prepare for additional RHU training sessions
4. Take your quick reference card for future reference

---

## Keyboard Shortcuts for Google Forms

| Action | Windows | Mac |
|--------|---------|-----|
| New question | `Ctrl + K` | `Cmd + K` |
| Duplicate question | `Ctrl + D` | `Cmd + D` |
| Move question up | `Ctrl + Up` | `Cmd + Up` |
| Move question down | `Ctrl + Down` | `Cmd + Down` |
| Preview form | `Ctrl + P` | `Cmd + P` |

---

## Keyboard Shortcuts for Google Sheets

| Action | Windows | Mac |
|--------|---------|-----|
| New row | `Alt + I`, then `R` | `Ctrl + Option + I`, then `R` |
| Format as bold | `Ctrl + B` | `Cmd + B` |
| Format as italic | `Ctrl + I` | `Cmd + I` |
| Insert date | `Ctrl + ;` | `Cmd + ;` |
| Insert time | `Ctrl + Shift + ;` | `Cmd + Shift + ;` |
| Fill down | `Ctrl + D` | `Cmd + D` |

---

**End of RHU-1 Hands-On Exercise**
