# RHU-1 Trainer Guide: Residence Hall Administration and Monitoring

## Session Metadata

| Field | Value |
|-------|-------|
| **Unit** | Residence Hall Unit (RHU) |
| **Session ID** | RHU-1 |
| **Session Title** | Residence Hall Administration and Monitoring |
| **Duration** | 1 hour 15 minutes (75 minutes) |
| **Prerequisites** | Session 0 (Google Workspace Fundamentals) |
| **Google Workspace Tools** | Google Forms, Google Sheets, Google Docs, Google Drive |
| **LibreOffice Equivalent** | LibreOffice Writer, Calc (optional - to be deployed campus-wide) |
| **Manual Reference** | SSM 5.1 Evaluation of Students Application for Residence Hall Accommodation, SSM 5.2 Residence Hall Accommodation |
| **Target Audience** | RHU staff, Residence Hall Head, Residence Hall Attendants |

## Time Allocation Breakdown

| Component | Time | Notes |
|-----------|------|-------|
| **Pre-Session Video** (asynchronous) | 10-15 min | Sent 2-3 days before session |
| **In-Person Session** | 75 min | |
| ├─ Welcome and Q&A on Video | 5 min | Address questions from pre-session video |
| ├─ Digital Residence Hall Application | 15 min | Google Forms for applications |
| ├─ Resident Management Tracker | 15 min | Google Sheets for tracking residents |
| ├─ Contract Templates & Waivers | 10 min | Google Docs for contracts |
| ├─ Good Housekeeping Checklist | 10 min | Digital form for inspections |
| ├─ Leave Pass Tracking | 10 min | Timestamp-based tracking |
| ├─ Audience Practice | 7 min | Guided hands-on exercise |
| └─ Wrap-up & Scoring | 3 min | Review, answer key, leaderboard update |

## Learning Objectives

By the end of this session, participants will be able to:

1. Create a digital Residence Hall Application Form using Google Forms (per SSM 5.1)
2. Build a resident management tracker in Google Sheets with room assignments and contract status
3. Create and use Google Docs templates for Residence Hall Contracts and Parent/Guardian Waivers (per SSM 5.1)
4. Digitize the Good Housekeeping Checklist using Google Forms (per SSM 5.2)
5. Track Leave Pass and Return Slips with automatic timestamps in Google Sheets (per SSM 5.2)
6. Organize RHU documents in Google Drive following proper folder structure
7. Apply LibreOffice as offline backup for RHU documents (optional)

## Materials Needed

- Computers/laptops with internet access
- Access to PSHS Google Workspace domain
- Sample residence hall application data for practice
- Printed quick reference cards (one per participant)
- Projector for demonstration
- Whiteboard or digital equivalent

## Pre-Session Video Content Summary

The pre-session video (10-15 minutes) covers:
1. **Analogy** (30 sec): Physical logbook → Google Sheet
2. **Keywords & Concepts** (2 min): Digital forms, timestamp tracking, conditional formatting, data validation
3. **Pattern Demonstration** (8-10 min): Building RHU digital tools step-by-step
4. **Quick Check Question** (30 sec): "What Google Workspace tool would you use to create a digital residence hall application form?"

---

## In-Person Session Script

### 1. Welcome and Quick Q&A (5 minutes)

**Trainer Script:**

"Good morning/afternoon, everyone! Welcome to RHU-1: Residence Hall Administration and Monitoring.

This session will transform how RHU manages residence hall operations using Google Workspace. We'll create digital tools for applications, resident tracking, contracts, housekeeping inspections, and leave pass monitoring.

Before we dive in, let's address any questions you might have from the pre-session video."

**Anticipated Questions & Answers:**

| Question | Answer |
|----------|--------|
| "Why can't we keep using paper forms?" | Paper forms are time-consuming to process, hard to track, and can be lost. Digital forms automatically collect data, are searchable, and multiple staff can access them simultaneously. |
| "What about parents who don't have internet?" | Parents can still submit paper forms. RHU staff can enter the data into the digital system. The digital system enhances, not replaces, existing processes. |
| "How do we handle signatures digitally?" | For now, we'll use Google Forms to collect data, and print contracts for physical signatures. As PSHS adopts digital signatures, we can transition to fully digital processes. |
| "Can we track who's in the residence hall at any time?" | Yes! With the resident tracker and leave pass system, you'll always know who's present, who's on leave, and when they're expected to return. |

