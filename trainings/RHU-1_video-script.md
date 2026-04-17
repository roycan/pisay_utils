# RHU-1 Video Script: Residence Hall Administration and Monitoring

**Duration:** 10-15 minutes
**Format:** Pre-recorded video for participants to watch before the in-person session
**Target Audience:** RHU staff, Residence Hall Head, Residence Hall Attendants

---

## Opening: Analogy (30 seconds)

[SCREEN: Split screen showing a physical logbook on the left, Google Sheets on the right]

**Narrator:**

"Imagine you've been using a physical logbook to track residence hall applications, room assignments, and leave passes. It works—but there are problems. Only one person can write at a time. Searching for a specific student's record means flipping through pages. And if the logbook gets lost or damaged, all that data is gone.

Now imagine that same logbook, but digital. Multiple staff can access it simultaneously. You can search for any student in seconds. Data is automatically backed up in the cloud. That's what we're going to build today—a digital residence hall management system using Google Workspace."

[SCREEN: Title slide: "RHU-1: Residence Hall Administration and Monitoring"]

---

## Keywords and Concepts (2 minutes)

[SCREEN: Bulleted list of keywords appears one by one as narrator speaks]

**Narrator:**

"Before we dive in, let's cover some key terms you'll need to know.

**First: Digital Forms.** Instead of paper forms that students fill out by hand, we'll use Google Forms. Students can submit applications online, and all responses are automatically collected in a spreadsheet. No more manual data entry.

**Second: Timestamp Tracking.** For leave passes, we need to know exactly when a student leaves and returns. Google Sheets can automatically record timestamps, making it easy to track duration and ensure students return on time.

**Third: Conditional Formatting.** This automatically changes cell colors based on rules. We'll use it to highlight pending contracts in yellow, active residents in green, and terminated contracts in red. This gives you instant visual status.

**Fourth: Data Validation.** This ensures data is entered correctly. For example, we can create a dropdown list for contract status so there's no confusion between different statuses.

**Fifth: Templates.** Instead of typing the same contract for every student, we'll create templates in Google Docs. When a new student is approved, we simply fill in their details and print."

[SCREEN: Visual examples of each concept appear as they're mentioned]

---

## Pattern Demonstration (8-10 minutes)

### Digital Residence Hall Application (2.5 minutes)

[SCREEN: Screen recording of creating a Google Form]

**Narrator:**

"Let's start with the Residence Hall Application Form. Go to forms.google.com and click Blank. Name it 'Residence Hall Application Form.'

Now let's add the questions. Per SSM 5.1, we need to collect student information for evaluation.

Add a section for Student Information: Full Name, Student ID, Grade Level, Scholarship Category, and Gender.

Add a section for Contact Information: Home Address, Distance from Campus, Parent/Guardian Name, and Contact Details.

Add a section for Health Information: Medical conditions and emergency contacts.

Finally, add an Agreement section where students acknowledge they understand accommodation is subject to availability and agree to comply with residence hall rules.

[SCREEN: Configuring form settings]

**Narrator:**

"Click Settings and enable 'Collect email addresses' to track who submitted. Under Responses, you can link to a Google Sheet where all responses will be automatically collected.

Click Send, copy the link, and share it with the Registrar for distribution during enrollment. All applications are now collected in one place, making evaluation per SSM 5.1 Section 3.3.2 much easier."

### Resident Management Tracker (2.5 minutes)

[SCREEN: Screen recording of creating a Google Sheet]

**Narrator:**

"Now let's create a resident management tracker. Go to drive.google.com, click New, and select Google Sheets. Name it 'RHU_Resident_Tracker_2026-2027.'

Set up column headers: Student Name, Student ID, Grade Level, Gender, Room Assignment, Bed Number, Contract Status, Contract Date, Appliances Declared, Fee Status, and Contact Information.

[SCREEN: Adding data validation and conditional formatting]

**Narrator:**

"Let's add data validation for Contract Status. Select the column, go to Data, Data validation, and choose Dropdown. Add options: Pending, Signed, Active, and Terminated.

Now let's add conditional formatting. Select all columns, go to Format, Conditional formatting. Add a rule: if Contract Status equals 'Pending,' show yellow background. Add another rule: if 'Active,' show green background. And if 'Terminated,' show red background.

At the bottom, add summary formulas to count total residents, active contracts, pending contracts, and students with appliances. This gives you a quick overview of residence hall occupancy."

### Contract Templates (1.5 minutes)

[SCREEN: Screen recording of creating a Google Doc template]

**Narrator:**

"Per SSM 5.1, the Residence Hall Head distributes contracts to qualified interns. Let's create a template in Google Docs.

Create a new Google Doc and name it 'Residence_Hall_Contract_Template.' Type the contract with placeholders for student name, ID, grade level, and fees. These placeholders will be replaced with actual data when generating individual contracts.

Create similar templates for the Parent/Guardian Waiver and the Appliance Declaration Form.

These templates can be printed for physical signatures. As PSHS adopts digital signatures in the future, we can transition to fully digital contracts."

### Good Housekeeping Checklist (1.5 minutes)

[SCREEN: Screen recording of creating a checklist form]

**Narrator:**

"Per SSM 5.2 Section 4.3.1, the Residence Hall Head inspects rooms using a Good Housekeeping Checklist. Let's digitize this.

Create a new Google Form named 'Good_Housekeeping_Checklist.' Add sections for Room Information, Cleanliness, Safety and Security, and Overall Assessment.

For each checklist item, use a checkbox question with options: Passed or Needs Improvement.

Link the form to a Google Sheet to collect all inspection data. Add conditional formatting to highlight 'Needs Improvement' items in red. This makes it easy to identify rooms that need follow-up."

### Leave Pass Tracking (2 minutes)

[SCREEN: Screen recording of creating a leave pass tracker]

**Narrator:**

"Finally, per SSM 5.2 Section 4.2.1, let's create a leave pass tracking system.

Create a new Google Sheet named 'Leave_Pass_Tracker.' Set up columns: Student Name, Student ID, Date of Leave, Time Out, Destination, Purpose, Parent Notified, Approved By, Date of Return, Time In, Duration, Status, and Notes.

Add a formula in the Duration column to automatically calculate hours between time out and time in. Add a formula in the Status column to show whether the student is 'On Leave' or 'Returned.'

Add conditional formatting: yellow for 'On Leave,' green for 'Returned,' and orange for overnight stays (duration over 24 hours).

You can also create a Google Form for students to submit leave pass requests, which streamlines the process per SSM 5.2."

---

## Quick Check Question (30 seconds)

[SCREEN: Question on screen with multiple choice options]

**Narrator:**

"Before we wrap up, here's a quick check to test your understanding:

**Question:** What Google Workspace tool would you use to create a digital Residence Hall Application Form?

A) Google Docs
B) Google Sheets
C) Google Forms
D) Google Slides

