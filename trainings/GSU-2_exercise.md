# GSU-2 Hands-On Exercise: Facility Use Management and Performance Evaluation

**Duration:** 8 minutes
**Format:** Guided step-by-step exercise
**Prerequisites:** Watched pre-session video, Session 0 completed

---

## Exercise Scenario

You are a GSU staff member responsible for managing facility bookings and performance evaluations. Your task is to practice creating digital tools for facility management using Google Workspace.

---

## Step-by-Step Instructions

### Part 1: Create a Shared Calendar (2 minutes)

#### Task 1: Create the Calendar

1. Open your web browser and go to `calendar.google.com`
2. On the left, click **+** next to "Other calendars" → **Create new calendar**
3. Name the calendar: `Practice_Booking`
4. Add a description: "Practice calendar for facility booking"
5. Set time zone: `Asia/Manila`
6. Click **Create calendar**

4. Share the calendar:
   - Hover over the calendar name → Click the three dots → **Settings and sharing**
   - Under **Share with specific people**, enter a colleague's email address
   - Set permission level: **Make changes and manage sharing**
   - Click **Send**

5. Create a test event:
   - Click on today's date at 9:00 AM
   - Title: `Practice Booking`
   - Description: `Test event for practice`
   - Click **Save**

**Expected Outcome:** You have a shared calendar with a test event.

[SCREENSHOT: Google Calendar with test event]

---

### Part 2: Create a Simple Permit Form (2 minutes)

#### Task 2: Create the Form

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Practice_Permit`

4. Add 3 questions:
   - Question 1: Name of Requestor (Short answer)
   - Question 2: Date of Use (Date)
   - Question 3: Purpose of Use (Paragraph)

5. Click **Responses** tab → Click **Link to Sheets**
6. Create a new spreadsheet: `Practice_Permit_Responses`
7. Click **Create**

8. Submit a test response:
   - Go back to the form
   - Fill in: Juan dela Cruz, 4/16/2026, Staff Meeting
   - Click **Submit**

9. View the response spreadsheet to verify data was collected

**Expected Outcome:** You have a permit form with 3 questions and responses collected.

[SCREENSHOT: Permit form and response spreadsheet]

---

### Part 3: Create an Evaluation Sheet (2 minutes)

#### Task 3: Create the Spreadsheet

1. Go to `drive.google.com`
2. Click **+ New** → **Google Sheets`
3. Name the sheet: `Practice_Evaluation`

4. Set up column headers in row 1:
   - Cell A1: `Name`
   - Cell B1: `Score 1`
   - Cell C1: `Score 2`
   - Cell D1: `Score 3`
   - Cell E1: `Total`
   - Cell F1: `Rating`

5. Format the header row:
   - Select row 1 → Click **Bold** → Add a background color

6. Add formulas:
   - In cell E2 (Total): `=SUM(B2:D2)`
   - In cell F2 (Rating): `=IF(E2>=27, "Excellent", IF(E2>=18, "Good", "Fair"))`

7. Add conditional formatting:
   - Select column F
   - Click **Format** → **Conditional formatting**
   - Add rules:
     - If Rating = "Excellent": Green background
     - If Rating = "Good": Yellow background
     - If Rating = "Fair": Orange background

8. Enter 1 sample evaluation:
   - Row 2: Juan dela Cruz, 10, 9, 8
   - Observe how Total and Rating calculate automatically

**Expected Outcome:** You have an evaluation sheet with formulas and conditional formatting.

[SCREENSHOT: Evaluation sheet with sample data]

---

### Part 4: Create a Checklist (2 minutes)

