# HSU-3 Trainer Guide: Infectious Disease Monitoring and Health Campaigns

## Session Metadata

| Field | Value |
|-------|-------|
| **Unit** | Health Services Unit (HSU) |
| **Session ID** | HSU-3 |
| **Session Title** | Infectious Disease Monitoring and Health Campaigns |
| **Duration** | 45 minutes |
| **Prerequisites** | Session 0 (Google Workspace Fundamentals) |
| **Google Workspace Tools** | Google Sheets, Google Slides, Google Forms |
| **LibreOffice Equivalent** | LibreOffice Calc, Impress (optional - to be deployed campus-wide) |
| **Manual Reference** | SSM 6.7 Infectious Disease Monitoring, SSM 6.5 Health Information Campaign |
| **Target Audience** | HSU staff, School Nurse, Physician |

## Time Allocation Breakdown

| Component | Time | Notes |
|-----------|------|-------|
| **Pre-Session Video** (asynchronous) | 10-15 min | Sent 2-3 days before session |
| **In-Person Session** | 45 min | |
| ├─ Welcome and Q&A on Video | 3 min | Address questions from pre-session video |
| ├─ Disease Monitoring Tracker | 12 min | Google Sheets with charts and pivot tables |
| ├─ Health Campaign Materials | 10 min | Google Slides for presentations |
| ├─ Health Awareness Surveys | 10 min | Google Forms for data collection |
| ├─ Audience Practice | 7 min | Guided hands-on exercise |
| └─ Wrap-up & Scoring | 3 min | Review, answer key, leaderboard update |

## Learning Objectives

By the end of this session, participants will be able to:

1. Create a disease monitoring tracker in Google Sheets per SSM 6.7
2. Use charts and pivot tables to visualize disease trends and patterns
3. Create health campaign materials in Google Slides per SSM 6.5
4. Design health awareness surveys using Google Forms
5. Analyze survey data to inform future health campaigns
6. Apply conditional formatting to highlight urgent cases
7. Organize HSU documents in Google Drive with proper folder structure

## Materials Needed

- Computers/laptops with internet access
- Access to PSHS Google Workspace domain
- Sample disease data for practice
- Printed quick reference cards (one per participant)
- Projector for demonstration
- Whiteboard or digital equivalent

## Pre-Session Video Content Summary

The pre-session video (10-15 minutes) covers:
1. **Analogy** (30 sec): Physical bulletin board → Google Slides
2. **Keywords & Concepts** (2 min): Pivot tables, charts, data visualization, conditional formatting, survey design
3. **Pattern Demonstration** (8-10 min): Building disease tracker, creating campaign materials, designing surveys
4. **Quick Check Question** (30 sec): "What Google Workspace tool would you use to create a pivot table for disease data analysis?"

---

## In-Person Session Script

### 1. Welcome and Quick Q&A (3 minutes)

**Trainer Script:**

"Good morning/afternoon, everyone! Welcome to HSU-3: Infectious Disease Monitoring and Health Campaigns.

This session will transform how HSU monitors infectious diseases and creates health campaign materials using Google Workspace. We'll create digital tools for disease tracking, data visualization, and health awareness surveys.

Before we dive in, let's address any questions you might have from the pre-session video."

**Anticipated Questions & Answers:**

| Question | Answer |
|----------|--------|
| "Why do we need a digital disease tracker?" | A digital tracker allows real-time monitoring, instant search, and automatic calculations. You can quickly identify trends, generate reports, and share data with stakeholders per SSM 6.7. |
| "Can we still use paper forms?" | Yes, you can collect data on paper and enter it into the digital system. The digital system enhances, not replaces, existing processes. |
| "How do we create charts from our data?" | Google Sheets has built-in chart tools. Select your data, click Insert, Chart, and choose the chart type. It's that simple! |
| "What about privacy of student health data?" | This is critical. Share spreadsheets only with authorized HSU staff. Use Google Drive permissions to control access. Never share sensitive health data publicly. |

**Trainer Script:**

"Great questions! Remember, the goal is to make HSU operations more efficient while maintaining compliance with SSM 6.7 and 6.5. Let's move to our first topic."

---

### 2. Disease Monitoring Tracker (12 minutes)

**Trainer Script:**

"Per SSM 6.7, we need to monitor infectious diseases among students and employees. Let's create a disease monitoring tracker in Google Sheets."

#### Step-by-Step Demo Script

**Step 1: Create the Google Sheet**

1. Go to `drive.google.com`
2. Click **+ New** → **Google Sheets**
3. Name the sheet: `Infectious_Disease_Monitoring_2026`

**Step 2: Set Up Column Headers**

