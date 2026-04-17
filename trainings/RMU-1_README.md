# RMU-1 Training Materials

## Overview

This folder contains all training materials for **RMU-1: Digital Records Tracking and Mail Management**, the first session in the Google Workspace training curriculum for PSHS-MC administrative units.

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | RMU-1 |
| **Session Title** | Digital Records Tracking and Mail Management |
| **Duration** | 1 hour 30 minutes (90 minutes) |
| **Prerequisites** | Session 0 (Google Workspace Fundamentals) |
| **Google Workspace Tools** | Google Sheets, Google Forms, Google Drive |
| **Manual Reference** | FAM 13.1 Records Management V2_Rev2 |
| **Target Audience** | RMU staff, Records Officer, Receiving Clerks |

## Files Included

### 1. Trainer Guide (`RMU-1_trainer-guide.md`)
Complete trainer script with:
- Session metadata and learning objectives
- Time allocation breakdown (90 minutes)
- Opening Q&A with anticipated questions
- Joint discussion: Building the digital registry (step-by-step demo)
- Audience practice: Guided exercise with 5 sample documents
- Contest activity: Independent challenge with 8 documents
- Answer key and scoring rubric
- Troubleshooting tips
- Extension activities (Google Forms, Drive folders, LibreOffice)
- Assessment and follow-up guidance
- Pre-training setup recommendations
- Video production tips
- Follow-up support suggestions

### 2. Video Script (`RMU-1_video-script.md`)
10-15 minute pre-session video script with:
- Opening analogy (physical logbook → Google Sheet)
- Keywords and concepts explanation
- Pattern demonstration with screen recording cues
- Quick check question
- Production notes for video recording

### 3. Hands-On Exercise (`RMU-1_exercise.md`)
Guided exercise with:
- Exercise scenario (Records Officer on duty)
- 10 step-by-step instructions
- 5 sample documents to enter
- Self-check answers
- Challenge variations (basic, intermediate, advanced)
- Troubleshooting guide

### 4. Quick Reference Card (`RMU-1_quick-ref-card.md`)
Front-and-back reference card with:
- **Side A:** Step-by-step guide for entering documents, finding documents, working offline
- **Side B:** Keyboard shortcuts, control number formula, common tasks, color coding guide, common mistakes to avoid, where to find help, emergency solutions, analogy reminder

### 5. Template Sheet (`RMU-1_template.csv`)
Pre-built CSV template that can be imported into Google Sheets:
- 50 empty rows for data entry
- 7 column headers (Date/Time Received, Control Number, Source/Sender, Subject Matter, Date Released, Personnel/Office Assigned, Remarks)
- Office list at the bottom (14 offices) for data validation

**How to use the template:**
1. Go to Google Drive (drive.google.com)
2. Click **+ New** → **File upload**
3. Select `RMU-1_template.csv`
4. The file will open in Google Sheets
5. Rename it as needed (e.g., `RMU_Digital_Registry_2026`)
6. Apply the control number formula in cell B2:
   ```
   =IF(A2="", "", TEXT(A2, "YYMM") & TEXT(COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*"), "00"))
   ```
7. Drag the formula down for all data rows
8. Set up data validation for column F using the office list (rows 52-65)

## Control Number Format

**Format:** YYMMXX

- **YY:** Year (2 digits) - e.g., 26 for 2026
- **MM:** Month (2 digits) - e.g., 04 for April
- **XX:** Document count for that month (2 digits) - e.g., 01, 02, 03...

**Examples:**
- `260401` = 1st document received in April 2026
- `260410` = 10th document received in April 2026
- `260501` = 1st document received in May 2026

**Formula:**
```
=IF(A2="", "", TEXT(A2, "YYMM") & TEXT(COUNTIF($B$1:B1, TEXT(A2, "YYMM") & "*"), "00"))
```

## Teaching Methodology

### Flipped Classroom Approach

**Part 1: Pre-Session Video (10-15 min, asynchronous)**
- Participants watch the video 2-3 days before the in-person session
- Covers analogy, keywords, patterns, and examples
- Includes screen recordings of actual Google Workspace tools
- Ends with a quick check question

