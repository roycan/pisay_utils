# GSU-2 Trainer Guide: Facility Use Management and Performance Evaluation

## Session Metadata

| Field | Value |
|-------|-------|
| **Unit** | General Services Unit (GSU) |
| **Session ID** | GSU-2 |
| **Session Title** | Facility Use Management and Performance Evaluation |
| **Duration** | 1 hour (60 minutes) |
| **Prerequisites** | Session 0 (Google Workspace Fundamentals), GSU-1 (recommended) |
| **Google Workspace Tools** | Google Calendar, Google Forms, Google Sheets |
| **LibreOffice Equivalent** | LibreOffice Calc (optional - to be deployed campus-wide) |
| **Manual Reference** | FAM 6.2 Use of Vehicle, Facilities and Equipment, FAM 6.3 Janitorial Services, FAM 6.6 Security Services |
| **Target Audience** | GSU staff, Property Custodian, Security Head, Janitorial Services Head |

## Time Allocation Breakdown

| Component | Time | Notes |
|-----------|------|-------|
| **Pre-Session Video** (asynchronous) | 10-15 min | Sent 2-3 days before session |
| **In-Person Session** | 60 min | |
| ├─ Welcome and Q&A on Video | 3 min | Address questions from pre-session video |
| ├─ Shared Google Calendars for Booking | 12 min | Facility and vehicle booking |
| ├─ Digital Permit Forms | 12 min | Google Forms for permits |
| ├─ Performance Evaluation Scoring | 12 min | Automatic calculations in Sheets |
| ├─ Cleaning Checklist | 8 min | Digital form for inspections |
| ├─ Audience Practice | 8 min | Guided hands-on exercise |
| └─ Wrap-up & Scoring | 5 min | Review, answer key, leaderboard update |

## Learning Objectives

By the end of this session, participants will be able to:

1. Create and manage shared Google Calendars for facility and vehicle booking per FAM 6.2
2. Create digital permit forms using Google Forms (facilities and vehicles)
3. Build performance evaluation spreadsheets with automatic scoring in Google Sheets
4. Digitize the cleaning checklist using Google Forms per FAM 6.3
5. Create security guard evaluation forms per FAM 6.6
6. Use formulas to calculate total scores and averages
7. Organize GSU documents in Google Drive with proper folder structure

## Materials Needed

- Computers/laptops with internet access
- Access to PSHS Google Workspace domain
- Sample facility and vehicle data for practice
- Printed quick reference cards (one per participant)
- Projector for demonstration
- Whiteboard or digital equivalent

## Pre-Session Video Content Summary

The pre-session video (10-15 minutes) covers:
1. **Analogy** (30 sec): Wall calendar → Google Calendar
2. **Keywords & Concepts** (2 min): Shared calendars, event booking, automatic scoring, formulas, digital forms
3. **Pattern Demonstration** (8-10 min): Building calendars, permits, evaluations
4. **Quick Check Question** (30 sec): "What Google Workspace tool would you use to create a shared calendar for facility booking?"

---

## In-Person Session Script

### 1. Welcome and Quick Q&A (3 minutes)

**Trainer Script:**

"Good morning/afternoon, everyone! Welcome to GSU-2: Facility Use Management and Performance Evaluation.

This session will transform how GSU manages facility bookings, vehicle requests, and performance evaluations using Google Workspace. We'll create shared calendars, digital permit forms, and automated evaluation systems.

Before we dive in, let's address any questions you might have from the pre-session video."

**Anticipated Questions & Answers:**

| Question | Answer |
|----------|--------|
| "Why do we need a shared calendar?" | A shared calendar allows everyone to see facility and vehicle availability in real-time. It prevents double-booking and makes scheduling more efficient per FAM 6.2. |
| "Can we still use paper permits?" | Yes, you can collect data on paper and enter it into the digital system. The digital system enhances, not replaces, existing processes. |
| "How do we calculate scores automatically?" | Google Sheets has powerful formula functions. We'll use SUM, AVERAGE, and other functions to calculate total scores automatically. |
| "What about security of booking data?" | This is critical. Share calendars and forms only with authorized staff. Use Google Drive permissions to control access. |