**Trainer Script:**

"Great questions! Remember, the goal is to make RHU operations more efficient while maintaining compliance with SSM 5.1 and 5.2. Let's move to our first topic."

---

### 2. Digital Residence Hall Application (15 minutes)

**Trainer Script:**

"Per SSM 5.1, the Residence Hall Application Form is distributed during enrollment and collected by the Registrar. Let's create a digital version using Google Forms."

#### Step-by-Step Demo Script

**Step 1: Create the Google Form**

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Residence Hall Application Form - SY 2026-2027`

**Step 2: Add Questions (Based on SSM 5.1)**

[SCREEN: Creating form questions]

**Trainer Script:**

"Let's add the necessary questions for the application. Per SSM 5.1 Section 3.3.1, we need to evaluate based on grade level, scholarship categorization, and distance from campus.

**Question 1: Student Information**
- Title: Student Information
- Description: Please provide your personal information
- Question 1: Full Name (Short answer)
- Question 2: Student ID Number (Short answer)
- Question 3: Grade Level (Dropdown: Grade 7, Grade 8, Grade 9, Grade 10, Grade 11, Grade 12)
- Question 4: Scholarship Category (Dropdown: Full Scholar, Partial Scholar, Non-Scholar)
- Question 5: Gender (Dropdown: Male, Female)

**Question 2: Contact Information**
- Title: Contact Information
- Question 6: Home Address (Paragraph)
- Question 7: Distance from Campus (Dropdown: < 5km, 5-10km, 10-20km, > 20km)
- Question 8: Parent/Guardian Name (Short answer)
- Question 9: Parent/Guardian Contact Number (Short answer)
- Question 10: Parent/Guardian Email (Short answer)

**Question 3: Health Information**
- Title: Health Information
- Question 11: Do you have any medical conditions? (Yes/No)
- Question 12: If yes, please describe (Paragraph - conditional on Yes)
- Question 13: Emergency Contact Name (Short answer)
- Question 14: Emergency Contact Relationship (Short answer)
- Question 15: Emergency Contact Number (Short answer)

**Question 4: Agreement**
- Title: Agreement
- Question 16: I understand that accommodation is subject to availability and approval (Required checkbox)
- Question 17: I agree to comply with all Residence Hall rules and regulations (Required checkbox)"

**Step 3: Configure Form Settings**

1. Click **Settings** (gear icon)
2. Under **Presentation**, check **Collect email addresses** (to track who submitted)
3. Under **Responses**, check **Limit to 1 response** (if needed)
4. Click **Save**

**Step 4: Share the Form**

1. Click **Send** (top right)
2. Click the **Link** tab
3. Click **Shorten URL**
4. Copy the link
5. Share with Registrar for distribution during enrollment

**Step 5: View Responses**

1. Click **Responses** tab
2. Responses automatically populate in a Google Sheet
3. Click the green Sheets icon to open the response spreadsheet

**Trainer Script:**

"Excellent! Now all applications are collected in one spreadsheet. This makes evaluation much easier per SSM 5.1 Section 3.3.2, where the Residence Hall Committee evaluates all applications."

---

### 3. Resident Management Tracker (15 minutes)

**Trainer Script:**

"Now let's create a resident management tracker in Google Sheets. This will help us track room assignments, contract status, and appliance declarations per SSM 5.1 and 5.2."

#### Step-by-Step Demo Script

**Step 1: Create the Google Sheet**

1. Go to `drive.google.com`
2. Click **+ New** → **Google Sheets**
3. Name the sheet: `RHU_Resident_Tracker_2026-2027`

**Step 2: Set Up Column Headers**

[SCREEN: Typing column headers]

**Trainer Script:**

"Per SSM 5.1 and 5.2, let's set up these columns:

Row 1 headers:
- A: Student Name
- B: Student ID
- C: Grade Level
- D: Gender
- E: Room Assignment
- F: Bed Number
- G: Contract Status
- H: Contract Date
- I: Appliances Declared
- J: Appliance Fee Paid
- K: Monthly Fee Paid
- L: Parent/Guardian Contact
- M: Emergency Contact
- N: Notes"

**Step 3: Format Columns**

1. Select row 1 → **Bold** → Add background color
2. Select column G (Contract Status) → **Data** → **Data validation**
3. Choose **Dropdown** → Options: Pending, Signed, Active, Terminated
4. Select column I (Appliances Declared) → **Data** → **Data validation**
5. Choose **Checkbox** → For declaring appliances

**Step 4: Add Conditional Formatting**

[SCREEN: Setting up conditional formatting]

**Trainer Script:**

"Let's add visual cues for contract status.

1. Select columns A through N
2. Click **Format** → **Conditional formatting**
3. Add rule 1:
   - Format cells if: **Custom formula is**
   - Formula: `=$G2="Pending"`
   - Formatting: Yellow background
4. Add rule 2:
   - Format cells if: **Custom formula is**
   - Formula: `=$G2="Active"`
   - Formatting: Green background
5. Add rule 3:
   - Format cells if: **Custom formula is**
   - Formula: `=$G2="Terminated"`
   - Formatting: Red background"

**Step 5: Create a Summary Section**

[SCREEN: Adding summary formulas]

**Trainer Script:**

"At the bottom of the sheet, let's add a summary:

Row 50: Summary Statistics
Row 51: Total Residents: `=COUNTA(A2:A49)`
Row 52: Active Contracts: `=COUNTIF(G2:G49, "Active")`
Row 53: Pending Contracts: `=COUNTIF(G2:G49, "Pending")`
Row 54: With Appliances: `=COUNTIF(I2:I49, TRUE)`

This gives you a quick overview of residence hall occupancy."

---

### 4. Contract Templates & Waivers (10 minutes)

**Trainer Script:**

"Per SSM 5.1 Section 4, the Residence Hall Head distributes residence hall contracts, appliance forms, and parent/guardian waivers. Let's create templates for these in Google Docs."

#### Step-by-Step Demo Script

**Step 1: Create Residence Hall Contract Template**

1. Go to `drive.google.com`
2. Click **+ New** → **Google Docs**
3. Name the document: `Residence_Hall_Contract_Template`

[SCREEN: Typing contract template]

**Trainer Script:**

"Type the contract template. Here's a basic structure:

```
RESIDENCE HALL CONTRACT
Philippine Science High School - Main Campus
School Year 2026-2027