[SCREEN: Typing column headers]

**Trainer Script:**

"Per SSM 6.7 Section 3.2, let's set up these columns:

Row 1 headers:
- A: Date Reported
- B: Student/Employee Name
- C: Grade Level/Position
- D: Disease Type
- E: Symptoms
- F: Date Onset
- G: Status
- H: Date Cleared
- I: Days Absent
- J: Class/Section
- K: Notes

**Step 3: Format Columns**

1. Select row 1 → **Bold** → Add background color
2. Select columns A, F, G, H → **Format** → **Number** → **Date**
3. Select column I → **Format** → **Number** → **Number** (for days absent)
4. Select columns D, E, G → **Data** → **Data validation**
5. For Disease Type (D): Dropdown with options per SSM 6.7:
   - Acute Viral/Bacterial Conjunctivitis
   - Viral Exanthems (Measles)
   - Viral Exanthems (Chickenpox)
   - Parotitis (Mumps)
   - Dengue Infections
   - Amoebiasis
   - Typhoid Fever
   - Hepatitis A
   - Other
6. For Status (G): Dropdown: Active, Recovered, Referred, Under Observation
7. For Symptoms (E): Paragraph text for detailed symptoms

**Step 4: Add Formulas**

[SCREEN: Adding formulas]

**Trainer Script:**

"Let's add formulas to automate calculations.

Column I (Days Absent): In cell I2, enter:
```
=IF(AND(H2<>"",F2<>""), (H2-F2), "")
```
This calculates the number of days between onset and clearance.

Column J (Current Status Indicator): In cell K2, enter:
```
=IF(G2="Active", "⚠️ URGENT", IF(G2="Recovered", "✅ Cleared", ""))
```
This adds visual indicators for active cases."

**Step 5: Add Conditional Formatting**

[SCREEN: Setting up conditional formatting]

**Trainer Script:**

"Let's add visual cues for active cases.

1. Select columns A through K
2. Click **Format** → **Conditional formatting**
3. Add rule 1:
   - Format cells if: **Custom formula is**
   - Formula: `=$G2="Active"`
   - Formatting: Red background with bold text
4. Add rule 2:
   - Format cells if: **Custom formula is**
   - Formula: `=$G2="Recovered"`
   - Formatting: Green background
5. Add rule 3:
   - Format cells if: **Custom formula is**
   - Formula: `=$G2="Referred"`
   - Formatting: Orange background"

**Step 6: Create a Pivot Table**

[SCREEN: Creating a pivot table]

**Trainer Script:**

"Now let's create a pivot table to analyze disease patterns.

1. Select all data (columns A through K)
2. Click **Insert** → **Pivot table**
3. Choose to create in a new sheet
4. In the pivot table editor:
   - Rows: Disease Type
   - Columns: Status
   - Values: Count of Student/Employee Name
5. This shows a summary of cases by disease type and status

**Step 7: Create a Chart**

[SCREEN: Creating a chart]

**Trainer Script:**

"Let's create a chart to visualize disease trends.

1. Select the pivot table data
2. Click **Insert** → **Chart**
3. Choose a chart type (Column chart works well)
4. Customize the chart title: 'Infectious Disease Cases by Type - 2026'
5. The chart updates automatically as you add new data"

---

### 3. Health Campaign Materials (10 minutes)

**Trainer Script:**

"Per SSM 6.5, HSU spearheads health information dissemination campaigns. Let's create campaign materials in Google Slides."

#### Step-by-Step Demo Script

**Step 1: Create a Google Slides Presentation**

1. Go to `drive.google.com`
2. Click **+ New** → **Google Slides**
3. Name the presentation: `Dengue_Prevention_Campaign_2026`

**Step 2: Create Slide 1 (Title Slide)**

[SCREEN: Creating title slide]

**Narrator:**

"Click in the title box and type: 'Dengue Prevention Campaign'

Click in the subtitle box and type: 'Protect Our School Community'

Add a background color or image related to health/dengue prevention."

**Step 3: Create Slide 2 (What is Dengue?)**

1. Click **Insert** → **Slide** (or press `Ctrl+M`)
2. Title: 'What is Dengue?'
3. Content:
   ```
   Dengue is a mosquito-borne viral infection causing severe flu-like illness.
   
   Symptoms:
   • High fever
   • Severe headache
   • Pain behind eyes
   • Joint and muscle pain
   • Skin rash
   
   Prevention:
   • Eliminate mosquito breeding sites
   • Use mosquito repellent
   • Wear protective clothing
   • Install screens on windows
   ```

**Step 4: Create Slide 3 (4-S Campaign)**