**Trainer Script:**

"Great questions! Remember, the goal is to make GSU operations more efficient while maintaining compliance with FAM 6.2, 6.3, and 6.6. Let's move to our first topic."

---

### 2. Shared Google Calendars for Booking (12 minutes)

**Trainer Script:**

"Per FAM 6.2, we need to ensure proper scheduling of facilities and vehicles. Let's create shared Google Calendars for booking."

#### Step-by-Step Demo Script

**Step 1: Create a Facility Calendar**

1. Go to `calendar.google.com`
2. On the left, click **+** next to "Other calendars" → **Create new calendar**
3. Name the calendar: `Facility Booking - PSHS-MC`
4. Add description: "Shared calendar for booking school facilities per FAM 6.2"
5. Set time zone: `Asia/Manila`
6. Click **Create calendar**

**Step 2: Share the Calendar**

[SCREEN: Sharing calendar settings]

**Trainer Script:**

"Now let's share the calendar with authorized staff.

1. Hover over the calendar name → Click the three dots → **Settings and sharing**
2. Under **Share with specific people**, enter email addresses of authorized staff
3. Set permission level: **Make changes and manage sharing** (for GSU staff)
4. Set permission level: **See all event details** (for requestors)
5. Click **Send**

**Step 3: Create a Vehicle Calendar**

1. Click **+** next to "Other calendars" → **Create new calendar**
2. Name the calendar: `Vehicle Booking - PSHS-MC`
3. Add description: "Shared calendar for booking school vehicles per FAM 6.2"
4. Set time zone: `Asia/Manila`
5. Click **Create calendar**
6. Share with authorized staff (same process as facility calendar)

**Step 4: Book a Facility**

[SCREEN: Creating a calendar event]

**Trainer Script:**

"Let's demonstrate how to book a facility.

1. Click on the date and time you want to book
2. Add event title: `Science Lab 1 - Grade 7 Class`
3. Add description with details:
   ```
   Requestor: Juan dela Cruz
   Purpose: Laboratory Activity
   Number of participants: 30
   Equipment needed: Microscopes, beakers
   ```
4. Add guests: Enter email addresses of relevant staff (optional)
5. Click **Save**
6. The event appears on the shared calendar for everyone to see"

**Step 5: Book a Vehicle**

1. Click on the date and time you want to book
2. Add event title: `School Van - Field Trip`
3. Add description with details:
   ```
   Requestor: Maria Santos
   Destination: National Museum
   Purpose: Educational Tour
   Number of passengers: 15
   Driver: Pedro Reyes
   ```
4. Click **Save**
5. The event appears on the vehicle calendar

---

### 3. Digital Permit Forms (12 minutes)

**Trainer Script:**

"Per FAM 6.2, we need permits for using school facilities and vehicles. Let's create digital permit forms using Google Forms."

#### Step-by-Step Demo Script