This Contract is made and entered into by and between:

PHILIPPINE SCIENCE HIGH SCHOOL - MAIN CAMPUS, represented by the Campus Director,
hereinafter referred to as the SCHOOL,

and

STUDENT NAME, Student ID: [STUDENT_ID], Grade Level: [GRADE_LEVEL],
hereinafter referred to as the INTERN/RESIDENT,

WHEREAS, the SCHOOL agrees to provide accommodation to the INTERN/RESIDENT
subject to the terms and conditions herein stated:

SECTION 1: ACCOMMODATION
The SCHOOL shall provide lodging accommodation to the INTERN/RESIDENT at the
Residence Hall for the School Year 2026-2027.

SECTION 2: FEES
The INTERN/RESIDENT shall pay a monthly lodging fee of [AMOUNT] and
appliance/electrical devices fee as prescribed by current policy.

SECTION 3: RULES AND REGULATIONS
The INTERN/RESIDENT shall strictly follow all rules and regulations of the
Residence Hall as stated in the Residence Hall Handbook and PSHS Code of Conduct.

SECTION 4: TERMINATION
This contract may be terminated by the SCHOOL for violation of rules and
regulations, non-payment of fees, or other just cause.

IN WITNESS WHEREOF, the parties have executed this Contract on this
____ day of ____________, 2026.

