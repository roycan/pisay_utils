# HSU-3 Hands-On Exercise: Infectious Disease Monitoring and Health Campaigns

**Duration:** 7 minutes
**Format:** Guided step-by-step exercise
**Prerequisites:** Watched pre-session video, Session 0 completed

---

## Exercise Scenario

You are an HSU staff member preparing for the upcoming flu season. Your task is to practice creating digital tools for disease monitoring and health campaigns using Google Workspace.

---

## Step-by-Step Instructions

### Part 1: Create a Disease Tracker (2 minutes)

#### Task 1: Create the Spreadsheet

1. Open your web browser and go to `drive.google.com`
2. Click **+ New** → **Google Sheets**
3. Name the sheet: `Practice_Disease_Tracker`

4. Set up column headers in row 1:
   - Cell A1: `Date Reported`
   - Cell B1: `Student Name`
   - Cell C1: `Disease Type`
   - Cell D1: `Status`
   - Cell E1: `Notes`

5. Format the header row:
   - Select row 1 → Click **Bold** → Add a background color (light gray or light blue)

6. Add data validation for Disease Type:
   - Select column C
   - Click **Data** → **Data validation**
   - Choose **Dropdown**
   - Options: `Flu`, `Dengue`, `Chickenpox`, `Other`
   - Check **Show dropdown list in cell**
   - Click **Done**

7. Add data validation for Status:
   - Select column D
   - Click **Data** → **Data validation**
   - Choose **Dropdown**
   - Options: `Active`, `Recovered`, `Referred`
   - Check **Show dropdown list in cell**
   - Click **Done**

8. Add conditional formatting:
   - Select columns A through E
   - Click **Format** → **Conditional formatting**
   - Add rule:
     - Format cells if: **Custom formula is**
     - Formula: `=$D2="Active"`
     - Formatting: Red background
   - Click **Done**

9. Enter 2 sample cases:
   - Row 2: 4/16/2026, Juan dela Cruz, Flu, Active, Mild symptoms
   - Row 3: 4/15/2026, Maria Santos, Dengue, Recovered, Hospitalized for 3 days

**Expected Outcome:** You have a disease tracker with data validation and conditional formatting.

[SCREENSHOT: Disease tracker with 2 sample cases]

---

### Part 2: Create a Simple Chart (2 minutes)

#### Task 2: Create a Chart

1. Select your data (cells A1 through E3)
2. Click **Insert** → **Chart**
3. Choose **Column chart** (should be selected by default)
4. Customize the chart:
   - Chart title: `Disease Cases by Type`
   - Make sure data range is correct
5. Click **Insert**
6. Observe how the chart visualizes your data

**Expected Outcome:** You have a column chart showing disease cases by type.

[SCREENSHOT: Column chart showing disease data]

---

### Part 3: Create Campaign Slides (2 minutes)

#### Task 3: Create a Presentation

1. Go to `drive.google.com`
2. Click **+ New** → **Google Slides**
3. Name the presentation: `Practice_Health_Campaign`

4. Create Slide 1 (Title Slide):
   - Click in the title box and type: `Hand Washing Campaign`
   - Click in the subtitle box and type: `Stay Healthy, Stay Safe!`
   - Add a background color or image

5. Create Slide 2:
   - Click **Insert** → **Slide** (or press `Ctrl+M`)
   - Title: `Why Wash Your Hands?`
   - Content:
     ```
     Hand washing removes germs and prevents the spread of disease.
     
     When to wash:
     • Before eating
     • After using the restroom
     • After sneezing or coughing
     • After touching animals
     ```

6. Add visual elements:
   - Click **Insert** → **Image** → Upload a relevant image (or use a placeholder)
   - Add icons or shapes if desired
   - Use consistent colors and fonts

**Expected Outcome:** You have a 2-slide presentation on hand washing.

[SCREENSHOT: 2-slide presentation]

---

### Part 4: Create a Survey (1 minute)

