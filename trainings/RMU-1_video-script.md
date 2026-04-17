# RMU-1 Video Script: Digital Records Tracking and Mail Management

**Duration:** 10-15 minutes
**Format:** Pre-recorded video for participants to watch before the in-person session
**Target Audience:** RMU staff, Records Officer, Receiving Clerks

---

## Opening: Analogy (30 seconds)

[SCREEN: Split screen showing a physical logbook on the left, Google Sheets on the right]

**Narrator:**

"Imagine you've been using the same physical logbook for years. You write down every incoming document, the date, who sent it, what it's about. It works—but there are problems. Only one person can write at a time. If the logbook gets lost or damaged, all that data is gone. And finding a document from three months ago means flipping through page after page.

Now imagine that same logbook, but digital. Multiple people can work on it simultaneously. It's backed up automatically in the cloud. You can search for any document in seconds. That's what we're going to build today—a digital records registry using Google Sheets."

[SCREEN: Title slide: "RMU-1: Digital Records Tracking and Mail Management"]

---

## Keywords and Concepts (2 minutes)

[SCREEN: Bulleted list of keywords appears one by one as narrator speaks]

**Narrator:**

"Before we dive in, let's cover some key terms you'll need to know.

**First: Control Number.** This is the unique identifier we assign to every incoming document. Per FAM 13.1 Section 3.4b, our format is: YYMMXX where YY is the year, MM is the month, and XX is the document count for that month. For example, 260401 means this is the 1st document received in April 2026. This format helps us trace and retrieve records quickly.

**Second: Timestamp.** This is the exact date and time a document is received. In Google Sheets, we can automatically capture this when data is entered—no more forgetting to write down the time!

**Third: Auto-fill.** Instead of manually typing control numbers, we'll use a formula that generates them automatically. This prevents duplicates and saves time.

**Fourth: Data Validation.** This is a feature that ensures data is entered correctly. For example, we can create a dropdown list of valid offices, so there's no confusion between 'HRU' and 'Human Resources.'

**Fifth: Conditional Formatting.** This automatically changes cell colors based on rules. We'll use it to highlight documents that haven't been released yet—so nothing falls through the cracks."