_________________________                    _________________________
CAMPUS DIRECTOR                             INTERN/RESIDENT
```

**Step 2: Create Merge Fields for Mail Merge**

1. Identify fields to personalize: [STUDENT_ID], [GRADE_LEVEL], [AMOUNT]
2. These will be replaced with actual data when generating individual contracts

**Step 3: Create Parent/Guardian Waiver Template**

1. Create a new Google Doc: `Parent_Guardian_Waiver_Template`
2. Type the waiver template (similar structure to contract)
3. Include fields for parent/guardian signature

**Step 4: Create Appliance Declaration Form**

1. Create a new Google Doc: `Appliance_Declaration_Template`
2. Include list of allowed appliances and declaration fields

**Trainer Script:**

"These templates can be printed for physical signatures. In the future, as PSHS adopts digital signatures, we can transition to fully digital contracts."

---

### 5. Good Housekeeping Checklist (10 minutes)

**Trainer Script:**

"Per SSM 5.2 Section 4.3.1, the Residence Hall Head inspects each room using the Good Housekeeping Checklist. Let's digitize this using Google Forms."

#### Step-by-Step Demo Script

**Step 1: Create the Google Form**

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Good Housekeeping Checklist`

**Step 2: Add Questions (Based on SSM 5.2)**

[SCREEN: Creating checklist questions]

**Trainer Script:**

"Let's create the checklist questions. We'll use checkbox questions for each item.

**Section 1: Room Information**
- Title: Room Information
- Question 1: Room Number (Short answer)
- Question 2: Date of Inspection (Date)
- Question 3: Inspector Name (Short answer)

**Section 2: Cleanliness**
- Title: Cleanliness
- Question 4: Floor is clean and free of debris (Checkbox: Passed, Needs Improvement)
- Question 5: Bed is properly made (Checkbox: Passed, Needs Improvement)
- Question 6: Windows are clean (Checkbox: Passed, Needs Improvement)
- Question 7: Trash is properly disposed (Checkbox: Passed, Needs Improvement)

**Section 3: Safety and Security**
- Title: Safety and Security
- Question 8: Door locks are functional (Checkbox: Passed, Needs Improvement)
- Question 9: Electrical outlets are safe (Checkbox: Passed, Needs Improvement)
- Question 10: No prohibited items found (Checkbox: Passed, Needs Improvement)
- Question 11: Fire extinguisher is accessible (Checkbox: Passed, Needs Improvement)

**Section 4: Overall Assessment**
- Title: Overall Assessment
- Question 12: Overall Room Condition (Dropdown: Excellent, Good, Fair, Poor)
- Question 13: Comments/Recommendations (Paragraph)
- Question 14: Follow-up Required? (Yes/No)
- Question 15: If yes, specify follow-up action (Paragraph - conditional on Yes)"

**Step 3: Configure Response Destination**

1. Click **Responses** tab
2. Click **Link to Sheets**
3. Create a new spreadsheet: `Good_Housekeeping_Responses`
4. This will collect all inspection data

**Step 4: Add Conditional Formatting to Response Sheet**

1. Open the response spreadsheet
2. Select the data range
3. Add conditional formatting to highlight "Needs Improvement" items in red
4. Add conditional formatting to highlight "Poor" overall condition in red

**Trainer Script:**

"Now you can conduct inspections on a tablet or mobile device, and all data is automatically collected in one spreadsheet. This makes tracking room conditions and follow-ups much easier per SSM 5.2."

---

### 6. Leave Pass Tracking (10 minutes)

**Trainer Script:**

"Per SSM 5.2 Section 4.2.1, the Residence Hall Head receives and logs student leave passes. Let's create a tracking system with automatic timestamps."

#### Step-by-Step Demo Script

**Step 1: Create the Google Sheet**

1. Go to `drive.google.com`
2. Click **+ New** → **Google Sheets**
3. Name the sheet: `Leave_Pass_Tracker_2026-2027`

**Step 2: Set Up Column Headers**

[SCREEN: Typing column headers]

**Trainer Script:**

"Set up these columns:

Row 1 headers:
- A: Student Name
- B: Student ID
- C: Grade Level
- D: Date of Leave
- E: Time Out
- F: Destination
- G: Purpose
- H: Parent/Guardian Notified
- I: Approved By
- J: Date of Return
- K: Time In
- L: Duration (Hours)
- M: Status
- N: Notes"

