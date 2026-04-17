# Google Workspace Training Curriculum for PSHS-MC Administrative Units

## Executive Summary

This document proposes a tailored Google Workspace (and LibreOffice backup) training curriculum for 10 administrative units at PSHS-MC. Each training session is designed to be **45 minutes to 1 hour 30 minutes**, directly tied to workflows documented in the PSHS System manuals (SSM, FAM, QM), and includes clear prerequisites.

The curriculum leverages the **Google Workspace Education Plus** license already paid for by the institution, maximizing ROI by replacing manual/paper-based processes with collaborative digital workflows. **LibreOffice** is introduced as an offline backup for continuity when internet is unavailable.

---

## Foundational Training (Required for All Units)

Before unit-specific sessions, all staff must complete a common foundational session. This ensures baseline competency across the organization.

### Session 0: Google Workspace Fundamentals
**Duration:** 1 hour 30 minutes  
**Audience:** ALL units (mandatory)  
**Prerequisites:** Basic computer literacy (can use a mouse, keyboard, and web browser)

**Topics:**
- Navigating the Google Workspace ecosystem (Gmail, Drive, Calendar, Docs, Sheets, Slides, Forms, Meet, Chat)
- PSHS email policies per FAM 12.2 (official use only, no personal/commercial accounts, prohibited services like Netflix/Shopee)
- Google Drive: folder structure, file upload, sharing permissions, organizing with stars and colors
- Gmail essentials: composing, replying, CC/BCC, attachments, labels, search
- Google Calendar: creating events, inviting attendees, setting reminders
- Google Chat vs Gmail: when to use which
- **LibreOffice equivalent overview:** LibreOffice Writer, Calc, and Impress as offline alternatives; saving and opening Google files in LibreOffice formats (.odt, .ods, .odp)

**Why this is critical:** FAM 12.2 Section 3.2 mandates that PSHS personnel use official PSHS email for all official communication. Section 3.2.9 requires coordination with ISA for email migration. Many staff may not be fully aware of these policies or the full suite available to them.

---

## Unit-Specific Training Sessions

---

### 1. Health Services Unit (HSU)

**Relevant Manuals:** SSM 6.1 (Health Screening Protocols During Enrolment), SSM 6.2 (Availment of Health Services), SSM 6.4 (Student Health Information), SSM 6.5 (Health Information Campaign), SSM 6.6 (Dental Examination), SSM 6.7 (Infectious Disease Monitoring)

**Forms Used:** Health History and Personal Data Sheet, Physical Examination Form, Dental Health Record, Clinic Admission Slip, Medical/Dental Consent Form, Infectious Disease Monitoring Tool

#### Session HSU-1: Digital Health Records and Patient Tracking
**Duration:** 1 hour 15 minutes  
**Prerequisites:** Session 0 (Google Workspace Fundamentals)

**Topics:**
- **Google Sheets** for patient consultation logging (replacing the manual Consultation Logbook cited in SSM 6.2 Section 4.1, Activity 7)
- Creating a structured patient intake tracker: date, patient name, type (student/employee/visitor), chief complaint, vital signs, disposition (sent back to class / kept for observation / sent home / referred to hospital)
- **Google Forms** for digital Clinic Admission Slips - auto-populating a spreadsheet
- Data validation and dropdown menus to standardize entries
- **LibreOffice Calc** equivalent: opening and editing Google Sheets offline, data entry in .ods format

**Why this is useful:** SSM 6.2 Section 4.1 requires nurses to log patients in a Consultation Logbook and update medical consultation records. A shared Google Sheet allows real-time tracking by both the Nurse and Physician, eliminating the risk of a single physical logbook being unavailable. The triage system described in Section 3.2.3 can be managed more efficiently with digital timestamps and disposition tracking.

#### Session HSU-2: Health Screening Workflow Automation
**Duration:** 1 hour  
**Prerequisites:** Session 0, HSU-1

**Topics:**
- **Google Forms** for digital Health History and Personal Data Sheet collection during enrollment (per SSM 6.1 Section 3.1)
- Pre-populating forms with student data from REG unit
- **Google Docs** templates for Medical Certificates and health findings reports
- **Google Sheets** for tracking health screening status of incoming Grade 7 and lateral entrants (SSM 6.1 Section 4.0 - tracking who has submitted CBC, urinalysis, fecalysis, HbsAg, HbsAb, chest X-ray)
- Conditional formatting to flag incomplete requirements (red for missing, green for complete)
- **Google Meet** for virtual follow-up consultations with parents/guardians (per SSM 6.2 Section 3.3.1 - parent notification)

**Why this is useful:** SSM 6.1 Section 4.0 describes a multi-step process where the Nurse receives, collates, and endorses health documents to the Physician. A shared Google Sheet with status tracking eliminates the need to physically pass documents back and forth. The Physician can review student health data before the physical checkup.