[SCREEN: Visual examples of each concept appear as they're mentioned]

---

## Pattern Demonstration (8-10 minutes)

### Step 1: Create the Google Sheet (1 minute)

[SCREEN: Screen recording of opening Google Drive and creating a new Sheet]

**Narrator:**

"Let's build our digital registry together. Start by opening Google Drive at drive.google.com. Click the '+ New' button, then select 'Google Sheets.'

Name your sheet something descriptive—like 'RMU_Digital_Registry_2026.' This makes it easy to find later.

Now, let's set up our columns. Per FAM 13.1, we need seven specific fields."

[SCREEN: Typing column headers]

**Narrator:**

"In cell A1, type: Date/Time Received.
In B1: Control Number.
In C1: Source/Sender.
In D1: Subject Matter.
In E1: Date Released.
In F1: Personnel/Office Assigned.
In G1: Remarks.

These match exactly what's required in the manual."

### Step 2: Format the Columns (1 minute)

[SCREEN: Demonstrating formatting options]

**Narrator:**

"Now let's format each column correctly. Select column A, go to Format, Number, and choose 'Date time'—this captures both the date and the time.

For column E, the Date Released column, choose 'Date.'

For the remaining columns, choose 'Plain text'—this prevents any automatic formatting that might interfere with our data.

Finally, let's make our headers stand out. Select row 1, make it bold, and add a background color. I'll use a light gray here, but you can use your unit's color."

### Step 3: Auto-Generate Control Numbers (3 minutes)

[SCREEN: Close-up of typing the formula]

**Narrator:**

"This is the most important part—the formula that auto-generates our control numbers. Remember, the format is YYMMXX where YY is the year, MM is the month, and XX is the document count for that month.

In cell B2, enter this formula exactly as I show it:

```
=IF(A2="", "", TEXT(A2, "YYMM") & TEXT(COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*"), "00"))
```

[SCREEN: Formula broken down with color-coded parts]

**Narrator:**

"Let me break this down so you understand what it does:

The `IF(A2="", "", ...)` part means: if there's no date entered, leave the cell blank. This prevents control numbers from appearing for empty rows.

`TEXT(A2, "YYMM")` extracts the year and month from the date you entered—so April 16, 2026 becomes 2604.

The `COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*")` counts how many documents have already been received this month.

Finally, `TEXT(..., "00")` formats the series number as two digits—so we get 01, 02, 03, and so on.

[SCREEN: Dragging the formula down]

**Narrator:**

"Once you've entered the formula in cell B2, drag it down for at least 50 rows—or however many documents you typically receive in a month. Now, whenever you enter a date in column A, the control number will appear automatically!"

### Step 4: Add Data Validation (1.5 minutes)

[SCREEN: Creating a list of offices in a separate area]

**Narrator:**

"To ensure consistency in the 'Personnel/Office Assigned' column, let's create a dropdown list. First, in a separate area of your sheet—or in a new tab—list all the valid offices: Campus Director, Executive Director, HRU, GSU, ACU, PRU, ITU, HSU, LIB, REG, RHU, and RMU.

[SCREEN: Applying data validation]

**Narrator:**

"Now select column F—the Personnel/Office Assigned column. Go to Data, then Data validation. Under 'Criteria,' choose 'Dropdown from a range,' and select the range containing your office list. Make sure 'Show dropdown list in cell' is checked, then click Done.

Now, when you click in this column, you'll see a dropdown menu with all the valid options. No more guessing or typos!"

### Step 5: Add Conditional Formatting (1.5 minutes)

[SCREEN: Setting up conditional formatting rules]

**Narrator:**

"Let's add visual cues to help us track document status. We'll highlight documents that have been received but not yet released in yellow, and documents that have been released in green.

Select your entire data range—from A2 to G100, or however many rows you need. Go to Format, then Conditional formatting.

[SCREEN: Adding the first rule]

**Narrator:**

"Add your first rule. Choose 'Custom formula is' and enter this formula:

```
=AND(A2<>"", E2="")
```

This means: if there's a date received but no date released, apply the formatting. Choose a yellow background, then click Done.

[SCREEN: Adding the second rule]

**Narrator:**

"Now add a second rule. Again, choose 'Custom formula is' and enter:

```
=E2<>""
```

This means: if there's a date released, apply the formatting. Choose a light green background, then click Done.

Now, as you work, you'll instantly see which documents are still pending (yellow) and which have been completed (green)."

### Step 6: Enter Sample Data (1 minute)

[SCREEN: Entering a sample document]

**Narrator:**

"Let's test our registry with a sample document. In cell A2, enter today's date and time—let's say April 16, 2026 at 9:00 AM.

Watch what happens in cell B2—the control number appears automatically! It should show 260401.

Now fill in the rest: Source/Sender is 'DOST Main Office,' Subject is 'Memorandum on 2026 Budget Allocation,' assigned to 'ACU,' and add a remark like 'Urgent - requires immediate action.'

[SCREEN: The row turns yellow]

**Narrator:**

"Notice the row turned yellow? That's because we haven't entered a Date Released yet. This document is still pending.

Now let's say ACU has acted on it. Enter today's date in the Date Released column.

[SCREEN: The row turns green]

**Narrator:**

"The row turned green! This document is now complete. This visual feedback helps you track status at a glance."

### Step 7: Search and Filter (30 seconds)

[SCREEN: Demonstrating the filter feature]

**Narrator:**

"One more powerful feature—search and filter. Click anywhere in your data, then go to Data and choose 'Create a filter.'

Now you'll see filter arrows in each header. Click the arrow in the Personnel/Office Assigned column, uncheck 'Select all,' then check just 'ACU.'

[SCREEN: Only ACU documents show]

**Narrator:**

"Now you see only documents assigned to ACU. This makes it easy to generate reports or check on specific units. Click the filter arrow again and choose 'Clear' to see all documents again."

---

## Quick Check Question (30 seconds)

[SCREEN: Question on screen with multiple choice options]

**Narrator:**

"Before we wrap up, here's a quick check to test your understanding:

**Question:** What formula would you use to auto-generate a control number in the format YYMMXX?

A) =TEXT(A2, "YYMM") & "-" & ROW()
B) =IF(A2="", "", TEXT(A2, "YYMM") & TEXT(COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*"), "00"))
C) =A2 & "-" & COUNTA(A:A)
D) =CONCATENATE(YEAR(A2), "-", MONTH(A2), "-", ROW())

[SCREEN: Pause for 5 seconds]

**Narrator:**

"The correct answer is B! This formula checks if there's a date, extracts the year and month, counts how many documents have been received this month, and formats it as a two-digit number.

If you got this right, great job! If not, don't worry—we'll practice this together in the in-person session."

---

## Closing (30 seconds)

[SCREEN: Summary of what was covered]

**Narrator:**

"In this video, you learned how to:

- Create a digital records registry in Google Sheets
- Set up the seven required columns per FAM 13.1
- Auto-generate control numbers using a formula
- Add data validation for consistent entries
- Use conditional formatting for visual status tracking
- Filter and search your data

[SCREEN: Next steps]

**Narrator:**

"In our in-person session, we'll practice this hands-on, and you'll complete a contest activity to test your skills. Bring your questions, and get ready to transform how RMU manages records!

See you there!"

[SCREEN: PSHS logo and "Thank you for watching"]

---

## Production Notes for Video Recording

### Technical Requirements
- **Resolution:** 1920x1080 (1080p) minimum
- **Audio:** Clear narration, no background noise
- **Screen Recording:** Use zoom-in features for formulas and small text
- **Pacing:** Speak clearly and at a moderate pace; allow pauses for viewers to process information

### Visual Style
- **Color Scheme:** Use PSHS branding colors where appropriate
- **Font:** Clean, readable sans-serif (Arial, Roboto, or similar)
- **Transitions:** Simple cuts or fades; avoid flashy transitions
- **Annotations:** Use arrows, circles, or highlights to draw attention to specific elements

### Accessibility
- **Captions:** Include closed captions for accessibility
- **Visual Cues:** Use visual indicators (like the yellow/green highlighting) to reinforce concepts
- **Pacing:** Allow time for viewers to read on-screen text before moving on

### Distribution
- **Format:** MP4 or WebM
- **File Size:** Compress to under 500MB for easy sharing via email or Google Drive
- **Hosting:** Upload to Google Drive and share link 2-3 days before the in-person session
- **Deadline:** Ensure video is available to participants at least 48 hours before the session

---

**End of RMU-1 Video Script**
