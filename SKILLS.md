# SKILLS.md — Team HQ Procedural Capabilities
<!-- Tier 2: At the Waterline (Progressive Disclosure / On-Demand Execution) -->

> **The Iceberg Principle**: This file houses structured, executable skills. Only read the relevant skill section when triggered by `AGENTS.md`. Do not keep all skills in active working memory simultaneously.

---

## Skill 1: `skill:hq-architecture`
**Description**: Layout design, component hierarchy, and the Page vs. Database decision engine.

### 1.1 The Page vs. Database Decision Heuristic
* **Create a Page when**:
  * The content is narrative, static, or orienting (e.g., Mission, Values, Directory).
  * It acts as a dashboard/portal aggregating multiple linked database views.
* **Create a Database when**:
  * Multiple items share identical metadata (dates, assignees, tags, status).
  * Items need different operational views (Kanban, Calendar, Table, Gallery).

### 1.2 Root Dashboard Blueprint (Two-Column Standard)
* **Header**: Page Title (`🏠 [Team Name] HQ`) + Cover + Icon (`🏛️`).
* **Mission Callout Block**:
  * Icon: 🎯
  * Text: High-level team mission + Current Quarter North Star goal.
* **Column 1 (Left - 30% width)**: Navigation & Culture
  * Quick Links (Slack, GitHub, Figma, Drive)
  * Team Norms & Meeting Cadences
  * Team Member Directory
* **Column 2 (Right - 70% width)**: Active Execution
  * Linked View: `✅ [HQ] Tasks` (Filter: `Assignee = "Me"` & `Status ≠ Done`)
  * Linked View: `🎯 [HQ] Projects` (Gallery View, Filter: `Status ≠ Completed`)
* **Footer (Full Width)**:
  * Linked View: `📚 [HQ] Knowledge Base` (List View, Filter: `Pinned = true`)
  * Toggle: `> 🗄️ Backend Databases (Do Not Edit Directly)`

---

## Skill 2: `skill:database-relations`
**Description**: Complete schema engineering, bidirectional relations, rollups, and self-referencing templates.

### 2.1 Backend Data Model
```
┌─────────────────────────────────┐
│       🎯 [HQ] Projects          │
├─────────────────────────────────┤
│ • Name (Title)                  │
│ • Status (Status)               │
│ • Owner (Person / Select)       │
│ • Timeline (Date Range)         │
│ • Priority (Select)             │
│ • Tasks (Relation ──┐           │
│ • Progress (Rollup) │           │
└─────────────────────┼───────────┘
                      │ (1-to-many bidirectional)
┌─────────────────────┼───────────┐
│ ✅ [HQ] Tasks       │           │
├─────────────────────┴───────────┤
│ • Name (Title)                  │
│ • Status (To Do, In Prog, Done) │
│ • Assignee (Person / Select)    │
│ • Due Date (Date)               │
│ • Priority (P1, P2, P3)         │
│ • Project (Relation ◄───────────┘
└─────────────────────────────────┘
```

### 2.2 The Self-Referencing Template Pattern
To automatically link tasks to a project upon creation:
1. Open `🎯 [HQ] Projects` ➔ Click `+ New template` ➔ Title: `Project Blueprint`.
2. Inside the template body, insert: `/linked view of database` ➔ Select `✅ [HQ] Tasks`.
3. Apply Filter: `Project` contains `Project Blueprint`.
4. *Result*: When a teammate creates a project using this template, Notion dynamically rewrites the filter so only tasks belonging to *that specific project* appear.

---

## Skill 3: `skill:sop-synthesis`
**Description**: Transforming raw meeting discussions or unstructured notes into formal Standard Operating Procedures (SOPs).

### 3.1 Standard SOP Specification
Every document added to `📚 [HQ] Knowledge Base` must strictly contain:
1. **Context & Objective**: Why this process exists (1-2 sentences).
2. **Owner & Review Cadence**: Who owns it and when it expires.
3. **Prerequisites / Access Requirements**: Tool accounts or permissions needed.
4. **Step-by-Step Execution**: Numbered steps with checklist items.
5. **Edge Cases & Troubleshooting**: What to do when something fails.

---

## Skill 4: `skill:weekly-maintenance`
**Description**: Automated health checks, stale doc flagging, and workspace pruning.

### 4.1 Knowledge Base Stale Doc Formula (Free-Tier Compatible)
Insert this formula property into `📚 [HQ] Knowledge Base`:
```javascript
if(dateBetween(now(), prop("Last Verified"), "days") > 90, "⚠️ Stale (Needs Audit)", "✅ Verified")
```

### 4.2 Monday Morning 15-Minute Triage Checklist
1. **Filter Stale Docs**: Open `📚 [HQ] Knowledge Base` filtered by `⚠️ Stale`. Ping owners to re-verify or archive.
2. **Prune Completed Tasks**: Set Tasks view filter: `Status is Done` and `Last edited time is before 1 week ago` ➔ Archive or hide from active boards.
3. **Verify Progress Rollups**: Inspect active projects with 0% progress or missed milestone dates.

---

## Skill 5: `skill:free-tier-optimization`
**Description**: Maximizing Notion's free plan without running into paywalls.

* **Block Limits**: Free plans have *unlimited blocks* for individual owners. If collaborating with more than 1 member on a free workspace, use **Guest Sharing** (Share -> Invite email as "Can edit" on specific root pages) instead of adding full paid workspace members.
* **Storage Limits**: 5MB file upload limit. Store large assets in Google Drive/Cloudflare R2 and embed clickable links.
* **Formulas & Rollups**: Use native 2.0 formulas instead of third-party automation tools (Make/Zapier) to save quota.
