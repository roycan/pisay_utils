# Prompt for Code Mode Session: Building Remaining Tier 1 Training Guides

Copy everything below the line into a new Code mode session with GLM-4.7:

---

## Context

I work at Philippine Science High School - Main Campus (PSHS-MC). We are creating Google Workspace training guides for 10 administrative units. We have already completed the planning phase and built RMU-1 as our template session. Now we need to build the remaining Tier 1 sessions using the same structure and quality.

## What We've Already Done

1. Read all PSHS System manuals (Student Services Manual, Finance and Administration Manual) for each unit
2. Created a full curriculum with 23 sessions across 10 units
3. Scored each session for confidence and feasibility
4. Defined the teaching methodology (flipped classroom + gamification)
5. Built RMU-1 as our template session (all 4 deliverables + CSV template + README)

## Key Files to Read First

**You MUST read these files before starting any work:**

1. `plans/google-workspace-training-curriculum.md` — Full curriculum with all sessions, manual citations, tools, and prerequisites
2. `plans/training-confidence-feasibility-assessment.md` — Confidence/feasibility scores and prioritized build order
3. `trainings/RMU-1_trainer-guide.md` — **THIS IS YOUR TEMPLATE.** Follow this exact structure, format, and level of detail for all new sessions.
4. `trainings/RMU-1_video-script.md` — Template for the pre-session video script
5. `trainings/RMU-1_exercise.md` — Template for the hands-on exercise
6. `trainings/RMU-1_quick-ref-card.md` — Template for the quick reference card

Also read the relevant manual sections referenced in each session. The manuals are in the `manuals/` directory:
- Student Services Manual (SSM): `manuals/STUDENT SERVICES MANUAL (SSM) Ver2/Manuals/`
- Finance and Administration Manual (FAM): `manuals/FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2/Manuals/`

## Teaching Methodology (Flipped Classroom)

Each session has TWO parts:

**Part 1: Pre-Session Video (10-15 min, asynchronous)**
- Analogy that relates to something PSHS staff already know
- Keywords, patterns, and examples (instructor demonstrates)
- Screen recordings of actual Google Workspace tools
- Ends with a "quick check" question

**Part 2: In-Person Session (45min-1hr15min, synchronous, hands-on)**
- Quick Q&A on video (5 min)
- Joint Discussion: Collaborative example using actual unit data (15 min)
- Audience Practice: Participants work through guided exercises (20 min)
- Contest Activity: Independent challenge for inter-unit competition (10-20 min)

## Deliverables Per Session (6 files in /trainings/)

For each session, create these files in the `/trainings/` directory:

1. **`SESSION-ID_trainer-guide.md`** — Full trainer script with:
   - Session metadata (unit, duration, prerequisites, tools needed)
   - Time allocation breakdown
   - Analogy script (with PSHS-specific comparison)
   - Key concepts and keywords to emphasize
   - Step-by-step demo script with exact clicks/keystrokes
   - Joint discussion walkthrough (using actual unit forms/data)
   - Audience practice instructions (guided, step-by-step)
   - Contest activity description and scoring rubric
   - Answer key / expected outputs
   - Troubleshooting tips for common mistakes
   - Pre-training setup recommendations
   - Follow-up support suggestions

2. **`SESSION-ID_video-script.md`** — Word-for-word script for the 10-15 minute recorded lesson:
   - Opening analogy (30 seconds)
   - Keywords and concepts (2 minutes)
   - Pattern demonstration with screen recording cues (8-10 minutes)
   - Quick check question (30 seconds)
   - Slide/screen recording cues marked as [SCREEN: description of what to show]

3. **`SESSION-ID_exercise.md`** — Hands-on exercise using actual PSHS forms and data:
   - Exercise scenario based on real unit workflow
   - Step-by-step instructions (numbered, with expected outcome at each step)
   - Screenshots placeholders marked as [SCREENSHOT: description]
   - Challenge variations (basic, intermediate, advanced)
   - Self-check answers at the end

4. **`SESSION-ID_quick-ref-card.md`** — Quick reference card (designed for front-and-back PDF):
   - Side A: Step-by-step walkthrough of the single most common task (with minimal text, heavy on visuals/screenshots)
   - Side B: Keyboard shortcuts, tips, common pitfalls, and "where to find help"
   - Keep it concise — this is a cheat sheet, not a manual