#### Session HSU-3: Infectious Disease Monitoring and Health Campaigns
**Duration:** 45 minutes  
**Prerequisites:** Session 0

**Topics:**
- **Google Sheets** for the Infectious Disease Monitoring Tool (SSM 6.7) - tracking cases, dates, status, follow-up
- Charts and pivot tables for disease surveillance dashboards
- **Google Slides** for Health Information Campaign materials (SSM 6.5)
- **Google Forms** for creating health awareness surveys
- **LibreOffice Impress** for offline presentation creation

**Why this is useful:** SSM 6.7 requires systematic monitoring of infectious diseases. A digital dashboard allows real-time visualization of disease trends, enabling faster response. Health campaigns per SSM 6.5 can be created collaboratively using Slides templates.

---

### 2. Library Unit (LIB)

**Relevant Manuals:** SSM 4.1 (Acquisition of Learning Resource Materials), SSM 4.2 (Technical Processing), SSM 4.3 (Use of Library), SSM 4.4 (Inventory and Weeding), SSM 4.5 (Maintenance of Library Resources)

**Forms Used:** Library Resources Recommendation Form, Library Card, Book Card, Weeding Form

#### Session LIB-1: Library Inventory and Circulation Management
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0

**Topics:**
- **Google Sheets** as a library catalog/inventory system: tracking book titles, accession numbers, categories, status (available/borrowed/overdue)
- Creating a borrowing/returning tracker with timestamps (replacing manual Library Card and Book Card system per SSM 4.3 Section 4.3.1)
- Using `VLOOKUP` and `FILTER` functions to quickly find books and check availability
- Conditional formatting for overdue books (SSM 4.3 Section 3.4.2 - overdue notification)
- **Google Forms** for Library Resources Recommendation Form (SSM 4.1 Section 5.1.2) - allowing teachers and students to submit recommendations digitally
- **LibreOffice Calc** for offline inventory work

**Why this is useful:** SSM 4.3 Section 4.3.1 describes a manual process using physical library cards and book cards. A shared Google Sheet allows instant searching, automatic overdue calculation, and eliminates physical card loss. SSM 4.1 Section 4.0 describes a 7-step selection process where teachers submit lists that the Librarian consolidates - Google Forms auto-consolidates submissions.

#### Session LIB-2: Digital Library Promotion and Resource Management
**Duration:** 1 hour  
**Prerequisites:** Session 0, LIB-1

**Topics:**
- **Google Sites** for a simple library webpage: services, hours, rules, new acquisitions
- **Google Slides** for library orientation presentations (SSM 4.3 Section 3.2)
- **Google Sheets** for weeding management (SSM 4.4) - tracking items recommended for removal with reasons
- **Google Docs** for creating library guides and resource access instructions
- **Google Forms** for the Suggestion Box (SSM 4.3 Section 3.3.1.3 - digital replacement)

**Why this is useful:** SSM 4.3 Section 3.3.1.3 mentions a physical suggestion box. A Google Form suggestion box is always accessible, automatically timestamped, and easily consolidated. A Google Sites page fulfills the orientation requirement of SSM 4.3 Section 3.2 and can be updated anytime.

---

### 3. Registration Unit (REG)

**Relevant Manuals:** SSM 3.1 (Campaign for NCE), SSM 3.2 (Admission of Incoming Grade 7 and Lateral Entry), SSM 3.3 (Year-End Clearance), SSM 3.4 (Enrolment of Grade 8-12), SSM 3.5 (Transfer Program), SSM 3.6 (Request for Records), SSM 3.7 (Scholarship Categorization)

**Forms Used:** 24+ forms including NCE Acknowledgement, Enrollment Checklists, Student Information Sheet, Affidavit of Guardianship, Year-End Clearance, Transfer Forms, Scholarship Forms, Student Record Request, Attendance Sheets, Class Admission Slip, NCE Campaign Form

#### Session REG-1: Digital Enrollment and Student Records Management
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0

**Topics:**
- **Google Forms** for digital enrollment checklists (SSM 3.2 - Grade 7/Lateral Entrants checklist, SSM 3.4 - Grade 8-12 checklist) with checkbox items for each requirement
- **Google Sheets** as a master enrollment tracker: student name, grade level, requirements submitted (with conditional formatting for incomplete items)
- Creating a Student Information Sheet digital equivalent using Google Forms
- Using `IMPORTRANGE` to pull data from multiple forms into a master dashboard
- **Google Docs** templates for correspondence (Letter of Request for Intercampus Transfer per SSM 3.5, Student Record Request responses per SSM 3.6)
- Mail merge using Google Sheets + Docs for bulk parent/guardian letters
- **LibreOffice Writer** mail merge as offline backup

