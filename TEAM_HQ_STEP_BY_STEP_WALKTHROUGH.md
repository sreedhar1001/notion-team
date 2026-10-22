# Team HQ Master Walkthrough & Execution Guide
A complete implementation guide following the 5-part Notion Team HQ curriculum.

---

## Part I: Design Your Team HQ

### 1. Concrete Team Scenario (HyperScale AI)
* **Team Size**: 6 people.
* **Roles**: 
  - Founder & Product Lead
  - Technical Lead (Full-stack / Infrastructure)
  - AI Research / Prompt Engineer
  - Operations & Growth Lead
* **The 3 Most Common Teammate Questions**:
  1. *"What is the top priority for this sprint, and what does 'done' look like?"*
  2. *"Where is the official procedure for X (deploying, onboarding, spending money)?"*
  3. *"Who owns this deliverable, and is it on track for the target date?"*

### 2. Notion AI Planning Prompt (Pre-filled)
Copy and paste this into a fresh Notion page chat:

```markdown
I'm designing a Team HQ in Notion for HyperScale AI, an early-stage developer tools startup. The team is 6 people (Product Lead, Tech Lead, AI Engineer, and Ops/Growth). Help me plan before I build:

1. Who will use this HQ, and what will they come looking for each week?
2. What 4–6 core sections does it need?
3. For each section, what's the one thing it must answer at a glance?

Keep it short: a plan I can build from, not a full build.
```

### 3. The Resulting 5 Core Sections Plan
1. **🧭 Company Front Door**: Answers *"Why do we exist and what is this month's North Star?"*
2. **🎯 Current Priorities & Projects**: Answers *"What are we shipping right now, and when?"*
3. **✅ My Tasks Hub**: Answers *"What is on my plate today?"*
4. **📚 Knowledge Base (Docs)**: Answers *"Where is the single source of truth for our processes and policies?"*
5. **🔄 Operating Rhythms & Norms**: Answers *"How do we communicate and stay aligned without meeting overload?"*

---

## Part II: Build the Company Home

### 1. Notion AI Chat Prompt to Generate Company Home
Paste this into the chat on your root page:

```markdown
Turn this page into the Company Home for HyperScale AI. Add:

- A short mission statement at the top: "Empower developers to build and deploy autonomous agent workflows in minutes."
- A "Current priorities" section with our top 3 priorities:
  1. Launch V1 Agent SDK Public Beta
  2. Complete 5 Enterprise Pilot Integrations
  3. Implement Zero-Downtime Telemetry & Monitoring
- An "Announcements" section with one sample announcement: "🚀 Sprint 14 ships Friday at 3 PM! All PRs must be merged by 12 PM."
- A "Team norms" section with 4 working agreements:
  1. Default to public, asynchronous documentation over private direct messages.
  2. Standups are 15 minutes hard stop; blockers go to offline threads.
  3. No meetings on Focus Wednesdays.
  4. Every document must have a single DRI (Directly Responsible Individual).
- A "Key links" section I'll fill in as I build the rest of the HQ (Slack, GitHub, Figma, Docs DB).

Keep it clean, scannable, and modern.
```

### 2. Page Styling
- **Page Title**: `🏛️ HyperScale AI — Team HQ`
- **Icon**: `🏛️`
- **Cover Image**: Minimalist abstract or gradient cover.
- Set page width to **Full width** in the page menu (`...` top right).

---

## Part III: Create the Knowledge Base ("Docs")

### 1. Database Configuration
Create a full-page or inline database called **`Docs`**.

| Property Name | Property Type | Options / Configuration |
| :--- | :--- | :--- |
| **Name** | Title | Document Title |
| **Type** | Select | `📘 Process`, `⚖️ Policy`, `👋 Onboarding`, `💡 Decision`, `📖 Reference` |
| **Status** | Status | `Draft`, `Active`, `Needs Review`, `Archived` |
| **Owner** | Person (or Select) | Teammate responsible for keeping it accurate |
| **Last edited time** | Last edited time | *System property (updates automatically)* |

### 2. 6 Realistic Sample Docs Pre-populated

| Document Title | Type | Status | Owner | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Engineering PR & Git Workflow** | `📘 Process` | `Active` | Tech Lead | Branch naming, code review SLA, CI/CD checks |
| **New Teammate 30-Day Onboarding** | `👋 Onboarding` | `Active` | Ops Lead | Software logins, buddy assignment, first PR |
| **ADR-004: Postgres vs DynamoDB** | `💡 Decision` | `Active` | Tech Lead | Architectural decision record for state store |
| **Expense & Travel Reimbursement** | `⚖️ Policy` | `Active` | Ops Lead | Stipends, receipt upload rules, \$250 limit |
| **Incident Response & Pager Duty** | `📘 Process` | `Needs Review`| Tech Lead | Severity matrix, war room protocol, post-mortem |
| **Production API Endpoints Reference** | `📖 Reference`| `Active` | AI Engineer | Base URLs, rate limits, authentication tokens |

### 3. Page Templates to Create

#### Template A: Process Doc
- **Title**: `[Process] New Standard Procedure`
- **Body Content**:
  ```markdown
  ## 1. Overview & Goal
  What does this procedure achieve, and when should it be run?

  ## 2. Prerequisites & Permissions
  What accounts, API keys, or tools are required before starting?

  ## 3. Step-by-Step Instructions
  - [ ] Step 1: Initialize the environment.
  - [ ] Step 2: Run verification scripts.
  - [ ] Step 3: Document outcomes in the parent project.

  ## 4. Troubleshooting
  Common failure modes and how to resolve them.
  ```