**Step 1: Create Facility Permit Form**

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Permit to Use School Facilities`

**Step 2: Add Questions**

[SCREEN: Creating form questions]

**Trainer Script:**

"Let's add the necessary questions per FAM 6.2.

**Section 1: Requestor Information**
- Title: Requestor Information
- Question 1: Name of Requestor (Short answer)
- Question 2: Department/Unit (Dropdown: Academic, Admin, Student Services, etc.)
- Question 3: Email Address (Short answer)
- Question 4: Contact Number (Short answer)

**Section 2: Facility Details**
- Title: Facility Details
- Question 5: Facility to be Used (Dropdown: Science Lab 1, Science Lab 2, Auditorium, Gym, Classroom, etc.)
- Question 6: Date of Use (Date)
- Question 7: Time Start (Time)
- Question 8: Time End (Time)
- Question 9: Purpose of Use (Paragraph)

**Section 3: Equipment Needed**
- Title: Equipment Needed
- Question 10: Equipment Required (Checkboxes: Projector, Microphone, Tables, Chairs, Laboratory Equipment, Other)
- Question 11: If Other, please specify (Paragraph - conditional on Other)

**Section 4: Approval**
- Title: Approval
- Question 12: Division Chief Recommendation (Dropdown: Approved, Disapproved)
- Question 13: Comments (Paragraph)
- Question 14: FAD Chief Approval (Dropdown: Approved, Disapproved)
- Question 15: Final Approval Status (Dropdown: Approved, Disapproved, Pending)"

**Step 3: Configure and Share**

1. Click **Settings** → Enable "Collect email addresses"
2. Click **Responses** → Link to a Google Sheet
3. Name the spreadsheet: `Facility_Permit_Responses`
4. Click **Send** → Copy the link
5. Share with staff for submitting requests

**Step 4: Create Vehicle Permit Form**

1. Create a new Google Form: `Permit to Use School Vehicle`
2. Add similar questions for vehicle requests:
   - Requestor Information
   - Vehicle Details (Vehicle Type, Date, Time, Destination, Purpose)
   - Passenger Information (Number of passengers, Names)
   - Driver Information (Driver name, License number)
   - Approval sections

**Step 5: Configure and Share**

1. Link to a Google Sheet: `Vehicle_Permit_Responses`
2. Share the link with staff

---

### 4. Performance Evaluation Scoring (12 minutes)

**Trainer Script:**

"Per FAM 6.3 and 6.6, we need to evaluate janitorial and security performance. Let's create evaluation spreadsheets with automatic scoring."

#### Step-by-Step Demo Script

**Step 1: Create Janitorial Evaluation Spreadsheet**

1. Go to `drive.google.com`
2. Click **+ New** → **Google Sheets**
3. Name the sheet: `Janitorial_Performance_Evaluation_2026`

**Step 2: Set Up the Evaluation Form**

[SCREEN: Typing evaluation criteria]

**Trainer Script:**

"Let's set up the evaluation criteria per FAM 6.3.

Row 1 headers:
- A: Employee Name
- B: Date of Evaluation
- C: Evaluator
- D: Attendance (5 points)
- E: Punctuality (5 points)
- F: Quality of Work (20 points)
- G: Completeness of Tasks (15 points)
- H: Compliance with Schedule (15 points)
- I: Attitude/Cooperation (15 points)
- J: Safety Practices (10 points)
- K: Equipment Care (5 points)
- L: Total Score
- M: Rating
- N: Comments

**Step 3: Add Scoring Formula**

[SCREEN: Adding scoring formula]

**Trainer Script:**

"Let's add a formula to calculate the total score automatically.

In cell L2, enter:
```
=SUM(D2:K2)
```
This sums up all the scores from columns D through K.

In cell M2, enter:
```
=IF(L2>=90, "Outstanding", IF(L2>=80, "Very Satisfactory", IF(L2>=70, "Satisfactory", IF(L2>=60, "Fair", "Poor"))))
```
This assigns a rating based on the total score."

**Step 4: Add Conditional Formatting**

1. Select column M (Rating)
2. Click **Format** → **Conditional formatting**
3. Add rules:
   - If Rating = "Outstanding": Green background
   - If Rating = "Very Satisfactory": Light green background
   - If Rating = "Satisfactory": Yellow background
   - If Rating = "Fair": Orange background
   - If Rating = "Poor": Red background

**Step 5: Create Security Guard Evaluation Spreadsheet**

1. Create a new Google Sheet: `Security_Guard_Performance_Evaluation_2026`
2. Set up similar headers with security-specific criteria:
   - Attendance, Punctuality, Post Security, Access Control, Incident Response, Report Writing, Uniform/Equipment, Professional Conduct
3. Add scoring formula and conditional formatting

---

### 5. Cleaning Checklist (8 minutes)

**Trainer Script:**

"Per FAM 6.3, we need a cleaning checklist. Let's digitize it using Google Forms."

#### Step-by-Step Demo Script

**Step 1: Create the Checklist Form**

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Cleaning_Checklist`

**Step 2: Add Questions**

[SCREEN: Creating checklist questions]

**Trainer Script:**

"Let's add the cleaning checklist questions.

