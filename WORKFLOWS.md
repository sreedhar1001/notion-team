# WORKFLOWS.md — Deterministic Execution Playbooks
<!-- Operational Runbooks: Step-by-Step Execution Protocols -->

This document contains step-by-step playbooks for building, maintaining, and automating the Notion Team HQ.

---

## Playbook WF-01: Zero-to-One HQ Bootstrapping (30-Minute Build)

```
[Create Root Page] ➔ [Build Backend Databases] ➔ [Configure Relations] ➔ [Build Front-End Dashboard] ➔ [Seed Data]
```

### Step 1: Root Initialization
1. In your Notion workspace, click **Add a page** in the sidebar.
2. Title the page: `🏠 [Team Name] HQ`.
3. Add an icon (🏛️) and a clean cover image.
4. Add a full-width **Callout block** (`/callout`):
   ```markdown
   🎯 **Our Mission**: [Insert 1-sentence team mission statement]
   ⚡ **Q4 North Star**: [Insert primary quarterly metric or deliverable]
   ```

### Step 2: Backend Database Isolation
1. Scroll to the bottom of the page and create a Toggle List (`/toggle`).
2. Label it: `> 🗄️ Backend Databases (Do Not Move or Delete)`.
3. Inside the toggle, type `/database full page` to create each of the 3 databases:
   - `🎯 [HQ] Projects`
   - `✅ [HQ] Tasks`
   - `📚 [HQ] Knowledge Base`

### Step 3: Schema & Relation Configuration
1. In `🎯 [HQ] Projects`, add properties:
   - `Status` (Status: `Not Started`, `In Progress`, `On Hold`, `Completed`)
   - `Owner` (Person / Select)
   - `Timeline` (Date range)
   - `Priority` (Select: `🔴 P1`, `🟡 P2`, `🟢 P3`)
   - `Relation` ➔ Connect to `✅ [HQ] Tasks` (Enable "Show on [HQ] Tasks")
   - `Progress` (Rollup: Relation `Tasks`, Property `Status`, Calculate `Percent per group -> Done`)

2. In `✅ [HQ] Tasks`, add properties:
   - `Status` (Status: `To Do`, `In Progress`, `Blocked`, `Done`)
   - `Assignee` (Person / Select)
   - `Due Date` (Date)
   - `Priority` (Select: `High`, `Medium`, `Low`)
   - Ensure the `Project` relation column is visible.

3. In `📚 [HQ] Knowledge Base`, add properties:
   - `Category` (Select: `📘 SOP`, `⚖️ Policy`, `💡 Spec`, `🛠️ Tools`)
   - `Owner` (Person)
   - `Last Verified` (Date)
   - `Health` (Formula: `if(dateBetween(now(), prop("Last Verified"), "days") > 90, "⚠️ Stale", "✅ Verified")`)
   - `Pinned` (Checkbox)

### Step 4: Front-End Dashboard Assembly
On the root page (above the toggle):
1. Create a 2-column layout (`/2col`).
2. **Left Column (~30%)**:
   - `### 🧭 Team Norms & Quick Links`
   - Links to Slack channels, Shared Drive, Meeting schedules.
3. **Right Column (~70%)**:
   - `/linked view of database` ➔ Select `✅ [HQ] Tasks`.
   - **Tab 1: My Active Tasks** (Board View, Grouped by `Status`, Filter: `Assignee = "Me"` & `Status ≠ Done`).
   - **Tab 2: Overdue / Due Today** (List View, Filter: `Due Date is on or before today` & `Status ≠ Done`).
4. **Bottom Full-Width Section**:
   - `/linked view of database` ➔ Select `🎯 [HQ] Projects` (Gallery View, Filter: `Status ≠ Completed`).
   - `/linked view of database` ➔ Select `📚 [HQ] Knowledge Base` (List View, Filter: `Pinned is checked`).

---

## Playbook WF-02: Self-Referencing Project Template Deployment

Deploy this template once, and every future project will automatically manage its own child tasks:

1. Open `🎯 [HQ] Projects`.
2. Click the dropdown arrow next to **New** ➔ Select **+ New template**.
3. Set Title to: `New Project Blueprint`.
4. In the page body, add:
   ```markdown
   ## 🎯 Project Overview
   - **Objective**: What problem does this solve?
   - **Success Metrics**: How do we measure completion?
   - **Key Stakeholders**: Who needs to be consulted?

   ---
   ## 📋 Project Deliverables & Tasks
   ```
5. Below the heading, type `/linked view of database` ➔ select `✅ [HQ] Tasks`.
6. Click **Filter** ➔ Select `Project` ➔ Choose `New Project Blueprint`.
7. Return to the database, click the dropdown next to **New**, click `...` next to `New Project Blueprint`, and select **Set as default for all views**.

---

## Playbook WF-03: The 15-Minute Monday Morning AI Triage

Execute this every Monday at 9:00 AM:

1. **Step 1 (Stale Doc Check)**:
   - Open `📚 [HQ] Knowledge Base` with view filtered to `Health contains ⚠️ Stale`.
   - If stale docs exist: Mention owner in a comment asking to confirm accuracy or archive.
2. **Step 2 (Weekly Task Prune)**:
   - In `✅ [HQ] Tasks`, filter by `Status is Done` and `Due Date is before last week`.
   - Move to archive or ensure the board filter hides `Done` tasks.
3. **Step 3 (Milestone Review)**:
   - Review `🎯 [HQ] Projects` Rollup progress bars.
   - For any project behind schedule, ping the owner for a blocker status update.