[SCREEN: Pause for 5 seconds]

**Narrator:**

"The correct answer is C! Google Forms is designed for collecting data and is perfect for applications, surveys, and checklists. The responses automatically populate in a Google Sheet for easy management.

If you got this right, great job! If not, don't worry—we'll practice this in the in-person session."

---

## Closing (30 seconds)

[SCREEN: Summary of what was covered]

**Narrator:**

"In this video, you learned about:

- Creating a digital Residence Hall Application Form using Google Forms
- Building a resident management tracker in Google Sheets
- Creating contract templates in Google Docs
- Digitizing the Good Housekeeping Checklist
- Tracking leave passes with automatic timestamps

[SCREEN: Next steps]

**Narrator:**

"In our in-person session, we'll practice all of this hands-on, and you'll complete exercises to test your skills. Bring your questions, and get ready to transform how RHU manages residence hall operations!

See you there!"

[SCREEN: PSHS logo and "Thank you for watching"]

---

## Production Notes for Video Recording

### Technical Requirements
- **Resolution:** 1920x1080 (1080p) minimum
- **Audio:** Clear narration, no background noise
- **Screen Recording:** Use zoom-in features for small text and buttons
- **Pacing:** Speak clearly and at a moderate pace; allow pauses for viewers to process information

### Visual Style
- **Color Scheme:** Use PSHS branding colors where appropriate
- **Font:** Clean, readable sans-serif (Arial, Roboto, or similar)
- **Transitions:** Simple cuts or fades; avoid flashy transitions
- **Annotations:** Use arrows, circles, or highlights to draw attention to specific elements

### Accessibility
- **Captions:** Include closed captions for accessibility
- **Visual Cues:** Use visual indicators to reinforce concepts
- **Pacing:** Allow time for viewers to read on-screen text before moving on

### Distribution
- **Format:** MP4 or WebM
- **File Size:** Compress to under 500MB for easy sharing via email or Google Drive
- **Hosting:** Upload to Google Drive and share link 2-3 days before the in-person session
- **Deadline:** Ensure video is available to participants at least 48 hours before the session

---

## Important Notes for the Trainer

1. **Emphasize SSM Compliance:** Throughout the video, reference SSM 5.1 and 5.2 to show how digital tools comply with manual requirements.

2. **Use RHU-Specific Examples:** When demonstrating, use actual RHU scenarios (e.g., Grade 7 applications, room assignments, weekend leave passes).

3. **Mention Physical Signatures:** Clarify that for now, contracts are printed for physical signatures. Digital signatures may be adopted in the future.

4. **Highlight Benefits:** Emphasize efficiency gains—no more manual data entry, instant search, automatic backups.

5. **Keep It Practical:** Focus on tools that RHU staff will use daily. Don't get bogged down in advanced features.

---

**End of RHU-1 Video Script**