#### Task 4: Create the Checklist Form

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Practice_Checklist`

4. Add 3 checklist items:
   - Question 1: Task 1 completed? (Checkbox: Yes, No)
   - Question 2: Task 2 completed? (Checkbox: Yes, No)
   - Question 3: Task 3 completed? (Checkbox: Yes, No)

5. Click **Responses** tab → Click **Link to Sheets**
6. Create a new spreadsheet: `Practice_Checklist_Responses`
7. Click **Create**

8. Submit a test response:
   - Go back to the form
   - Fill in: Yes, Yes, No
   - Click **Submit**

9. View the response spreadsheet to verify data was collected

**Expected Outcome:** You have a checklist form with 3 items and responses collected.

[SCREENSHOT: Checklist form and response spreadsheet]

---

## Self-Check Answers

After completing the exercise, verify your work against these expected results:

### Question 1: Did you create a shared calendar?
**Answer:** Yes, if you have a calendar named "Practice_Booking" shared with a colleague.

### Question 2: Did you create a permit form with at least 3 questions?
**Answer:** Yes, if you have a Google Form with Name, Date, and Purpose questions.

### Question 3: Did you create an evaluation sheet with formulas?
**Answer:** Yes, if you have a spreadsheet with SUM and IF formulas working.

### Question 4: Did you add conditional formatting to the rating?
**Answer:** Yes, if ratings show in different colors (green, yellow, orange).

### Question 5: Did you create a checklist form?
**Answer:** Yes, if you have a Google Form with 3 checklist items.

### Question 6: Did you submit test responses to all forms?
**Answer:** Yes, if responses appear in the linked spreadsheets.

---

## Challenge Variations

### Basic Challenge (Completed Above)
- Create a shared calendar
- Create a permit form
- Create an evaluation sheet
- Create a checklist form

### Intermediate Challenge (If You Finish Early)
- Add more questions to the permit form (equipment needed, approval sections)
- Create a vehicle booking calendar
- Add more evaluation criteria to the sheet
- Create a security guard evaluation form

### Advanced Challenge (For Extra Practice)
- Set up event color coding in the calendar
- Create a dashboard showing booking statistics
- Add formulas to calculate average scores across multiple evaluations
- Create a cleaning checklist with conditional logic
- Design a permit approval workflow

---

## Troubleshooting

If you encounter issues, check these common problems:

| Problem | Solution |
|---------|----------|
| Calendar not visible to others | Check sharing permissions. Ensure correct email address. |
| Form responses not appearing | Check that form is linked to a spreadsheet. Verify you submitted. |
| Formula shows error | Check that referenced cells contain numbers. Verify formula syntax. |
| Conditional formatting not working | Verify formula syntax and that it's applied to the correct range. |
| Can't find uploaded files | Check the folder you created or search by filename. |
| Rating formula not working | Check IF statement syntax. Ensure parentheses are balanced. |

---

## FAM References

Remember these key references from the manuals:

**FAM 6.2 Use of Vehicle, Facilities and Equipment:**
- Section 4.1: Use of Facilities/Equipment (Permit to Use School Facilities)
- Section 4.2: Use of Motor Vehicle (Permit to Use School Vehicle, Driver's Trip Ticket)
- Section 5.1: Forms (Permit to Use School Facilities, Permit to Use School Vehicle)

**FAM 6.3 Janitorial Services:**
- Section 3.1: Cleaning Assignment and Schedule
- Section 4.0: Procedures (Cleaning Checklist, Performance Evaluation)
- Section 5.1: Forms (Cleaning Checklist, Janitorial Performance Evaluation)

**FAM 6.6 Security Services:**
- Section 3.1: Security and Safety Plan
- Section 4.0: Procedures (Security Guard Detailing Schedule, Performance Evaluation)
- Section 5.1: Forms (Security Guard Work Performance Evaluation)

---

## Next Steps

After completing this exercise:
1. Share your files with the trainer for verification
2. Ask any questions you have
3. Prepare for additional GSU training sessions
4. Take your quick reference card for future reference

---

## Keyboard Shortcuts for Google Calendar

| Action | Windows | Mac |
|--------|---------|-----|
| Create event | `C` | `C` |
| Go to today | `T` | `T` |
| Go to day view | `D` | `D` |
| Go to week view | `W` | `W` |
| Go to month view | `M` | `M` |
| Search | `/` | `/` |

---

## Keyboard Shortcuts for Google Sheets

| Action | Windows | Mac |
|--------|---------|-----|
| New row | `Alt + I`, then `R` | `Ctrl + Option + I`, then `R` |
| Bold | `Ctrl + B` | `Cmd + B` |
| Italic | `Ctrl + I` | `Cmd + I` |
| Insert formula | `=` | `=` |
| Fill down | `Ctrl + D` | `Cmd + D` |

---

**End of GSU-2 Hands-On Exercise**