1. Insert new slide
2. Title: '4-S Against Dengue'
3. Content:
   ```
   Search and Destroy
   • Eliminate breeding sites
   • Clean water containers weekly
   
   Self-Protection Measures
   • Use repellent
   • Wear long sleeves/pants
   • Install window screens
   
   Seek Early Consultation
   • Consult doctor if symptoms appear
   • Do not self-medicate
   
   Support Fogging/Spraying
   • Participate in fogging activities
   • Report dengue cases immediately
   ```

**Step 5: Create Slide 4 (Call to Action)**

1. Insert new slide
2. Title: 'What You Can Do'
3. Content:
   ```
   • Check your surroundings for stagnant water
   • Keep your surroundings clean
   • Report suspected dengue cases to HSU
   • Participate in school-wide clean-up drives
   • Educate your family and friends
   
   For more information, visit HSU or contact:
   School Nurse: [Contact Information]
   ```

**Step 6: Add Visual Elements**

1. Click **Insert** → **Image** → Upload relevant health images
2. Add icons or shapes to make slides more engaging
3. Use consistent colors and fonts throughout
4. Add PSHS logo to each slide

**Step 7: Export as PDF**

1. Click **File** → **Download** → **PDF Document (.pdf)`
2. The presentation can be printed as posters or shared digitally

---

### 4. Health Awareness Surveys (10 minutes)

**Trainer Script:**

"Per SSM 6.5, we need to assess the effectiveness of health campaigns. Let's create a health awareness survey using Google Forms."

#### Step-by-Step Demo Script

**Step 1: Create the Google Form**

1. Go to `forms.google.com`
2. Click **+ Blank**
3. Name the form: `Dengue_Awareness_Survey_2026`

**Step 2: Add Questions**

[SCREEN: Creating survey questions]

**Trainer Script:**

"Let's add questions to assess knowledge and awareness.

**Section 1: Demographics**
- Title: Student Information
- Question 1: Grade Level (Dropdown: Grade 7-12)
- Question 2: Section (Short answer)

**Section 2: Knowledge Assessment**
- Title: What You Know About Dengue
- Question 3: How is dengue transmitted? (Multiple choice: Mosquito bite, Direct contact, Contaminated food, Airborne)
- Question 4: What are the symptoms of dengue? (Checkboxes: High fever, Severe headache, Joint pain, Skin rash, All of the above)
- Question 5: How can we prevent dengue? (Checkboxes: Eliminate breeding sites, Use repellent, Wear protective clothing, Install screens, All of the above)

**Section 3: Behavior Assessment**
- Title: Your Practices
- Question 6: How often do you check for stagnant water around you? (Dropdown: Daily, Weekly, Monthly, Rarely, Never)
- Question 7: Do you use mosquito repellent? (Yes/No)
- Question 8: Do you wear long sleeves/pants when outdoors? (Yes/No)

**Section 4: Feedback**
- Title: Your Suggestions
- Question 9: What other health topics would you like HSU to address? (Paragraph)
- Question 10: How can HSU improve health campaigns? (Paragraph)

**Step 3: Configure and Share**

1. Click **Settings** → Enable "Collect email addresses" (optional, for tracking)
2. Click **Responses** → Link to a Google Sheet
3. Click **Send** → Copy the link
4. Share with students via email or class groups

**Step 4: Analyze Responses**

1. Open the response spreadsheet
2. Use charts to visualize knowledge levels
3. Identify gaps in awareness
4. Use data to improve future campaigns

---

### 5. Audience Practice: Guided Exercise (7 minutes)

**Trainer Script:**

"Now it's your turn! I'll guide you through a quick exercise. Follow along with me."

#### Exercise Steps

**Step 1: Create a Disease Tracker (2 minutes)**
1. Create a new Google Sheet named `Practice_Disease_Tracker`
2. Add headers: Date, Name, Disease Type, Status
3. Add data validation for Disease Type (Dengue, Flu, Chickenpox, Other)
4. Add conditional formatting (Red for Active, Green for Recovered)
5. Enter 2 sample cases

**Step 2: Create a Simple Chart (2 minutes)**
1. Select your data
2. Click **Insert** → **Chart**
3. Choose a column chart
4. Customize the title
5. Observe how the chart visualizes your data

**Step 3: Create a Campaign Slide (2 minutes)**
1. Create a new Google Slides presentation
2. Create 2 slides about a health topic (e.g., Hand Washing)
3. Add content and visual elements
4. Make it visually appealing

**Step 4: Create a Survey (1 minute)**
1. Create a new Google Form named `Practice_Health_Survey`
2. Add 3 questions about health knowledge
3. Submit a test response
4. View the response spreadsheet

**Trainer Circulation:**

While participants work, circulate to:
- Check that trackers are set up correctly
- Ensure charts are displaying properly
- Verify slides are visually appealing
- Confirm surveys are collecting responses
- Answer individual questions
- Provide encouragement

---

### 6. Wrap-up, Answer Key, and Scoring (3 minutes)

#### Answer Key

**Expected Outputs:**
- Disease tracker with headers, data validation, and conditional formatting
- Chart displaying disease data
- 2-slide presentation on a health topic
- Survey form with 3 questions and responses collected

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
| HSU | ___ | ___ | ___ | ___ |
| ... | ... | ... | ... | ... |

*(Fill in during actual training)*

---

## Troubleshooting Tips

### Common Mistakes and Solutions

| Mistake | Solution |
|---------|----------|
| Pivot table not showing data | Check that you selected the correct data range. Ensure headers are in the first row. |
| Chart not updating | Refresh the chart or check that data range is correct. |
| Conditional formatting not working | Verify formula syntax and that it's applied to the correct range. |
| Survey responses not appearing | Check that form is linked to a spreadsheet. |
| Can't find uploaded files | Check the folder you created or search by filename. |
| Formula shows #VALUE! error | Check that referenced cells contain the correct data type (dates for date calculations). |

### Tips for Success

1. **Use consistent naming** for all files and folders
2. **Update the tracker daily** during disease outbreaks
3. **Use charts to identify trends** and inform decision-making
4. **Create reusable slide templates** for different health topics
5. **Analyze survey data** to improve future campaigns
6. **Back up data regularly** (download as .ods for LibreOffice)
7. **Protect student privacy** — share only with authorized staff
8. **Follow DOH Calendar** when planning health campaigns (per SSM 6.5)

---

## Manual References

All materials reference:
- **SSM 6.7 Infectious Disease Monitoring V2_Rev0** — Sections 3.2 (Diseases to monitor), 3.4 (Excused from classes), 5.0 (Forms and Reports)
- **SSM 6.5 Health Information Campaign V2_Rev0** — Sections 3.2 (Campaign strategies), 3.5 (Bulletin Board), 4.0 (Procedures)

---

## Assessment and Follow-up

### Immediate Assessment

The audience practice serves as the immediate practical assessment. Participants who complete all tasks successfully have demonstrated competency.

### 60-Day Follow-Up (Per FAM 4.7 Section 4.6)

Two months after training, the HSU Head should assess:

1. **Application on the Job:** Are staff using digital tools for disease monitoring and campaigns?
2. **Efficiency Gains:** Has the time to generate reports decreased?
3. **Error Reduction:** Have errors in data entry decreased?
4. **Challenges Encountered:** What difficulties are staff facing?
5. **Additional Training Needed:** What topics need reinforcement?

### Recommended Next Steps

1. **Implement disease monitoring tracker** for current school year
2. **Create campaign materials** for upcoming health topics
3. **Conduct health awareness surveys** and analyze results
4. **Schedule HSU-1 and HSU-2** for additional training (if needed)
5. **Monitor disease trends** using charts and pivot tables

---

## Pre-Training Setup Recommendations

Before the first HSU-3 session:

1. **Create a shared Google Drive folder** for all HSU training materials
2. **Prepare sample disease data** for practice
3. **Set up the leaderboard** in Google Sheets with read-only access
4. **Set up a "HSU Help" channel** in Google Chat for ongoing questions
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
2. **Create a shared "HSU Help" channel** in Google Chat for ongoing questions
3. **Appoint "digital champions"** in HSU who can help colleagues
4. **Collect feedback** on the training materials for continuous improvement

---

## References

- **SSM 6.7 Infectious Disease Monitoring V2_Rev0**
- **SSM 6.5 Health Information Campaign V2_Rev0**
- **Google Sheets Help Center** — sheets.google.com/support
- **Google Slides Help Center** — slides.google.com/support
- **Google Forms Help Center** — forms.google.com/support
- **LibreOffice Documentation** — help.libreoffice.org

---

## Trainer Notes

- **Pace:** Adjust timing based on participant comfort level. If participants are struggling with pivot tables, spend more time on them.
- **Analogies:** Emphasize the physical bulletin board → Google Slides analogy throughout.
- **Real Examples:** Use actual HSU scenarios and data to make the training more relevant.
- **Manual References:** Frequently reference SSM 6.7 and 6.5 to show compliance.
- **Privacy:** Emphasize the importance of protecting student health data.
- **Follow-up:** Schedule a check-in with the HSU Head 2 weeks after training to address any issues.

---

**End of HSU-3 Trainer Guide**