**Why this is useful:** SSM 3.2 and 3.4 describe multi-step enrollment processes with extensive checklists. A digital enrollment tracker allows REG staff to see at a glance which students have incomplete requirements. The 24+ forms managed by this unit can be digitized, reducing physical storage needs and enabling instant search/retrieval. SSM 3.6 describes a records request process that can be initiated via Google Forms.

#### Session REG-2: Attendance Tracking and NCE Campaign Management
**Duration:** 1 hour  
**Prerequisites:** Session 0, REG-1

**Topics:**
- **Google Sheets** for Daily Attendance Sheet (PSHS-00-F-REG-19) and Attendance During Activities Sheet (PSHS-00-F-REG-20)
- Attendance tracking with automatic date stamping and summary formulas (`COUNTIF`, pivot tables)
- **Google Forms** for NCE Campaign coordination (SSM 3.1) - tracking school visits, applicant registrations
- **Google Slides** for NCE campaign presentations to prospective students
- **Google Meet** for virtual information sessions with prospective scholars
- **Google Sheets** for Record on Attendance and Punctuality (PSHS-00-F-REG-21)

**Why this is useful:** SSM 3.1 describes the NCE Campaign process involving scheduling and reporting. Digital tracking enables the REG unit to monitor campaign reach and effectiveness. Daily attendance tracking per SSM 3.4 can be automated with formulas that calculate totals and flag absences.

---

### 4. Residence Hall Unit (RHU)

**Relevant Manuals:** SSM 5.1 (Evaluation of Students Application for Residence Hall Accommodation), SSM 5.2 (Residence Hall Accommodation)

**Forms Used:** Residence Hall Application Form, Residence Hall Contract, Parent/Guardian Waiver, List of Appliances/Electrical Devices Form, Good Housekeeping Checklist, Residence Hall Student Leave Pass and Return Slip

#### Session RHU-1: Residence Hall Administration and Monitoring
**Duration:** 1 hour 15 minutes  
**Prerequisites:** Session 0

**Topics:**
- **Google Forms** for digital Residence Hall Application (SSM 5.1) - auto-populating a response spreadsheet
- **Google Sheets** for resident management: tracking occupants, room assignments, contract status, appliance declarations
- Conditional formatting for contract expiry dates and leave pass tracking
- **Google Docs** templates for Residence Hall Contracts and Parent/Guardian Waivers (SSM 5.2) with merge fields
- **Google Forms** for Good Housekeeping Checklist (digital inspection form per SSM 5.2)
- **Google Sheets** for Leave Pass and Return Slip tracking with timestamp-based monitoring
- **LibreOffice Writer** for contract printing when offline

**Why this is useful:** SSM 5.1 describes an evaluation process for residence hall applications. A Google Form application allows 24/7 submission and automatic consolidation. SSM 5.2 requires contract management and monitoring - a shared spreadsheet enables multiple staff to track resident status simultaneously. The Good Housekeeping Checklist can be completed on a tablet during inspections.

---

### 5. General Services Unit (GSU)

**Relevant Manuals:** FAM 6.1 (Request for Services), FAM 6.2 (Use of Vehicle, Facilities and Equipment), FAM 6.3 (Janitorial Services), FAM 6.4 (Preventive Maintenance), FAM 6.5 (Corrective Maintenance), FAM 6.6 (Security Services)

**Forms Used:** Request for Services, Permit to Use School Facilities, Permit to Use School Vehicle, Cleaning Checklist, Preventive Maintenance Schedule, Equipment History Card, Preventive Maintenance Checklist, Work Request Form, Security Guard Work Performance Evaluation Form, Janitorial Performance Evaluation Form, Pre-repair Inspection Report

#### Session GSU-1: Service Request and Maintenance Tracking
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0

**Topics:**
- **Google Forms** for digital Request for Services (FAM 6.1 - reproduction, security, janitorial requests) with approval workflow
- **Google Sheets** as a service request tracker: request number, date, type, requester, status, assigned personnel, completion date
- **Google Sheets** for Preventive Maintenance Schedule (FAM 6.4) with recurring date formulas and conditional formatting for upcoming/due/overdue maintenance
- Equipment History Card as a digital record per equipment (FAM 6.4 Section 3.5)
- **Google Forms** for Work Request Form and Pre-repair Inspection Report (FAM 6.5)
- Using Google Sheets charts for maintenance analytics
- **LibreOffice Calc** for offline maintenance schedule management

**Why this is useful:** FAM 6.1 requires a record book for reproduction and service requests. A digital tracker provides instant search, filtering, and automated reference numbering. FAM 6.4 Section 3.5 requires regular updating of Preventive Maintenance Checklists and Equipment History Cards - a shared spreadsheet ensures all stakeholders see the latest status. FAM 6.5 describes corrective maintenance workflows that benefit from digital tracking of work requests from submission to completion.