5. **`SESSION-ID_template.csv`** — Pre-built CSV template for import into Google Sheets:
   - Column headers matching the session's data structure
   - Empty rows for data entry
   - Any reference lists (e.g., office names, status options) at the bottom

6. **`SESSION-ID_README.md`** — Summary file explaining:
   - Session overview and learning objectives
   - Files included and how to use them
   - Pre-training setup checklist
   - Post-training follow-up steps
   - Manual references

## PSHS-Specific Analogies to Use

- Physical logbook → Google Sheet (RMU, HSU, GSU all use logbooks)
- Carbon copy forms → Google Forms (responses auto-copy to multiple people)
- Filing cabinet with folders → Google Drive folders (same hierarchy, digital)
- Inter-office envelope with routing slip → Google Drive sharing (same routing, instant)
- Bulletin board → Google Sites (same information posting, always accessible)
- Calculator and ledger → Google Sheets formulas (same math, automatic)
- Physical attendance sheet → Google Sheet with auto-date stamping
- Clipboard checklist → Google Forms (same checking off, instant tally)
- Wall calendar → Google Calendar (same scheduling, shared and searchable)

## Training Environment

- Participants have computers/laptops (fully hands-on)
- Class size: 10-15 per session
- Using the actual PSHS Google Workspace domain
- Leave-behind guides printed as PDF cards (front-and-back)
- LibreOffice is optional — will be deployed campus-wide before full training rollout

## Important Notes

- Use ACTUAL form names, form numbers, and manual section references (not generic examples)
- The editable form templates (.xlsx, .docx) exist in the manuals directory — reference them
- All manual citations should use the format: "SSM 6.2 Section 4.1" or "FAM 13.1 Section 3.4b"
- Include LibreOffice equivalents where applicable (as optional offline backup)
- Keep the language accessible — avoid jargon unless it's a keyword being taught
- The contest activity should be fun but practical — it tests real job skills
- Follow the EXACT structure of RMU-1 files for consistency

## Sessions to Build (Tier 1)

Build these 5 sessions in order:

### 1. Session 0: Google Workspace Fundamentals
- **Duration:** 1 hour 30 minutes
- **Audience:** ALL units (mandatory)
- **Prerequisites:** Basic computer literacy
- **Manual Reference:** FAM 12.2 (Information Technology Management)
- **Tools:** Gmail, Drive, Calendar, Docs, Sheets, Slides, Forms, Meet, Chat
- **Key Topics:** PSHS email policies per FAM 12.2 Section 3.2, Drive folder structure, Gmail essentials, Calendar basics, Chat vs Gmail, LibreOffice overview
- **Read:** `manuals/FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2/Manuals/PSHSS FAM 12.2 Information Technology Management V2_Rev3.pdf`

### 2. LO-1: LibreOffice as Offline Backup
- **Duration:** 1 hour
- **Audience:** All units (recommended)
- **Prerequisites:** Session 0
- **Tools:** LibreOffice Writer, Calc, Impress
- **Key Topics:** Installing LibreOffice, opening Google files in LibreOffice, saving in multiple formats, offline workflow (work offline → upload when online), Google Drive desktop app for offline access
- **Note:** LibreOffice will be deployed campus-wide — this session teaches how to use it as backup

### 3. RHU-1: Residence Hall Administration and Monitoring
- **Duration:** 1 hour 15 minutes
- **Audience:** Residence Hall Unit
- **Prerequisites:** Session 0
- **Manual Reference:** SSM 5.1, SSM 5.2
- **Tools:** Google Forms, Google Sheets, Google Docs
- **Forms Used:** Residence Hall Application Form (PSHS-00-F-RHU-01), Residence Hall Contract (RHU-02), Parent/Guardian Waiver (RHU-03), List of Appliances (RHU-04), Good Housekeeping Checklist (RHU-05), Leave Pass and Return Slip (RHU-07)
- **Key Topics:** Digital residence hall application via Google Forms, resident management tracker in Sheets, contract templates in Docs, Good Housekeeping Checklist as digital form, leave pass tracking with timestamps
- **Read:** `manuals/STUDENT SERVICES MANUAL (SSM) Ver2/Manuals/PSHSS SSM 5.1 Evaluation of Students Application for Residence Hall Accommodation V2_Rev0.pdf` and `manuals/STUDENT SERVICES MANUAL (SSM) Ver2/Manuals/PSHSS SSM 5.2 Residence Hall Accommodation V2_Rev0.pdf`

