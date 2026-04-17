# Prompt for Code Mode Session: Building Training Guides

Copy everything below the line into a new Code mode session with GLM-4.7:

---

## Context

I work at Philippine Science High School - Main Campus (PSHS-MC). We are creating Google Workspace training guides for 10 administrative units. We have already completed the planning phase and need to build the actual training materials.

## What We've Already Done

1. Read all PSHS System manuals (Student Services Manual, Finance and Administration Manual) for each unit
2. Created a full curriculum with 23 sessions across 10 units
3. Scored each session for confidence and feasibility
4. Defined the teaching methodology (flipped classroom + gamification)

## Key Files to Read First

**You MUST read these files before starting any work:**

1. `plans/google-workspace-training-curriculum.md` — Full curriculum with all sessions, manual citations, tools, and prerequisites
2. `plans/training-confidence-feasibility-assessment.md` — Confidence/feasibility scores and prioritized build order

Also read the relevant manual sections referenced in each session. The manuals are in the `manuals/` directory:
- Student Services Manual (SSM): `manuals/STUDENT SERVICES MANUAL (SSM) Ver2/Manuals/`
- Finance and Administration Manual (FAM): `manuals/FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2/Manuals/`

Editable form templates are in the `Forms/` subdirectories within each manual folder.

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

## Deliverables Per Session (4 files in /trainings/)

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

## PSHS-Specific Analogies to Use

- Physical logbook → Google Sheet (RMU, HSU, GSU all use logbooks)
- Carbon copy forms → Google Forms (responses auto-copy to multiple people)
- Filing cabinet with folders → Google Drive folders (same hierarchy, digital)
- Inter-office envelope with routing slip → Google Drive sharing (same routing, instant)
- Bulletin board → Google Sites (same information posting, always accessible)
- Calculator and ledger → Google Sheets formulas (same math, automatic)

## Training Environment

- Participants have computers/laptops (fully hands-on)
- Class size: 10-15 per session
- Using the actual PSHS Google Workspace domain
- Leave-behind guides printed as PDF cards (front-and-back)

## Build Order (Start with RMU-1)

**START WITH RMU-1 (Records Management Unit - Session 1: Digital Records Tracking and Mail Management).** This is our strongest session (90% confidence, 90% feasibility) because FAM 13.1 is the most detailed manual (19 pages) with explicitly listed fields and control number formats. It will serve as the TEMPLATE for all other sessions.

After RMU-1 is complete and approved, build these Tier 1 sessions next:
- Session 0 (Google Workspace Fundamentals - for all units)
- LO-1 (LibreOffice as Offline Backup - for all units)
- RHU-1 (Residence Hall Administration)
- HSU-3 (Infectious Disease Monitoring)
- GSU-2 (Facility Use Management and Performance Evaluation)

## Important Notes

- Use ACTUAL form names, form numbers, and manual section references (not generic examples)
- The editable form templates (.xlsx, .docx) exist in the manuals directory — reference them
- All manual citations should use the format: "SSM 6.2 Section 4.1" or "FAM 13.1 Section 3.4b"
- Include LibreOffice equivalents where applicable (as offline backup)
- Keep the language accessible — avoid jargon unless it's a keyword being taught
- The contest activity should be fun but practical — it tests real job skills

## First Task

Read `plans/google-workspace-training-curriculum.md` and `plans/training-confidence-feasibility-assessment.md`, then read the RMU-relevant manual sections (FAM 13.1 in `manuals/FINANCE AND ADMINISTRATION MANUAL (FAM) Ver2/Manuals/PSHSS FAM 13.1 Records Management V2_Rev2.pdf`). Then build all 4 deliverables for session RMU-1 in the `/trainings/` directory.