#### Session GSU-2: Facility Use Management and Performance Evaluation
**Duration:** 1 hour  
**Prerequisites:** Session 0, GSU-1

**Topics:**
- **Google Calendar** for facility and vehicle booking (FAM 6.2) - shared calendars for different facilities and vehicles
- **Google Forms** for Permit to Use School Facilities and Permit to Use School Vehicle
- **Google Sheets** for Security Guard and Janitorial Performance Evaluation (FAM 6.3, FAM 6.6) - scoring rubrics with automatic calculation
- **Google Sheets** for Cleaning Checklist tracking with date stamps
- **Google Docs** for creating standard operating procedures and evaluation reports

**Why this is useful:** FAM 6.2 describes the process for requesting use of school facilities and vehicles. A shared Google Calendar provides real-time visibility into facility/vehicle availability, preventing double-booking. Performance evaluations per FAM 6.3 and 6.6 can use Google Sheets with built-in formulas to automatically compute weighted scores.

---

### 6. Human Resources Unit (HRU)

**Relevant Manuals:** FAM 4.1 (Recruitment, Selection and Placement), FAM 4.3 (Career Pathing), FAM 4.5 (Strategic Performance Management System), FAM 4.7 (Training and Development), FAM 4.8 (Employee Benefits), FAM 4.15 (Personnel Records Management), FAM 4.17 (Request for Records)

**Forms Used:** Background Investigation/Verification Form, Structured Interview Questionnaire, Personnel Action Request Form, Teaching Demonstration Form, Orientation Checklist, Training/Workshop/Activity Evaluation Form, Training Effectiveness Form, Monthly Summary of Attendance, Service Credit Form, Clearance from Property and Money Accountabilities, Personnel Record Request Form, Speaker/Topic Evaluation Form, Teaching Overload Computation

#### Session HRU-1: Recruitment and Applicant Tracking
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0

**Topics:**
- **Google Sheets** as an Applicant Tracking System: applicant name, position applied, education, eligibility, experience, training, status (received/shortlisted/interviewed/demo teaching/background check/appointed/rejected)
- Evaluation Summary Table template (FAM 4.1 Section 5.1.3) with weighted scoring formulas for Faculty (Educational Qualification 25%, Teaching Competencies 55%, Personality 10%, Experience 5%, Training 5%) and Admin positions
- **Google Forms** for pre-assessment/shortlisting questionnaire
- **Google Docs** templates for Shortlisted Candidates Form, Request for Publication of Vacant Positions
- **Google Sheets** for tracking publication/posting compliance with RA 7041 (10 calendar days)
- **LibreOffice Calc** for offline scoring computation

**Why this is useful:** FAM 4.1 describes an 18-step recruitment process involving multiple stakeholders (HRMO, FSB/HRMPSB, Campus Director, BOT). A shared Google Sheet allows all committee members to view applicant status in real-time. The Evaluation Summary Table with built-in weighted scoring formulas eliminates manual computation errors. Tracking publication dates ensures compliance with RA 7041.

#### Session HRU-2: Training Management and Employee Records
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0, HRU-1

**Topics:**
- **Google Sheets** for Training Master Plan (FAM 4.7 Section 3.8) - annual training calendar with employee names, training programs, schedule, budget, status
- **Google Forms** for Training Needs Assessment Survey (FAM 4.7 Section 4.2, Activity 1)
- **Google Forms** for Training/Workshop/Activity Evaluation Form and Speaker/Topic Evaluation Form (FAM 4.7 Section 5.1.5-5.1.6)
- **Google Sheets** for Training Effectiveness tracking (FAM 4.7 Section 4.6) - pre/post assessment comparison
- **Google Sheets** for Monthly Summary of Attendance (PSHS-00-F-HRU-22)
- **Google Forms** for Personnel Record Request (FAM 4.17) - digital request form
- **Google Docs** templates for Orientation Checklist (FAM 4.7 Section 4.1)
- **Google Sheets** for Teaching Overload Computation with built-in formulas

**Why this is useful:** FAM 4.7 Section 3.8 requires a Training Master Plan updated monthly. A shared Google Sheet serves as the living document. Training evaluation forms (Section 3.9) can be distributed via Google Forms for instant collation. The Training Effectiveness Form (Section 4.6) requires follow-up 2 months after training - Google Sheets with date-based conditional formatting can automate reminders.

#### Session HRU-3: Attendance Tracking and Performance Management
**Duration:** 1 hour  
**Prerequisites:** Session 0

**Topics:**
- **Google Sheets** for Monthly Summary of Attendance with formulas for undertime, tardiness, leaves, service credits
- **Google Forms** for leave applications, overtime authority requests
- **Google Sheets** for IPCR/DPCR tracking and consolidation (FAM 4.5 SPMS)
- **Google Docs** templates for Personnel Action Request Forms
- **Google Calendar** for tracking employee probationary/contract dates, PDS updates, SALN submission deadlines