**Step 3: Add Formulas**

[SCREEN: Adding formulas]

**Trainer Script:**

"Let's add formulas for automatic calculations:

Column L (Duration): In cell L2, enter:
```
=IF(AND(K2<>"",E2<>""), (K2-E2)*24, "")
```
This calculates the duration in hours between time out and time in.

Column M (Status): In cell M2, enter:
```
=IF(J2="", "On Leave", IF(J2<>"", "Returned", ""))
```
This shows whether the student is still on leave or has returned."

**Step 4: Add Conditional Formatting**

1. Select columns A through N
2. Add conditional formatting:
   - If Status = "On Leave": Yellow background
   - If Status = "Returned": Green background
   - If Duration > 24 hours (overnight): Orange background

**Step 5: Create a Leave Pass Form (Optional)**

[SCREEN: Creating leave pass form]

**Trainer Script:**

"You can also create a Google Form for students to submit leave pass requests:

1. Create a new Google Form: `Leave_Pass_Request`
2. Add questions for student information, destination, purpose, dates
3. Share the form with students
4. Responses go to a spreadsheet
5. RHU staff can review and approve/reject requests

This streamlines the leave pass process per SSM 5.2."

---

### 7. Audience Practice: Guided Exercise (7 minutes)

**Trainer Script:**

"Now it's your turn! I'll guide you through a quick exercise. Follow along with me."

#### Exercise Steps

**Step 1: Create a Simple Application Form (2 minutes)**
1. Go to `forms.google.com`
2. Create a new form named `Practice_Application`
3. Add 3 questions: Name, Grade Level, Contact Number
4. Click **Send** → Copy the link
5. Share with a colleague

**Step 2: Create a Resident Tracker (2 minutes)**
1. Create a new Google Sheet named `Practice_Tracker`
2. Add headers: Name, Room, Status
3. Add data validation for Status (Pending, Active)
4. Add conditional formatting (Green for Active)
5. Enter 2 sample residents

**Step 3: Create a Simple Checklist (2 minutes)**
1. Create a new Google Form named `Practice_Checklist`
2. Add 3 checklist items with Passed/Needs Improvement options
3. Submit a test response
4. View the response spreadsheet

**Step 4: Upload to Google Drive (1 minute)**
1. Create a folder named `RHU_Practice_YourName`
2. Upload all files you created
3. Share the folder with the trainer

**Trainer Circulation:**

While participants work, circulate to:
- Check that forms are created correctly
- Ensure data validation is applied
- Verify conditional formatting is working
- Answer individual questions
- Provide encouragement

---

### 8. Wrap-up, Answer Key, and Scoring (3 minutes)

#### Answer Key

**Expected Outputs:**
- Application form created with 3 questions
- Resident tracker with headers, data validation, and conditional formatting
- Checklist form with 3 items
- All files uploaded to Google Drive

#### Scoring Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **Completion** | 40 pts | All 4 tasks completed |
| **Accuracy** | 40 pts | Forms and sheets created correctly |
| **Independence** | 20 pts | Completed without asking for help |
| **Total** | 100 pts | |

#### Leaderboard Update

**Trainer Script:**

"Let's update our leaderboard! I'll record each unit's scores based on how many participants completed the exercise successfully."

| Unit | Participants | Completed | Average Score | Total Points |
|------|--------------|-----------|---------------|--------------|
| RHU | ___ | ___ | ___ | ___ |
| ... | ... | ... | ... | ... |

*(Fill in during actual training)*

---

## Troubleshooting Tips

### Common Mistakes and Solutions

| Mistake | Solution |
|---------|----------|
| Form responses not appearing | Check that "Link to Sheets" is configured in Form Settings |
| Conditional formatting not working | Verify formula syntax and that it's applied to the correct range |
| Data validation dropdown not showing | Ensure "Show dropdown list in cell" is checked |
| Can't find uploaded files | Check "Shared with me" or search by filename |
| Formula shows #VALUE! error | Check that referenced cells contain the correct data type |
| Can't share folder | Verify recipient has PSHS Google account and correct email address |