**Section 1: Area Information**
- Title: Area Information
- Question 1: Area Being Cleaned (Dropdown: Corridor, Restroom, Classroom, Office, Laboratory, Gym, Auditorium)
- Question 2: Date of Cleaning (Date)
- Question 3: Janitor Name (Short answer)

**Section 2: Cleaning Tasks**
- Title: Cleaning Tasks
- Question 4: Floor swept and mopped (Checkbox: Completed, Not Completed)
- Question 5: Surfaces dusted and wiped (Checkbox: Completed, Not Completed)
- Question 6: Trash bins emptied (Checkbox: Completed, Not Completed)
- Question 7: Restrooms sanitized (Checkbox: Completed, Not Completed)
- Question 8: Windows cleaned (Checkbox: Completed, Not Completed)
- Question 9: Mirrors polished (Checkbox: Completed, Not Completed)

**Section 3: Supplies Used**
- Title: Supplies Used
- Question 10: Cleaning supplies used (Checkboxes: Broom, Mop, Disinfectant, Glass Cleaner, Trash Bags, Other)
- Question 11: If Other, please specify (Paragraph - conditional on Other)

**Section 4: Overall Assessment**
- Title: Overall Assessment
- Question 12: Overall Cleanliness (Dropdown: Excellent, Good, Fair, Poor)
- Question 13: Comments/Issues (Paragraph)

**Step 3: Configure and Share**

1. Click **Responses** → Link to a Google Sheet
2. Name the spreadsheet: `Cleaning_Checklist_Responses`
3. Share the link with janitorial staff

---

### 6. Audience Practice: Guided Exercise (8 minutes)

**Trainer Script:**

"Now it's your turn! I'll guide you through a quick exercise. Follow along with me."

#### Exercise Steps

**Step 1: Create a Shared Calendar (2 minutes)**
1. Go to `calendar.google.com`
2. Create a new calendar named `Practice_Booking`
3. Share it with a colleague
4. Create a test event

**Step 2: Create a Simple Permit Form (2 minutes)**
1. Go to `forms.google.com`
2. Create a new form named `Practice_Permit`
3. Add 3 questions: Name, Date, Purpose
4. Submit a test response
5. View the response spreadsheet

**Step 3: Create an Evaluation Sheet (2 minutes)**
1. Create a new Google Sheet named `Practice_Evaluation`
2. Add headers: Name, Score 1, Score 2, Score 3, Total, Rating
3. Add a formula to calculate Total (SUM)
4. Add a formula to calculate Rating (IF statement)
5. Enter 1 sample evaluation

**Step 4: Create a Checklist (2 minutes)**
1. Create a new Google Form named `Practice_Checklist`
2. Add 3 checklist items with Completed/Not Completed options
3. Submit a test response
4. View the response spreadsheet

**Trainer Circulation:**

While participants work, circulate to:
- Check that calendars are shared correctly
- Ensure forms are collecting responses
- Verify formulas are working
- Confirm checklists are functioning
- Answer individual questions
- Provide encouragement

---

### 7. Wrap-up, Answer Key, and Scoring (5 minutes)

#### Answer Key

**Expected Outputs:**
- Shared calendar created and shared
- Permit form with 3 questions and responses collected
- Evaluation sheet with formulas working
- Checklist form with 3 items and responses collected

#### Scoring Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **Completion** | 40 pts | All 4 tasks completed |
| **Accuracy** | 40 pts | Tools used correctly |
| **Independence** | 20 pts | Completed without asking for help |
| **Total** | 100 pts | |

#### Leaderboard Update

**Trainer Script:**

"Let's update our leaderboard! I'll record each unit's scores based on how many participants completed the exercise successfully."

| Unit | Participants | Completed | Average Score | Total Points |
|------|--------------|-----------|---------------|--------------|
| GSU | ___ | ___ | ___ | ___ |
| ... | ... | ... | ... | ... |

*(Fill in during actual training)*

---

## Troubleshooting Tips

### Common Mistakes and Solutions