**Why this is useful:** FAM 4.5 requires a Strategic Performance Management System. Digital tracking of attendance and performance commitments enables HRU to generate reports on demand rather than manually compiling physical records.

---

### 7. Information Technology Unit (ITU)

**Relevant Manuals:** FAM 12.1 (Online Publication), FAM 12.2 (Information Technology Management), FAM 12.3 (Backup and Recovery), FAM 12.4 (Device Lending Policy)

**Forms Used:** IT Job Request Form, Contract of Agreement, Preventive Maintenance Schedule, Equipment History Card

#### Session ITU-1: IT Service Management and Google Workspace Administration
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0, familiarity with Google Workspace admin concepts

**Topics:**
- **Google Sheets** for IT Job Request tracking (FAM 12.2 Section 4.1) - request ID, date, user, equipment, issue, status, assigned to, resolution date
- **Google Forms** for digital IT Job Request Form submission
- **Google Workspace Admin Console** overview: user management, email account creation/migration (FAM 12.2 Section 3.2.2 - ISA authority to create email accounts)
- **Google Sheets** for IT Equipment Inventory (FAM 12.2 Section 3.6.1) with equipment history tracking
- **Google Drive** shared drives for centralized software installers, drivers, and documentation
- **Google Keep** for quick technical notes and troubleshooting checklists
- **Google Sites** for an internal IT knowledge base / FAQ page
- **LibreOffice** deployment considerations: compatibility with Google formats, batch installation

**Why this is useful:** FAM 12.2 describes comprehensive IT management responsibilities including email account management, equipment inventory, and maintenance tracking. A digital IT Job Request system enables users to submit requests 24/7 and allows ITU to prioritize and track resolution. The Equipment History Card (Section 4.1, Activity 1.4) can be maintained as a digital record per equipment, accessible to all ITU staff.

#### Session ITU-2: Backup, Recovery, and Security Practices
**Duration:** 1 hour  
**Prerequisites:** Session 0, ITU-1

**Topics:**
- **Google Drive** for backup and recovery (FAM 12.3) - shared drives, version history, trash recovery
- **Google Takeout** for data export and archival
- Google Workspace security features: 2-step verification enforcement, password policies, audit logs
- **Google Sheets** for Device Lending tracking (FAM 12.4) - borrower, device, date issued, expected return, condition
- **Google Apps Script** introduction: automating email notifications for overdue equipment, scheduled maintenance reminders
- **LibreOffice** as offline contingency: configuring LibreOffice to default save in Google-compatible formats, setting up auto-save

**Why this is useful:** FAM 12.3 requires backup and recovery procedures for digital files. Google Drive's version history and shared drives provide institutional-level backup. FAM 12.4 requires tracking of lent devices - a digital tracker with automated email reminders ensures timely returns. Apps Script can automate many routine notifications described in the manual workflows.

---

### 8. Procurement Unit (PRU)

**Relevant Manuals:** FAM 5.1 (Procurement Process), FAM 5.2 (Requisition and Issuance), FAM 5.3 (Receipt, Inspection, Acceptance), FAM 5.4 (Storage, Safekeeping and Inventory), FAM 5.5 (Disposal), FAM 5.6 (Lost, Stolen, Damaged Property), FAM 5.7 (Evaluation of External Providers)

**Forms Used:** Request for Quotation, Abstract of Quotation, External Provider Performance Evaluation Form

#### Session PRU-1: Procurement Tracking and Quotation Management
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0

**Topics:**
- **Google Sheets** as a Purchase Request (PR) tracker: PR number, date, requesting unit, items, PPMP reference, mode of procurement, status (received/verified/approved/bidding/awarded/delivered)
- Tracking the 55+ step procurement process (FAM 5.1 Section 4.2-4.5) with status dropdowns and date stamps
- **Google Sheets** for Abstract of Quotations (FAM 5.1 Section 5.1.2) with automatic lowest-bid highlighting using `MIN` formula
- **Google Docs** templates for Request for Quotations, BAC Resolutions, Notices
- **Google Drive** shared folders for procurement documents organized by PR number
- **Google Sheets** for Annual Procurement Plan (APP) monitoring and Procurement Monitoring Reports (FAM 5.1 Section 4.6 - Forms 1-3)
- **LibreOffice Calc** for offline quotation comparison and abstract preparation

**Why this is useful:** FAM 5.1 describes one of the most complex processes in the institution, spanning up to 55 steps for public bidding. A shared Google Sheet tracker provides real-time visibility to PRU, BAC, end-users, and management. The Abstract of Quotations with automatic lowest-bid calculation reduces manual comparison errors. Procurement Monitoring Reports (Section 4.6) can be generated directly from the tracker.

