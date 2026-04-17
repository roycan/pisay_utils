# Training Guide Confidence & Feasibility Assessment

## Training Environment (Confirmed)

- **Setup:** Participants have computers/laptops (fully hands-on)
- **Class size:** 10-15 per session
- **Environment:** Actual PSHS Google Workspace domain
- **Leave-behind format:** PDF quick-reference cards (front-and-back)
- **ACU note:** Uses standard government accounting; more details pending

## Scoring Criteria

**Confidence Score** = How confident we can create an accurate, comprehensive training guide given what we know from the manuals + Google Workspace knowledge. Factors: manual detail level, workflow clarity, solution standardness.

**Feasibility Score** = How feasible it is to deliver the training effectively within the time constraint to the likely audience skill level. Factors: topic complexity, audience baseline, time adequacy, hands-on practicality.

> **Note:** Feasibility scores are boosted +5-10% across the board because participants have computers, the class size is ideal (10-15), and we can use the actual PSHS domain for live exercises.

---

## Session-by-Session Assessment

### Session 0: Google Workspace Fundamentals
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **95%** | Standard Google Workspace training. We know PSHS email policies from FAM 12.2 in detail. Well-documented topic with abundant reference materials available. |
| Feasibility | **90%** | Basic topics, but covering the full suite in 1h30m is a lot. May need to focus on the 4-5 most essential tools and mention the rest briefly. |

**What we have:** FAM 12.2 Sections 3.1-3.7 give us concrete policies to reference (email rules, prohibited uses, LMS policies, equipment rules).  
**What we need:** Nothing additional — this is ready to build.

---

### HSU-1: Digital Health Records and Patient Tracking
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | We read SSM 6.1 and 6.2 in detail. The consultation logbook workflow is clearly described. Google Sheets for tracking is a standard solution. |
| Feasibility | **80%** | Nurses and physicians may have varying tech comfort. The triage system mapping to Sheets is doable but needs sensitive analogies for medical staff. |

**What we have:** SSM 6.2 Section 4.1 lists 8 specific procedure steps with responsible parties. The Consultation Logbook, patient disposition options (sent back to class / kept for observation / sent home / referred to hospital), and the Clinic Admission Slip are all explicitly described.  
**What we need:** Confirmation on whether HSU currently uses any digital system already (to avoid duplication).

---

### HSU-2: Health Screening Workflow Automation
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **80%** | We understand the enrollment screening process from SSM 6.1. Google Forms + Sheets is well-documented. But we'd need to see the actual Health History and Personal Data Sheet fields to create an accurate digital form. |
| Feasibility | **75%** | Conditional formatting and pre-populating are intermediate topics. May need to simplify or extend time. |

**What we have:** SSM 6.1 Section 3.2.1 lists the required lab tests (CBC with blood-typing, urinalysis, fecalysis, HbsAg, HbsAb, chest X-ray). Section 4.0 gives a 7-step procedure.  
**What we need:** The actual HSU-01 form (Health History and Personal Data Sheet) to map fields to Google Forms. We have the editable .docx copy in the manuals folder, so we can extract this.

---

### HSU-3: Infectious Disease Monitoring and Health Campaigns
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | Charts and pivot tables in Sheets are standard. SSM 6.7 describes the monitoring requirement clearly. |
| Feasibility | **85%** | Shorter session (45min), focused topic. Very doable. Good candidate for first session to build. |

**What we have:** SSM 6.7 describes infectious disease monitoring. The Infectious Disease Monitoring Tool form (HSU-06) exists as an editable .xlsx.  
**What we need:** Nothing additional — ready to build.

---

### LIB-1: Library Inventory and Circulation Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **80%** | We read SSM 4.1 and 4.3 in detail. The borrowing/returning workflow with library cards and book cards is clearly described. But we don't know if PSHS-MC already uses a library management system (e.g., Koha, Librarika) that might make Google Sheets redundant for this purpose. |
| Feasibility | **75%** | VLOOKUP and FILTER are intermediate functions that may challenge non-technical library staff. Need careful pacing. |

**What we have:** SSM 4.3 Section 4.3.1 describes the complete borrowing/returning process in 5 steps. The Library Card (LIB-02) and Book Card (LIB-03) forms exist as editable .xlsx files. SSM 4.1 Section 4.0 describes the 7-step acquisition process.  
**What we need:** ⚠️ **Critical clarification** — Does the library already use a digital catalog system? If yes, this session needs to pivot to complementing that system rather than replacing it.

