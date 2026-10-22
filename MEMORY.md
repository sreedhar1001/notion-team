# MEMORY.md — Team HQ Persistent Memory & State
<!-- Tier 3: Deep Below the Waterline (Submerged / Persistent Long-Term Memory) -->

> **The Iceberg Principle**: This file contains persistent facts, Architectural Decision Records (ADRs), state tracking, and lessons learned. It prevents agent amnesia across sessions. Agents consult this file to verify past decisions or update ongoing workspace state.

---

## 1. System Invariants & Environment
- **Platform**: Notion (Web / Desktop App).
- **Plan Tier**: Notion Free Plan ($0/month).
- **Core User Archetype**: Startup / Student Club / Non-Profit / Agile Engineering Team.
- **Root Entity**: `🏠 [Team Name] HQ` (Single root page).
- **Backend Architecture**: Decoupled 3-Database Triad (`Projects`, `Tasks`, `Knowledge Base`).

---

## 2. Architecture Decision Records (ADRs)

### ADR-001: The 3-Database Triad vs. Monolithic Database
- **Context**: Could we combine Projects, Tasks, and Knowledge Base into one large database with a "Type" select property?
- **Decision**: **Rejected**. Separate them into 3 distinct databases.
- **Rationale**: 
  1. Tasks require granular assignees, fast Kanban filtering, and daily due dates.
  2. Projects require date ranges, high-level ownership, and rollup progress calculations.
  3. Knowledge Base requires doc categories, health audit formulas, and verification tags.
  4. Combining them degrades performance and clutters property lists in Notion's free tier.

### ADR-002: Backend Database Isolation in a Collapsed Toggle
- **Context**: Where should the raw databases live?
- **Decision**: Inside a collapsed toggle `> 🗄️ Backend Databases (Do Not Move)` at the bottom of the root HQ page.
- **Rationale**: Users should only interact with curated, filtered Linked Database Views on the main dashboard. Leaving raw databases exposed invites accidental property deletion or broken relations.

### ADR-003: Bidirectional Project-Task Relation with Self-Referencing Templates
- **Context**: How do teammates create tasks within a project without manually tagging the project every time?
- **Decision**: Use a bidirectional relation paired with a Notion Self-Referencing Template filter (`Project contains [Current Template Name]`).
- **Rationale**: Completely eliminates manual data entry errors. Any task created inside the project page automatically inherits that project's relation.

### ADR-004: 90-Day Stale Document Health Formula
- **Context**: Team knowledge bases quickly become obsolete and untrusted.
- **Decision**: Implement a native date formula triggering a `⚠️ Stale` warning if `Last Verified` is older than 90 days.
- **Rationale**: Lowers the barrier to maintenance. The team doesn't have to read every doc—they just filter the list for `⚠️ Stale` once a month.

---

## 3. Entity Topology & Current State

```yaml
Workspace_State:
  Root_Page: "🏠 [Team Name] HQ"
  Backend_Databases:
    - name: "🎯 [HQ] Projects"
      status: "Defined"
      properties: ["Name", "Status", "Owner", "Timeline", "Priority", "Category", "Tasks (Relation)", "Progress (Rollup)"]
    - name: "✅ [HQ] Tasks"
      status: "Defined"
      properties: ["Name", "Status", "Assignee", "Due Date", "Priority", "Project (Relation)"]
    - name: "📚 [HQ] Knowledge Base"
      status: "Defined"
      properties: ["Doc Title", "Category", "Owner", "Last Verified", "Health (Formula)", "Pinned (Checkbox)"]
  Front_End_Views:
    - "My Tasks (Board View: Filtered by Assignee = Me & Status != Done)"
    - "Due Today / Overdue (List View: Filtered by Due Date <= Today)"
    - "Active Projects (Gallery / Table View: Filtered by Status != Completed)"
    - "Pinned Resources (List View: Filtered by Pinned = True)"
```

---

## 4. Anti-Patterns & Learned Nuances

| Anti-Pattern | Why It Breaks | Enforced Rule |
| :--- | :--- | :--- |
| **Nesting pages inside tasks** | Content gets lost, search index explodes, unmanageable permissions. | All docs live in `📚 Knowledge Base`; tasks link to docs via relation or URL. |
| **Unassigned / No-Date Tasks** | Tasks become an infinite, demoralizing backlog graveyard. | Every task must have an `Assignee` and a `Due Date` before moving to `In Progress`. |
| **Over-nesting pages (> 2 levels)** | Teammates suffer navigation fatigue and ask "Where does this live?" | Maximum 2 levels of hierarchy: Root HQ ➔ Section / Database ➔ Item. |
| **Circular Relations** | Linking Project A ➔ Project B ➔ Project A breaks rollup calculations. | Strictly 1-to-many relationship: 1 Project contains many Tasks. |

---

## 5. Session Trajectory & Change Log
- **Session 1 (2026-10-22)**:
  - Initialized Iceberg framework for Notion Team HQ.
  - Deployed `AGENTS.md` (Operational Charter & Personas).
  - Deployed `SKILLS.md` (Procedural Schemas & Architecture).
  - Deployed `MEMORY.md` (ADRs & Invariant State).
  - Generated deterministic workflows in `WORKFLOWS.md`.
  - Created Notion AI prompt templates in `NOTION_AI_TEMPLATES.md`.
  - Integrated `TAVILY_API_KEY` for live web-grounded research and verified API connectivity.
  - Built autonomous engine `team_hq_builder.py` and interactive web application `app.py`.
  - Generated production workspace export in `build_output/`.