#### Session PRU-2: External Provider Evaluation and Document Management
**Duration:** 1 hour  
**Prerequisites:** Session 0, PRU-1

**Topics:**
- **Google Forms** for External Provider Performance Evaluation (FAM 5.7) - digital evaluation with scoring rubrics
- **Google Sheets** for provider database: company name, contact details, categories, performance scores, blacklists
- **Google Docs** templates for contracts, purchase orders, notices of award
- **Google Drive** folder structure for organized procurement documentation per fiscal year
- **Google Sheets** for PhilGEPS posting tracker and compliance monitoring
- **LibreOffice Writer** for contract and document preparation offline

**Why this is useful:** FAM 5.7 requires systematic evaluation of external providers. Digital evaluation forms with automatic scoring standardize the assessment process. A provider database enables quick lookup of past performance during procurement activities.

---

### 9. Accounting Unit (ACU)

**Relevant Manuals:** FAM 8.1 (Budget Preparation), FAM 8.2 (Budget Execution, Monitoring and Reporting), FAM 9.1 (Disbursement Process), FAM 9.2 (Payroll and Remittances), FAM 9.3 (Cash Advance), FAM 9.4 (Financial Reporting), FAM 9.5 (Bank Reconciliation), FAM 10.1 (Petty Cash Fund), FAM 10.2 (Preparation and Release of Payments), FAM 10.3 (Collection and Deposit), FAM 11.0 (Consolidation and Submission of Financial Reports)

**Forms Used:** Authority to Claim

#### Session ACU-1: Financial Tracking and Reporting with Google Sheets
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0, intermediate spreadsheet skills (basic formulas, cell formatting)

**Topics:**
- **Google Sheets** for budget tracking: allotment, obligations, balances per line item (FAM 8.1-8.2)
- Advanced formulas: `SUMIFS`, `VLOOKUP`, `QUERY` for financial data analysis
- **Google Sheets** for disbursement tracking (FAM 9.1): DV number, payee, amount, purpose, status, ORS reference, check number
- Pivot tables for monthly/quarterly financial summaries
- **Google Sheets** for Bank Reconciliation (FAM 9.5): bank balance vs book balance, outstanding checks, deposits in transit
- **Google Sheets** for Petty Cash Fund monitoring (FAM 10.1): date, item, amount, running balance, replenishment tracking
- **Google Sheets** charts for Financial Reporting dashboards (FAM 9.4)
- **LibreOffice Calc** for offline financial work, including pivot tables and advanced functions

**Why this is useful:** FAM 9.1-11.0 describe extensive financial tracking and reporting requirements. Google Sheets with built-in formulas can automate running balances, bank reconciliation computations, and budget utilization monitoring. FAM 9.4 requires financial reporting - charts and pivot tables enable visual dashboards for management decision-making. The 3% HRD budget allocation per FAM 4.7 Section 3.13 can be tracked automatically.

#### Session ACU-2: Payment Processing and Collection Management
**Duration:** 1 hour  
**Prerequisites:** Session 0, ACU-1

**Topics:**
- **Google Sheets** for Payment preparation and release tracking (FAM 10.2): tracking from obligation to check release
- **Google Sheets** for Collection and Deposit monitoring (FAM 10.3): date, source, amount, OR number, deposit date, bank reference
- **Google Forms** for Authority to Claim digital submission
- **Google Docs** templates for financial certificates and transmittal documents
- **Google Sheets** for Cash Advance monitoring (FAM 9.3): grantee, purpose, amount, liquidation status, outstanding balance
- Conditional formatting for aging of unliquidated cash advances

**Why this is useful:** FAM 10.2 and 10.3 describe payment and collection processes that generate numerous tracking records. Digital tracking enables instant status queries and automated aging reports for unliquidated cash advances. FAM 9.3 requires monitoring of cash advances - conditional formatting can flag aging advances that need follow-up.

---

### 10. Records Management Unit (RMU)

**Relevant Manuals:** FAM 13.1 (Records Management), FAM 13.2 (Messengerial/Courier Services)

**Forms Used:** Routing Slip, Records Requisition and Acknowledgement Slip, Request for Transfer of Inactive Records, Request for Messengerial Services, Transmittal Slip

#### Session RMU-1: Digital Records Tracking and Mail Management
**Duration:** 1 hour 30 minutes  
**Prerequisites:** Session 0

**Topics:**
- **Google Sheets** as a digital logbook/registry (FAM 13.1 Section 3.4b): date received, control number, source/sender, subject, date released, assigned office, remarks
- Auto-generating document control numbers using Google Sheets formulas (FAM 13.1 Section 3.4b - format: year-month-series, e.g., 2026-04-100)
- **Google Sheets** for Routing Slip tracking (FAM 13.1 Section 4.2): document number, routing sequence, action taken per office
- **Google Forms** for Records Requisition and Acknowledgement Slip (FAM 13.1 Section 4.6)
- **Google Forms** for Request for Messengerial Services (FAM 13.2)
- **Google Sheets** for Transmittal Slip tracking with delivery confirmation
- **Google Drive** folder structure mirroring the Filing Chart system (FAM 13.1 Section 3.15)
- **LibreOffice Writer** for offline document preparation and printing