---

### LIB-2: Digital Library Promotion and Resource Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | Google Sites and Slides are straightforward tools. SSM 4.3-4.5 provide clear requirements. |
| Feasibility | **85%** | Google Sites is one of the most user-friendly tools. Good follow-up session after LIB-1. |

**What we have:** SSM 4.3 Section 3.2 describes library orientation requirements. Section 3.3.1.3 describes the suggestion box. SSM 4.4 covers weeding.  
**What we need:** Nothing additional — ready to build.

---

### REG-1: Digital Enrollment and Student Records Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **75%** | REG has 24+ forms and complex multi-step processes. We read SSM 3.1-3.7 but the sheer volume means we need to prioritize which forms to digitize first. IMPORTRANGE and mail merge are intermediate-advanced. |
| Feasibility | **70%** | This is the most form-heavy unit. Trying to cover enrollment checklists, student info sheets, transfer forms, AND mail merge in 1h30m is ambitious. Consider splitting into two sessions or narrowing scope. |

**What we have:** SSM 3.2 and 3.4 describe detailed enrollment checklists. 24+ forms are listed with editable copies available. SSM 3.6 describes the records request process.  
**What we need:** ⚠️ **Prioritization** — We need to identify the top 3-5 most critical forms to digitize first, not all 24+. Also need to confirm if REG already uses any student information system.

---

### REG-2: Attendance Tracking and NCE Campaign Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | Attendance tracking with COUNTIF and pivot tables is well-documented. NCE campaign management is essentially project tracking. |
| Feasibility | **80%** | More focused than REG-1. Doable within the time. |