#### Task 4: Create a Survey Form

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Practice_Health_Survey`

4. Add 3 questions:
   - Question 1: Grade Level (Dropdown: Grade 7, Grade 8, Grade 9, Grade 10, Grade 11, Grade 12)
   - Question 2: How often do you wash your hands? (Dropdown: Always, Usually, Sometimes, Rarely, Never)
   - Question 3: What would help you wash your hands more often? (Paragraph)

5. Click **Responses** tab → Click **Link to Sheets**
6. Create a new spreadsheet: `Practice_Survey_Responses`
7. Click **Create**

8. Submit a test response:
   - Go back to the form
   - Fill in: Grade 10, Usually, More reminders
   - Click **Submit**

9. View the response spreadsheet to verify data was collected

**Expected Outcome:** You have a survey form with 3 questions and responses collected in a spreadsheet.

[SCREENSHOT: Survey form and response spreadsheet]

---

## Self-Check Answers

After completing the exercise, verify your work against these expected results:

### Question 1: Did you create a disease tracker with data validation?
**Answer:** Yes, if you have a spreadsheet with dropdown menus for Disease Type and Status.

### Question 2: Did you add conditional formatting?
**Answer:** Yes, if Active cases show in red (or your chosen color).

### Question 3: Did you create a chart from your data?
**Answer:** Yes, if you have a visual chart showing disease cases.

### Question 4: Did you create a 2-slide presentation?
**Answer:** Yes, if you have a Google Slides presentation with a title slide and content slide.

### Question 5: Did you create a survey with at least 3 questions?
**Answer:** Yes, if you have a Google Form with 3 questions and responses collected.

---

## Challenge Variations

### Basic Challenge (Completed Above)
- Create a disease tracker
- Create a chart
- Create a 2-slide presentation
- Create a survey with 3 questions

### Intermediate Challenge (If You Finish Early)
- Add a pivot table to analyze disease data by type and status
- Add more slides to your presentation (symptoms, prevention, resources)
- Add more survey questions (knowledge assessment, behavior assessment)
- Create a summary slide in your presentation

### Advanced Challenge (For Extra Practice)
- Create a dashboard with multiple charts (cases by month, cases by grade level)
- Add formulas to calculate recovery rates
- Create a health campaign calendar in Google Sheets
- Design a survey with conditional logic (show different questions based on previous answers)
- Create a printable PDF version of your campaign materials

---

## Troubleshooting

If you encounter issues, check these common problems:

| Problem | Solution |
|---------|----------|
| Chart not displaying data | Check that you selected the correct data range. Ensure headers are in the first row. |
| Pivot table not showing data | Verify that you selected all columns including headers. Check that data is not empty. |
| Conditional formatting not working | Verify formula syntax and that it's applied to the correct range. |
| Survey responses not appearing | Check that form is linked to a spreadsheet. Verify you submitted the form. |
| Can't find uploaded files | Check the folder you created or search by filename. |
| Formula shows error | Check that referenced cells contain the correct data type (dates for date calculations). |
| Can't insert image in Slides | Check image format (JPG, PNG work best). Try a different image. |

---

## SSM References

Remember these key references from the manuals:

**SSM 6.7 Infectious Disease Monitoring:**
- Section 3.2: Diseases to monitor (Conjunctivitis, Exanthems, Parotitis, Dengue, Amoebiasis, Typhoid, Hepatitis A)
- Section 3.4: Students excused from classes until fully recovered
- Section 5.1.1: Infectious Disease Monitoring Tool

**SSM 6.5 Health Information Campaign:**
- Section 3.2: Campaign strategies (posters, brochures, videos, activities)
- Section 3.5: Bulletin Board for information campaign
- Section 4.0: Procedures for health information activities

---

## Next Steps

After completing this exercise:
1. Share your files with the trainer for verification
2. Ask any questions you have
3. Prepare for additional HSU training sessions
4. Take your quick reference card for future reference

---

## Keyboard Shortcuts for Google Sheets

| Action | Windows | Mac |
|--------|---------|-----|
| New row | `Alt + I`, then `R` | `Ctrl + Option + I`, then `R` |
| Bold | `Ctrl + B` | `Cmd + B` |
| Italic | `Ctrl + I` | `Cmd + I` |
| Insert chart | `Alt + I`, then `C` | `Ctrl + Option + I`, then `C` |
| Insert pivot table | `Alt + I`, then `P` | `Ctrl + Option + I`, then `P` |

---

## Keyboard Shortcuts for Google Slides

| Action | Windows | Mac |
|--------|---------|-----|
| New slide | `Ctrl + M` | `Cmd + M` |
| Duplicate slide | `Ctrl + D` | `Cmd + D` |
| Present | `Ctrl + Shift + F5` | `Cmd + Shift + Enter` |
| Undo | `Ctrl + Z` | `Cmd + Z` |
| Redo | `Ctrl + Y` | `Cmd + Y` |

---

**End of HSU-3 Hands-On Exercise**