**Why this is useful:** FAM 13.1 Section 3.4b requires maintaining a logbook with specific fields (date, control number, source, subject, etc.). A Google Sheet provides instant search, filtering by date range or sender, and eliminates the risk of a single physical logbook being damaged or unavailable. Auto-generated control numbers ensure consistency. The routing process described in Section 4.2 can be tracked digitally so any office can check where a document is in the routing chain.

#### Session RMU-2: Records Inventory, Disposition, and Electronic Records
**Duration:** 1 hour  
**Prerequisites:** Session 0, RMU-1

**Topics:**
- **Google Sheets** for Records Inventory and Appraisal (FAM 13.1 Section 3.9): record type, location, retention period, disposal date, status
- Conditional formatting for records approaching disposal dates
- **Google Sheets** for Records Disposition Schedule tracking (FAM 13.1 Section 3.11-3.12)
- **Google Drive** for electronic records storage: folder hierarchy matching filing charts, access control
- **Google Forms** for Request for Transfer of Inactive Records (FAM 13.1 Section 4.6)
- **Google Docs** for certified copy templates (FAM 13.1 Section 3.8)
- **Google Sheets** for tracking electronic communications received and printed (FAM 13.1 Section 3.7)
- **LibreOffice** for accessing and printing records offline

**Why this is useful:** FAM 13.1 Section 3.9 requires annual inventory of records. A digital inventory tracker enables continuous monitoring rather than a once-a-year manual count. Section 3.11-3.12 describes retention and disposition - conditional formatting can automatically highlight records due for disposal. Section 3.7 specifically addresses electronic records handling, which aligns perfectly with Google Drive storage.

---

## LibreOffice Offline Backup Sessions

### Supplemental Session LO-1: LibreOffice as Offline Backup
**Duration:** 1 hour  
**Audience:** All units (recommended)  
**Prerequisites:** Session 0

**Topics:**
- Installing LibreOffice (free, open-source)
- LibreOffice Writer: creating documents, opening .docx and Google Docs files, saving in multiple formats
- LibreOffice Calc: spreadsheets, opening .xlsx and Google Sheets files, basic formulas
- LibreOffice Impress: presentations, opening .pptx and Google Slides files
- Saving Google Workspace files for offline use: File > Download as .odt/.ods/.odp
- Setting up LibreOffice to default save in Microsoft-compatible formats if needed
- Workflow: work offline in LibreOffice > upload to Google Drive when internet returns
- Using Google Drive desktop app for offline file access

**Why this is useful:** PSHS-MC may experience internet outages, and Microsoft Office licenses may not always be available. LibreOffice provides a free, legal alternative that can open and save in formats compatible with both Microsoft Office and Google Workspace. This ensures business continuity regardless of internet or budget status.

---

## Curriculum Summary Matrix

| Unit | Session ID | Session Title | Duration | Prerequisites |
|------|-----------|---------------|----------|---------------|
| ALL | Session 0 | Google Workspace Fundamentals | 1h 30m | Basic computer literacy |
| HSU | HSU-1 | Digital Health Records and Patient Tracking | 1h 15m | Session 0 |
| HSU | HSU-2 | Health Screening Workflow Automation | 1h 00m | Session 0, HSU-1 |
| HSU | HSU-3 | Infectious Disease Monitoring and Health Campaigns | 0h 45m | Session 0 |
| LIB | LIB-1 | Library Inventory and Circulation Management | 1h 30m | Session 0 |
| LIB | LIB-2 | Digital Library Promotion and Resource Management | 1h 00m | Session 0, LIB-1 |
| REG | REG-1 | Digital Enrollment and Student Records Management | 1h 30m | Session 0 |
| REG | REG-2 | Attendance Tracking and NCE Campaign Management | 1h 00m | Session 0, REG-1 |
| RHU | RHU-1 | Residence Hall Administration and Monitoring | 1h 15m | Session 0 |
| GSU | GSU-1 | Service Request and Maintenance Tracking | 1h 30m | Session 0 |
| GSU | GSU-2 | Facility Use Management and Performance Evaluation | 1h 00m | Session 0, GSU-1 |
| HRU | HRU-1 | Recruitment and Applicant Tracking | 1h 30m | Session 0 |
| HRU | HRU-2 | Training Management and Employee Records | 1h 30m | Session 0, HRU-1 |
| HRU | HRU-3 | Attendance Tracking and Performance Management | 1h 00m | Session 0 |
| ITU | ITU-1 | IT Service Management and Google Workspace Administration | 1h 30m | Session 0 |
| ITU | ITU-2 | Backup, Recovery, and Security Practices | 1h 00m | Session 0, ITU-1 |
| PRU | PRU-1 | Procurement Tracking and Quotation Management | 1h 30m | Session 0 |
| PRU | PRU-2 | External Provider Evaluation and Document Management | 1h 00m | Session 0, PRU-1 |
| ACU | ACU-1 | Financial Tracking and Reporting with Google Sheets | 1h 30m | Session 0, intermediate sheets skills |
| ACU | ACU-2 | Payment Processing and Collection Management | 1h 00m | Session 0, ACU-1 |
| RMU | RMU-1 | Digital Records Tracking and Mail Management | 1h 30m | Session 0 |
| RMU | RMU-2 | Records Inventory, Disposition, and Electronic Records | 1h 00m | Session 0, RMU-1 |
| ALL | LO-1 | LibreOffice as Offline Backup | 1h 00m | Session 0 |