**Part 2: In-Person Session (75 min, synchronous, hands-on)**
- Quick Q&A on video (5 min)
- Joint Discussion: Collaborative example (15 min)
- Audience Practice: Guided exercises (20 min)
- Contest Activity: Independent challenge (25 min)
- Wrap-up & Scoring (10 min)

### Gamification: Inter-Unit Competition

- Each unit earns points based on participant performance
- Scoring criteria: Completion, Accuracy, Independence
- Visible leaderboard tracks unit progress across all sessions
- Points accumulate across the entire training program

## Pre-Training Setup Checklist

Before the first RMU-1 session:

- [ ] Create a shared Google Drive folder for all RMU training materials
- [ ] Set up the template sheet (import CSV, apply formula, set up data validation)
- [ ] Test the control number formula with actual PSHS-MC data
- [ ] Prepare the leaderboard in Google Sheets with read-only access
- [ ] Set up a "RMU Help" channel in Google Chat for ongoing questions
- [ ] Record the pre-session video (10-15 minutes)
- [ ] Host the video on Google Drive and share the link 48 hours before the session
- [ ] Print quick reference cards (one per participant)
- [ ] Verify all participants have access to the PSHS Google Workspace domain
- [ ] Test the training room setup (projector, internet, participant computers)

## Post-Training Follow-Up

### Immediate (Within 1 Week)
- [ ] Collect feedback from participants
- [ ] Address any issues or questions
- [ ] Share the leaderboard update

### Short-Term (2-4 Weeks)
- [ ] Schedule a 15-minute check-in to address issues
- [ ] Verify that RMU is using the digital registry in daily operations
- [ ] Train additional RMU staff who didn't attend the session

### Long-Term (60 Days)
- [ ] Complete Training Effectiveness Form per FAM 4.7 Section 4.6
- [ ] Assess application on the job, efficiency gains, error reduction
- [ ] Identify additional training needs
- [ ] Schedule RMU-2 (Records Inventory, Disposition, and Electronic Records)

## Manual References

All materials reference **FAM 13.1 Records Management V2_Rev2**:
- Section 3.4b: Registry Sheet/Log Sheets requirements
- Section 3.7: Handling Electronic Records
- Section 3.15: File Classification and Coding System
- Section 4.2: Handling of Incoming Electronic Communications
- Section 4.6: Request of Inactive Records

## LibreOffice Integration

**Note:** LibreOffice is optional and will be deployed campus-wide before full training rollout.

### When LibreOffice is Available:
- Download Google Sheets as .ods (OpenDocument Spreadsheet)
- Work offline in LibreOffice Calc
- Re-upload to Google Drive when internet returns
- Use for weekly backup routine

## Support Resources

**For Google Sheets:**
- Help Center: sheets.google.com/support
- Press `?` in any Google Sheet for quick help

**For LibreOffice:**
- Help Center: help.libreoffice.org
- Press `F1` in LibreOffice for context help

**For PSHS Policies:**
- FAM 13.1 Records Management Manual
- Contact RMU Head or Records Officer

**For Technical Issues:**
- Contact ITU at `itu@pshs.edu.ph` (or your campus ITU email)

## Next Steps

After RMU-1 is approved and delivered:

1. **Build remaining Tier 1 sessions:**
   - Session 0 (Google Workspace Fundamentals)
   - LO-1 (LibreOffice as Offline Backup)
   - RHU-1 (Residence Hall Administration)
   - HSU-3 (Infectious Disease Monitoring)
   - GSU-2 (Facility Use Management)

2. **Await ACU system details** for ACU-1 and ACU-2

3. **Build Tier 2 sessions** with minor preparation

4. **Build Tier 3 sessions** with research

5. **Build Tier 4 sessions** requiring significant preparation

## Contact

For questions about these training materials, contact:
- Training Coordinator: [Name/Email]
- RMU Head: [Name/Email]

---

**Version:** 1.0
**Last Updated:** April 2026
**Status:** Ready for Review and Approval