### Tips for Success

1. **Use consistent naming** for files and folders
2. **Set up templates** at the start of each school year
3. **Train students** on how to use digital forms
4. **Regularly back up** data (download as .ods for LibreOffice)
5. **Review responses** daily during enrollment period
6. **Use filters** to find specific students or status
7. **Print contracts** for physical signatures as needed
8. **Keep the manual** (SSM 5.1 and 5.2) accessible for reference

---

## Manual References

All materials reference:
- **SSM 5.1 Evaluation of Students Application for Residence Hall Accommodation V2_Rev0** — Sections 3.3 (Evaluation for Admission), 4.0 (Procedures), 5.0 (List of Forms and Reports)
- **SSM 5.2 Residence Hall Accommodation V2_Rev0** — Sections 4.2 (Monitoring Health and Safety), 4.3 (Maintenance of Properties), 5.0 (List of Forms and Reports)

---

## Assessment and Follow-up

### Immediate Assessment

The audience practice serves as the immediate practical assessment. Participants who complete all tasks successfully have demonstrated competency.

### 60-Day Follow-Up (Per FAM 4.7 Section 4.6)

Two months after training, the RHU Head should assess:

1. **Application on the Job:** Are staff using digital tools in daily operations?
2. **Efficiency Gains:** Has the time to process applications decreased?
3. **Error Reduction:** Have errors in tracking decreased?
4. **Challenges Encountered:** What difficulties are staff facing?
5. **Additional Training Needed:** What topics need reinforcement?

### Recommended Next Steps

1. **Implement digital application form** for next enrollment period
2. **Set up resident tracker** with all current residents
3. **Create contract templates** and use them for new residents
4. **Digitize good housekeeping checklist** and conduct inspections
5. **Implement leave pass tracking** system
6. **Schedule RHU-2** (if needed) for advanced topics

---

## Pre-Training Setup Recommendations

Before the first RHU-1 session:

1. **Create a shared Google Drive folder** for all RHU training materials
2. **Prepare sample application data** for practice
3. **Set up the leaderboard** in Google Sheets with read-only access
4. **Set up a "RHU Help" channel** in Google Chat for ongoing questions
5. **Record the pre-session video** (10-15 minutes)
6. **Host the video on Google Drive** and share the link 48 hours before the session
7. **Print quick reference cards** (one per participant)
8. **Test the training room setup** (projector, internet, participant computers)

---

## Video Production Tips

For the pre-session video:

1. **Use a screen recording tool** like Loom, OBS, or Google Meet recording
2. **Keep the video under 15 minutes** to maintain engagement
3. **Add captions** for accessibility
4. **Host on Google Drive** and share the link 48 hours before the session
5. **Test the video** on multiple devices before distribution
6. **Emphasize the SSM references** throughout

---

## Follow-Up Support

After the session:

1. **Schedule a 15-minute check-in** 1 week later to address issues
2. **Create a shared "RHU Help" channel** in Google Chat for ongoing questions
3. **Appoint "digital champions"** in RHU who can help colleagues
4. **Collect feedback** on the training materials for continuous improvement

---

## References

- **SSM 5.1 Evaluation of Students Application for Residence Hall Accommodation V2_Rev0**
- **SSM 5.2 Residence Hall Accommodation V2_Rev0**
- **Google Forms Help Center** — forms.google.com/support
- **Google Sheets Help Center** — sheets.google.com/support
- **Google Docs Help Center** — docs.google.com/support
- **LibreOffice Documentation** — help.libreoffice.org

---

## Trainer Notes

- **Pace:** Adjust timing based on participant comfort level. If participants are struggling with a particular tool, spend more time on it.
- **Analogies:** Emphasize the physical logbook → digital logbook analogy throughout.
- **Real Examples:** Use actual RHU scenarios and data to make the training more relevant.
- **Manual References:** Frequently reference SSM 5.1 and 5.2 to show compliance.
- **Follow-up:** Schedule a check-in with the RHU Head 2 weeks after training to address any issues.

---

**End of RHU-1 Trainer Guide**