**Total Sessions:** 23 (including foundational and LibreOffice)  
**Total Training Hours:** approximately 26 hours across all units

---

## Recommended Implementation Sequence

1. **Phase 1 - Foundation:** Session 0 for all staff + LO-1 (LibreOffice)
2. **Phase 2 - High-Impact Units First:** ITU (they become internal champions), RMU (records management benefits everyone), HRU (training management supports the rest of the program)
3. **Phase 3 - Transaction-Heavy Units:** REG, PRU, ACU, GSU
4. **Phase 4 - Service Units:** HSU, LIB, RHU

---

## Teaching Methodology: Flipped Classroom + Gamification

### Flipped Classroom Approach

Each session is split into two parts:

**Part 1: Pre-Session Video ("I Do" — asynchronous, 10-15 minutes)**
- Trainer records the analogy, keywords, patterns, and examples
- Video is sent to participants 2-3 days before the in-person session
- Participants can watch, pause, rewind, and rewatch as many times as needed
- Video includes screen recordings of the actual Google Workspace tools
- Video ends with a "quick check" question to verify understanding

**Part 2: In-Person Session ("We Do" + "You Do" — synchronous, 45min-1hr15min)**
- Quick Q&A on the video content (5 min)
- Joint Discussion: Collaborative example using actual unit data (15 min)
- Audience Practice: Participants work through guided exercises (20 min)
- Contest Activity: Independent challenge to cement learning (10-20 min)

### Why Flipped Classroom Works Here
- Participants can absorb the conceptual part at their own pace
- In-person time is maximized for hands-on practice (the most valuable part)
- Reduces pressure on slower learners — they can rewatch the video
- Faster learners can skip ahead or watch once
- The trainer's time is spent on the highest-value activity: coaching

### Gamification: Inter-Unit Competition

**Mechanics:**
- Each unit earns points based on how many staff members can successfully and independently complete the "You Do" contest activity
- Scoring criteria: Completion (did they finish?), Accuracy (is it correct?), Independence (did they need help?), Speed (how fast?)
- A visible leaderboard tracks unit progress across all sessions
- Points accumulate across the entire training program

**Prizes (tie to FAM 4.9 — Rewards and Recognition):**
- Top-performing unit gets recognized at a campus event
- Individual high performers can be nominated for PSHS rewards
- Bragging rights and a small token (e.g., "Most Digitized Unit" certificate)

**Why This Works:**
- Creates healthy competition and peer support within units
- Motivates practice outside of training hours
- Aligns with the existing PSHS Rewards and Recognition framework (FAM 4.9)
- Generates natural "champions" in each unit who can help others

### Session Materials Structure

Each session produces 4 deliverables stored in `/trainings/`:

1. **Trainer Guide** (`SESSION-ID_trainer-guide.md`) — Full script with timing, talking points, analogies, exercises, and answer keys
2. **Pre-Session Video Script** (`SESSION-ID_video-script.md`) — Word-for-word script for the 10-15 minute recorded lesson, with slide/screen recording cues
3. **Hands-On Exercise File** (`SESSION-ID_exercise.md`) — Step-by-step exercise using actual unit forms and data, with screenshots
4. **Quick Reference Card** (`SESSION-ID_quick-ref-card.md`) — Front-and-back PDF card: Side A = step-by-step walkthrough of the most common task, Side B = shortcuts, tips, and "where to find help"

### Assessment and Certification

Per FAM 4.7 Section 3.9, a Training Effectiveness Form shall be accomplished to assess the impact of each training. This curriculum recommends:
- **Pre-training assessment:** Brief self-assessment of Google Workspace familiarity (before watching the video)
- **Post-training assessment:** The contest activity itself serves as the practical assessment
- **60-day follow-up:** Training Effectiveness Form (per FAM 4.7 Section 4.6) to assess on-the-job application