| Mistake | Solution |
|---------|----------|
| Calendar not visible to others | Check sharing permissions. Ensure calendar is shared with correct email addresses. |
| Form responses not appearing | Check that form is linked to a spreadsheet. Verify you submitted the form. |
| Formula shows #VALUE! error | Check that referenced cells contain numbers, not text. |
| Conditional formatting not working | Verify formula syntax and that it's applied to the correct range. |
| Can't find uploaded files | Check the folder you created or search by filename. |
| Rating formula not working | Check IF statement syntax. Ensure parentheses are balanced. |

### Tips for Success

1. **Use consistent naming** for all calendars, forms, and sheets
2. **Set up templates** at the start of each school year
3. **Train staff** on how to use shared calendars
4. **Update calendars daily** with bookings and cancellations
5. **Use formulas** to automate calculations and reduce errors
6. **Back up data regularly** (download as .ods for LibreOffice)
7. **Protect sensitive data** — share only with authorized staff
8. **Follow FAM procedures** for permits and evaluations

---

## Manual References

All materials reference:
- **FAM 6.2 Use of Vehicle, Facilities and Equipment V2_Rev1** — Sections 4.1 (Facilities), 4.2 (Vehicles), 5.0 (Forms and Reports)
- **FAM 6.3 Janitorial Services V2_Rev0** — Sections 3.1 (Cleaning Schedule), 4.0 (Procedures), 5.0 (Forms and Reports)
- **FAM 6.6 Security Services V2_Rev0** — Sections 3.1 (Security Plan), 4.0 (Procedures), 5.0 (Forms and Reports)

---

## Assessment and Follow-up

### Immediate Assessment

The audience practice serves as the immediate practical assessment. Participants who complete all tasks successfully have demonstrated competency.

### 60-Day Follow-Up (Per FAM 4.7 Section 4.6)

Two months after training, the GSU Head should assess:

1. **Application on the Job:** Are staff using digital tools for facility booking and evaluations?
2. **Efficiency Gains:** Has the time to process permits decreased?
3. **Error Reduction:** Have errors in scheduling decreased?
4. **Challenges Encountered:** What difficulties are staff facing?
5. **Additional Training Needed:** What topics need reinforcement?

### Recommended Next Steps

1. **Implement shared calendars** for facility and vehicle booking
2. **Create digital permit forms** and use them for all requests
3. **Set up evaluation spreadsheets** with automatic scoring
4. **Digitize cleaning checklist** and use it for inspections
5. **Schedule GSU-1** (if not yet completed) for additional training

---

## Pre-Training Setup Recommendations

Before the first GSU-2 session:

1. **Create a shared Google Drive folder** for all GSU training materials
2. **Prepare sample facility and vehicle data** for practice
3. **Set up the leaderboard** in Google Sheets with read-only access
4. **Set up a "GSU Help" channel** in Google Chat for ongoing questions
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
6. **Emphasize the FAM references** throughout

---

## Follow-Up Support

After the session:

1. **Schedule a 15-minute check-in** 1 week later to address issues
2. **Create a shared "GSU Help" channel** in Google Chat for ongoing questions
3. **Appoint "digital champions"** in GSU who can help colleagues
4. **Collect feedback** on the training materials for continuous improvement

---

## References

- **FAM 6.2 Use of Vehicle, Facilities and Equipment V2_Rev1**
- **FAM 6.3 Janitorial Services V2_Rev0**
- **FAM 6.6 Security Services V2_Rev0**
- **Google Calendar Help Center** — calendar.google.com/support
- **Google Sheets Help Center** — sheets.google.com/support
- **Google Forms Help Center** — forms.google.com/support
- **LibreOffice Documentation** — help.libreoffice.org

---

## Trainer Notes

- **Pace:** Adjust timing based on participant comfort level. If participants are struggling with formulas, spend more time on them.
- **Analogies:** Emphasize the wall calendar → Google Calendar analogy throughout.
- **Real Examples:** Use actual GSU scenarios and data to make the training more relevant.
- **Manual References:** Frequently reference FAM 6.2, 6.3, and 6.6 to show compliance.
- **Follow-up:** Schedule a check-in with the GSU Head 2 weeks after training to address any issues.

---

**End of GSU-2 Trainer Guide**