### 4. HSU-3: Infectious Disease Monitoring and Health Campaigns
- **Duration:** 45 minutes
- **Audience:** Health Services Unit
- **Prerequisites:** Session 0
- **Manual Reference:** SSM 6.7, SSM 6.5
- **Tools:** Google Sheets, Google Slides, Google Forms
- **Forms Used:** Infectious Disease Monitoring Tool (PSHS-00-F-HSU-06)
- **Key Topics:** Disease monitoring tracker in Sheets with charts and pivot tables, health campaign materials in Slides, health awareness surveys via Forms
- **Read:** `manuals/STUDENT SERVICES MANUAL (SSM) Ver2/Manuals/PSHSS SSM 6.7 Infectious Disease Monitoring V2_Rev0.pdf` and `manuals/STUDENT SERVICES MANUAL (SSM) Ver2/Manuals/PSHSS SSM 6.5 Health Information Campaign V2_Rev0.pdf`

### 5. GSU-2: Facility Use Management and Performance Evaluation
- **Duration:** 1 hour
- **Audience:** General Services Unit
- **Prerequisites:** Session 0, GSU-1 (but GSU-1 hasn't been built yet — note this as a prerequisite)
- **Manual Reference:** FAM 6.2, FAM 6.3, FAM 6.6
- **Tools:** Google Calendar, Google Forms, Google Sheets
- **Forms Used:** Permit to Use School Facilities (PSHS-00-F-GSM-02), Permit to Use School Vehicle (PSHS-00-F-GSM-03), Cleaning Checklist (PSHS-00-F-GSM-05), Security Guard Work Performance Evaluation Form (PSHS-00-F-GSM-12), Janitorial Performance Evaluation Form (PSHS-00-F-GSM-13)
- **Key Topics:** Shared Google Calendars for facility/vehicle booking, digital permit forms, performance evaluation scoring with automatic calculation in Sheets
- **Read:** `manuals/FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2/Manuals/PSHSS FAM 6.2 Use of Vehicle, Facilities and Equipment V2_Rev1.p.pdf`, `manuals/FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2/Manuals/PSHSS FAM 6.3 Janitorial Services V2_Rev0.pdf`, and `manuals/FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2/Manuals/PSHSS FAM 6.6 Security Services V2_Rev0.pdf`

## Build Order

1. **Session 0** first — everyone needs this, highest impact
2. **LO-1** second — quick to build, universal need
3. **RHU-1** third — clean, well-scoped, good forms
4. **HSU-3** fourth — short, focused, 45 minutes
5. **GSU-2** fifth — Google Calendar is easy to teach

## Quality Checklist

Before submitting each session, verify:

- [ ] All 6 files created with correct naming convention
- [ ] Manual citations use the format "SSM X.X Section Y" or "FAM X.X Section Y"
- [ ] Actual PSHS form names and numbers are used (not generic examples)
- [ ] PSHS-specific analogy is included
- [ ] Contest activity has scoring rubric
- [ ] Answer key / expected outputs are provided
- [ ] Pre-training setup checklist is included
- [ ] Follow-up support suggestions are included
- [ ] LibreOffice is mentioned as optional backup
- [ ] Structure matches RMU-1 template exactly

## First Task

Read the RMU-1 template files first:
1. `trainings/RMU-1_trainer-guide.md`
2. `trainings/RMU-1_video-script.md`
3. `trainings/RMU-1_exercise.md`
4. `trainings/RMU-1_quick-ref-card.md`
5. `trainings/RMU-1_template.csv`
6. `trainings/RMU-1_README.md`

Then read the curriculum and assessment files:
7. `plans/google-workspace-training-curriculum.md`
8. `plans/training-confidence-feasibility-assessment.md`

Then read the manual for Session 0:
9. `manuals/FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2/Manuals/PSHSS FAM 12.2 Information Technology Management V2_Rev3.pdf`

Then build all 6 deliverables for Session 0 in the `/trainings/` directory. After Session 0 is complete, proceed to LO-1, then RHU-1, then HSU-3, then GSU-2.