#### Template B: Decision Record (ADR)
- **Title**: `[ADR-00X] Title of Decision`
- **Body Content**:
  ```markdown
  ## Status
  Proposed / Accepted / Superseded

  ## Context & Problem Statement
  What issue are we solving? What constraints exist?

  ## Considered Options
  1. Option A (Pros / Cons)
  2. Option B (Pros / Cons)

  ## Decision & Rationale
  Which option did we choose, and why?

  ## Consequences
  What becomes easier or harder as a result of this decision?
  ```

### 4. Database Views
- **View 1 (Default)**: Table grouped by **Type**.
- **View 2**: "Audit / Stale Docs" sorted by **Last edited time** (Oldest first), filtered to `Status = Needs Review`.

---

## Part IV: Connect Projects and Tasks

### 1. Database Schema

#### `Projects` Database
- **Name** (Title)
- **Status** (Status: `Planning`, `In Progress`, `On Hold`, `Done`)
- **Owner** (Person / Select)
- **Target Date** (Date)
- **Priority** (Select: `🔴 High`, `🟡 Medium`, `🟢 Low`)
- **What done looks like** (Text): 1-sentence definition of completion.
- **Tasks** (Relation: 2-way connect to `Tasks`)

#### `Tasks` Database
- **Name** (Title)
- **Status** (Status: `To Do`, `Doing`, `Done`)
- **Assignee** (Person / Select)
- **Due Date** (Date)
- **Project** (Relation: 2-way connect to `Projects`)

### 2. Sample Data (3 Projects with 3-4 Tasks Each)

```
🎯 Project 1: Launch V1 Agent SDK
   ├── Status: In Progress | Owner: Tech Lead | Target Date: Nov 15
   ├── What done looks like: Python & TypeScript packages published to PyPI & npm with 95% test coverage.
   ├── [Task 1.1] Write TypeScript SDK bindings (Assignee: Tech Lead | Due: Nov 2 | Done)
   ├── [Task 1.2] Implement retry exponential backoff (Assignee: AI Engineer | Due: Nov 7 | Doing)
   └── [Task 1.3] Publish quickstart documentation (Assignee: Product Lead | Due: Nov 12 | To Do)

🎯 Project 2: Q4 Enterprise Pilots
   ├── Status: In Progress | Owner: Ops Lead | Target Date: Nov 30
   ├── What done looks like: 5 pilot contracts signed with active telemetry pipeline verified.
   ├── [Task 2.1] Draft pilot security agreement & DPA (Assignee: Ops Lead | Due: Nov 5 | Doing)
   ├── [Task 2.2] Schedule technical onboarding calls (Assignee: Ops Lead | Due: Nov 10 | To Do)
   └── [Task 2.3] Build custom webhook export demo (Assignee: Tech Lead | Due: Nov 18 | To Do)

🎯 Project 3: Automated Monitoring & Alerting
   ├── Status: Planning | Owner: Tech Lead | Target Date: Dec 15
   ├── What done looks like: PagerDuty alerts wired to Slack #alerts with <2 min latency.
   ├── [Task 3.1] Evaluate Datadog vs Grafana Cloud (Assignee: Tech Lead | Due: Nov 20 | To Do)
   └── [Task 3.2] Configure synthetic uptime probes (Assignee: AI Engineer | Due: Nov 28 | To Do)
```

### 3. Front-End Dashboard Integration
On the Company Home page under **Current priorities**:
1. Type `/linked view of database`.
2. Select **Projects**.
3. Filter: `Status = In Progress`.
4. Display properties: `Owner`, `Target Date`, `Priority`, `What done looks like`.

---

## Part V: Add AI and Operating Rhythms

### 1. Maintenance Checklists on Company Home
Add this toggle or callout block to the bottom of Company Home:

```markdown
## 🔄 Operating Rhythm

### ⏱️ Weekly Check-in (15 min — Every Monday 9:30 AM)
- [ ] Update active project statuses and upcoming target dates.
- [ ] Post one announcement in Company Home with this week's focus.
- [ ] Clear any documents in Docs marked "Needs Review".
- [ ] Archive tasks completed last sprint.

### 📅 Monthly Alignment (30 min — Last Friday of the Month)
- [ ] Archive finished projects and outdated docs.
- [ ] Review Team Norms and Current Priorities. (Are they still accurate?)
- [ ] Run the Notion AI Stale Content Audit.
```

### 2. Notion AI Maintenance Prompts (Ready to Run)

#### Prompt 1: Priority Cross-Reference Query
```markdown
Search my Team HQ and answer: what are our current priorities, and which projects support each one? Cite the pages you used.
```

#### Prompt 2: Stale Content & Unowned Items Audit
```markdown
Look through the Docs and Projects databases in my Team HQ. List anything that looks stale, unowned, or missing — docs with no owner or in "needs review", projects past their target date, statuses that haven't moved. Suggest what to update first.
```

---

## Final Step: Publish Your Team HQ

1. At the top right of your Company Home page, click **Share**.
2. Switch to the **Publish** tab.
3. Click the blue **Publish to web** button.
4. *(Optional)* Turn on **Allow duplicate as template** so team members, advisors, or peers can duplicate your setup.
5. Click **View site** to copy your public link!