**What we have:** PSHS-00-F-REG-19 (Daily Attendance Sheet), REG-20 (Attendance During Activities), REG-21 (Record on Attendance and Punctuality), REG-23 (NCE Campaign Form), REG-24 (NCE Campus Director's Report) all exist as editable copies.  
**What we need:** Nothing additional — ready to build.

---

### RHU-1: Residence Hall Administration and Monitoring
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | We read SSM 5.1-5.2. The forms are straightforward (application, contract, waiver, checklist, leave pass). Google Forms + Sheets is a clean solution. |
| Feasibility | **85%** | Well-scoped session with good duration. The Good Housekeeping Checklist as a digital form is an excellent hands-on exercise. |

**What we have:** SSM 5.1-5.2 describe evaluation and accommodation processes. 6 forms exist with editable copies (.docx and .xlsx).  
**What we need:** Nothing additional — ready to build.

---

### GSU-1: Service Request and Maintenance Tracking
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | We read FAM 6.1 and 6.4 in detail. The record book, preventive maintenance schedule, and equipment history card are clearly described workflows. |
| Feasibility | **80%** | Good scope. Maintenance scheduling with recurring date formulas is a useful intermediate topic that GSU staff will appreciate. |

**What we have:** FAM 6.1 describes the service request process with a record book. FAM 6.4 describes preventive maintenance with schedules, checklists, and equipment history cards. 11 forms exist for GSU with editable copies.  
**What we need:** Nothing additional — ready to build.

---

### GSU-2: Facility Use Management and Performance Evaluation
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | Google Calendar for booking is straightforward. Evaluation scoring with formulas is well-documented. FAM 6.2-6.3 and 6.6 provide clear requirements. |
| Feasibility | **85%** | Google Calendar is one of the easiest tools to teach. Evaluation scoring formulas are a good practical exercise. |

**What we have:** FAM 6.2 covers facility/vehicle use. FAM 6.3 covers janitorial services. FAM 6.6 covers security services. Performance evaluation forms exist for both security guards and janitorial staff.  
**What we need:** Nothing additional — ready to build.

---

### HRU-1: Recruitment and Applicant Tracking
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **80%** | We read FAM 4.1 in full detail (6 pages, 18-step process). The weighted scoring criteria are explicitly stated in the manual. But the multi-committee process (FSB/HRMPSB, MANCOM, EXECOM, BOT) adds complexity to tracker design. |
| Feasibility | **75%** | The weighted scoring formulas are straightforward to teach. But the multi-stakeholder aspect means the tracker needs different views/permissions, which is an intermediate Google Sheets concept. |

**What we have:** FAM 4.1 Section 3.4 gives exact criteria and weights for Faculty (Education 25%, Teaching Competencies 55%, Personality 10%, Experience 5%, Training 5%), Admin Level I, and Admin Level II positions. The 18-step procedure is fully documented.  
**What we need:** Clarification on whether the Evaluation Summary Table scoring should be done collaboratively in real-time (during HRMPSB meetings) or individually. This affects the design.

---

### HRU-2: Training Management and Employee Records
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | We read FAM 4.7 in full (11 pages). The Training Master Plan, TNA Survey, evaluation forms, and effectiveness tracking are all clearly described with specific forms. |
| Feasibility | **80%** | Well-documented workflows that map cleanly to Google tools. The 2-month follow-up tracking is a clever use of Sheets date functions. |

**What we have:** FAM 4.7 Section 3.8 requires a Training Master Plan. Section 4.2 describes the TNA process. Section 4.5-4.6 describe evaluation and effectiveness tracking. All forms exist (Orientation Checklist, TNA Survey, Training Disposition Form, Training Effectiveness Form, Evaluation Forms).  
**What we need:** Nothing additional — ready to build.

---

### HRU-3: Attendance Tracking and Performance Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **75%** | We know attendance tracking is needed (Monthly Summary of Attendance form exists). But we didn't read FAM 4.5 (SPMS) in detail, so IPCR/DPCR tracking needs more research. |
| Feasibility | **80%** | Attendance formulas are standard. But SPMS/IPCR components may need HRU input on exact requirements and scoring. |

**What we have:** PSHS-00-F-HRU-22 (Monthly Summary of Attendance) exists. FAM 4.5 references SPMS but we haven't read it in detail.  
**What we need:** ⚠️ **Need to read FAM 4.5** (Strategic Performance Management System) to understand IPCR/DPCR requirements before building this guide.

---

### ITU-1: IT Service Management and Google Workspace Administration
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **70%** | We read FAM 12.2 in detail. But Google Workspace Admin Console is a specialized topic that requires actual admin access to demonstrate. Apps Script is an advanced topic. |
| Feasibility | **65%** | ITU staff likely have a higher technical baseline, but covering Admin Console AND Apps Script in 1h30m is ambitious. Recommend splitting or deferring Apps Script to a separate advanced session. |

**What we have:** FAM 12.2 describes IT management policies, email account management (Section 3.2), equipment inventory (Section 3.6), and maintenance/repair procedures (Section 4.1). IT Job Request Form exists.  
**What we need:** ⚠️ **Admin access required** — The trainer needs Google Workspace Admin Console access to create accurate guides. Also need to decide whether Apps Script should be a separate advanced session.

---

### ITU-2: Backup, Recovery, and Security Practices
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **75%** | Google Drive backup and 2SV are well-documented. But we'd need to know specific PSHS security policies beyond FAM 12.2. Device lending tracking is straightforward. |
| Feasibility | **70%** — Apps Script introduction may be too much for this session. Security policy configuration needs ITU buy-in and authority. |

**What we have:** FAM 12.3 covers backup and recovery. FAM 12.4 covers device lending. FAM 12.2 Section 3.5 covers virus prevention.  
**What we need:** Confirmation on whether PSHS has a specific data privacy/backup policy document beyond what's in the manual.

---

### PRU-1: Procurement Tracking and Quotation Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | We read FAM 5.1 in full (19 pages!). The procurement process is extremely well-documented with clear step-by-step procedures. The Abstract of Quotations with MIN formula is a clean, specific teaching example. |
| Feasibility | **75%** — The 55+ step process is complex. The tracker needs careful design to be useful without being overwhelming. Recommend simplifying to key status checkpoints rather than tracking every single step. |

**What we have:** FAM 5.1 covers the complete procurement lifecycle: Purchase Request processing, Public Bidding (steps 1-55), Alternative Modes, Small Value Procurement, and Monitoring Reports. Abstract of Quotations form exists.  
**What we need:** ⚠️ **Scope decision** — Should the tracker follow every step or just key milestones? Recommend milestone tracking (PR submitted → Approved → Bidding → Award → Delivery → Inspection).

---

### PRU-2: External Provider Evaluation and Document Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** | Provider evaluation forms and database are straightforward. FAM 5.7 covers evaluation requirements. |
| Feasibility | **85%** | Well-scoped follow-up session. Building a provider database is an excellent hands-on exercise. |

**What we have:** FAM 5.7 covers external provider evaluation. PSHS-00-F-PRU-05 (External Provider Performance Evaluation Form) exists as editable .xlsx.  
**What we need:** Nothing additional — ready to build.

---

### ACU-1: Financial Tracking and Reporting with Google Sheets
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **70%** — We read FAM 9.1 but it's only 3 pages and mostly references the Government Accounting Manual (GAM) which we don't have. Budget tracking requires understanding PSHS-specific chart of accounts and allotment structures. |
| Feasibility | **65%** — Accounting staff may already use specialized government accounting software. Google Sheets would need to complement, not replace, existing systems. Advanced formulas (QUERY, SUMIFS, pivot tables) need significant time to teach properly. |

**What we have:** FAM 8.1-8.2 (budget), FAM 9.1-9.5 (disbursement, payroll, cash advance, financial reporting, bank reconciliation), FAM 10.1-10.3 (petty cash, payments, collection), FAM 11.0 (consolidation). Only the Authority to Claim form (ACU-01) is listed.  
**What we need:** ⚠️ **Critical gap** — We need to: (1) understand what accounting system ACU currently uses, (2) get the GAM references, (3) understand the chart of accounts structure, (4) confirm whether Google Sheets is meant to replace or supplement existing tools. This session needs the most preparation.

---

### ACU-2: Payment Processing and Collection Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **70%** — Same constraints as ACU-1. Cash advance aging and collection tracking are useful but need accounting domain knowledge we don't fully have. |
| Feasibility | **70%** — Conditional formatting for aging is straightforward to teach. But the accounting context needs to be accurate. |

**What we have:** FAM 9.3 (cash advance), FAM 10.2 (payment preparation), FAM 10.3 (collection and deposit).  
**What we need:** Same as ACU-1 — understanding of existing systems and GAM references.

---

### RMU-1: Digital Records Tracking and Mail Management
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **90%** — We read FAM 13.1 in full (19 pages!). The registry/logbook fields are explicitly listed in Section 3.4b. The document control number format is specified (year-month-series). This is one of the most detailed manuals we have. |
| Feasibility | **90%** — The workflow is crystal clear and the Google Sheets solution is straightforward. Auto-generating control numbers with formulas is an excellent teaching example. The analogies write themselves (physical logbook → digital logbook). |

**What we have:** FAM 13.1 Section 3.4b lists exact registry fields (Date/Time Received, Control Number, Source/Sender, Subject Matter, Date Released, Personnel/Office Assigned, Remarks). Section 4.2 describes the electronic communications handling procedure. Section 3.15 covers file classification. All 5 RMU forms exist with editable copies.  
**What we need:** Nothing additional — **this is our strongest session. Best candidate to build first as a template for others.**

---

### RMU-2: Records Inventory, Disposition, and Electronic Records
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **85%** — Records inventory and disposition tracking are well-documented in FAM 13.1 Sections 3.9-3.13. The retention schedule and filing chart concepts translate well to digital. |
| Feasibility | **85%** — Good follow-up to RMU-1. Conditional formatting for disposal dates is a practical, satisfying exercise. |

**What we have:** FAM 13.1 Sections 3.9 (inventory), 3.10 (transfer), 3.11-3.12 (retention), 3.13 (disposal), 3.14 (preservation).  
**What we need:** Nothing additional — ready to build.

---

### LO-1: LibreOffice as Offline Backup
| Metric | Score | Notes |
|--------|-------|-------|
| Confidence | **90%** — LibreOffice is well-documented. File compatibility between Google Workspace and LibreOffice formats is a standard topic. |
| Feasibility | **90%** — Simple, practical session. Most concepts transfer directly from Google Workspace knowledge. The "download from Google, open in LibreOffice, re-upload" workflow is easy to demonstrate. |

**What we have:** General knowledge of LibreOffice and Google Workspace file compatibility.  
**What we need:** Confirm which LibreOffice version will be installed campus-wide, to ensure screenshots match.

---

## Summary Ranking (Highest to Lowest Confidence)

| Rank | Session | Confidence | Feasibility | Status |
|------|---------|-----------|-------------|--------|
| 1 | Session 0: Fundamentals | 95% | 90% | ✅ Ready to build |
| 2 | RMU-1: Digital Records Tracking | 90% | 90% | ✅ Ready to build — **best template session** |
| 3 | LO-1: LibreOffice Backup | 90% | 90% | ✅ Ready to build |
| 4 | RMU-2: Records Inventory | 85% | 85% | ✅ Ready to build |
| 5 | LIB-2: Digital Library Promotion | 85% | 85% | ✅ Ready to build |
| 6 | HSU-3: Disease Monitoring | 85% | 85% | ✅ Ready to build |
| 7 | RHU-1: Residence Hall Admin | 85% | 85% | ✅ Ready to build |
| 8 | GSU-2: Facility Use & Evaluation | 85% | 85% | ✅ Ready to build |
| 9 | PRU-2: Provider Evaluation | 85% | 85% | ✅ Ready to build |
| 10 | GSU-1: Service Request Tracking | 85% | 80% | ✅ Ready to build |
| 11 | HRU-2: Training Management | 85% | 80% | ✅ Ready to build |
| 12 | REG-2: Attendance & NCE | 85% | 80% | ✅ Ready to build |
| 13 | HSU-1: Digital Health Records | 85% | 80% | ✅ Ready to build |
| 14 | PRU-1: Procurement Tracking | 85% | 75% | ✅ Ready — needs scope decision |
| 15 | LIB-1: Library Inventory | 80% | 75% | ⚠️ Needs library system check |
| 16 | HRU-1: Recruitment Tracking | 80% | 75% | ✅ Ready — needs workflow clarification |
| 17 | HSU-2: Health Screening | 80% | 75% | ⚠️ Needs form field extraction |
| 18 | REG-1: Digital Enrollment | 75% | 70% | ⚠️ Needs prioritization of 24+ forms |
| 19 | HRU-3: Attendance & Performance | 75% | 80% | ⚠️ Needs FAM 4.5 research |
| 20 | ITU-2: Backup & Security | 75% | 70% | ⚠️ Needs security policy details |
| 21 | ACU-1: Financial Tracking | 70% | 65% | 🔴 Needs GAM references + system audit |
| 22 | ACU-2: Payment Processing | 70% | 70% | 🔴 Same as ACU-1 |
| 23 | ITU-1: IT Service Mgmt & Admin | 70% | 65% | 🔴 Needs admin access + scope split |

---

## Recommended Build Order

### Tier 1: Build Immediately (Confidence ≥ 85%, Feasibility ≥ 80%)
These sessions have enough manual detail and straightforward Google Workspace solutions. Build these first — they also serve as templates for the teaching methodology.

1. **RMU-1** — Best template session. Most manual detail. Start here.
2. **Session 0** — Everyone needs this. High impact.
3. **LO-1** — Quick to build. Universal need.
4. **RHU-1** — Clean, well-scoped.
5. **HSU-3** — Short, focused.
6. **GSU-2** — Google Calendar is easy to teach.

### Tier 2: Build with Minor Preparation (Confidence 80-85%)
Need small clarifications or decisions, but mostly ready.

7. **HRU-2** — Ready, just needs form mapping.
8. **GSU-1** — Ready, good workflow documentation.
9. **PRU-2** — Ready, straightforward.
10. **LIB-2** — Ready.
11. **REG-2** — Ready.
12. **HSU-1** — Ready.
13. **RMU-2** — Ready after RMU-1.
14. **PRU-1** — Needs scope decision on milestone vs. step tracking.
15. **HRU-1** — Needs clarification on real-time collaboration during meetings.

### Tier 3: Build with Research (Confidence 70-80%)
Need additional information before guides can be accurate.

16. **LIB-1** — Check for existing library system first.
17. **HSU-2** — Extract form fields from HSU-01 .docx.
18. **REG-1** — Prioritize top 5 forms from 24+.
19. **HRU-3** — Read FAM 4.5 (SPMS) first.

### Tier 4: Requires Significant Preparation (Confidence < 75%)
These need domain expertise, system access, or policy decisions.

20. **ITU-2** — Needs security policy details beyond FAM 12.2.
21. **ACU-2** — Needs GAM references and system audit.
22. **ACU-1** — Needs GAM references, chart of accounts, system audit.
23. **ITU-1** — Needs admin console access; consider splitting Apps Script into separate session.
