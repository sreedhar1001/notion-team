# 🏛️ HyperScale AI — Team HQ

> **🎯 Mission**: Build the single operating system for autonomous agents and developer tooling.  
> **⚡ Current North Star**: Ship V1 public beta with 1,000 active developers and 99.9% uptime.  
> **💡 Operating Model Research**: For an Early-Stage AI Startup, the best practices for Notion team HQ workspace structure include enforcing a small set of top-level spaces, assigning one owner per top-level space to prevent drift, and using databases instead of folders. The workspace should have a clear hierarchy with a company home linking to spaces like Product, Operations, People, and Knowledge base. Archive rather than delete and review permissions quarterly to maintain security. For AI Developer Infrastructure & Autonomous Agents OKRs norms, the sources suggest starting with a clear hierarchy and using Notion AI to draft documents, build databases, and search across connected tools to save time and improve efficiency.

---

## 🧭 Team Orientation & Norms
| Protocol | Channel / Cadence | Responsible Owner | Rule of Engagement |
| :--- | :--- | :--- | :--- |
| **Daily Check-in** | Slack #daily-standup | All Team Members | Post top 3 priorities by 10:00 AM (Async). |
| **Sprint Planning** | Zoom / Notion | Product & Eng Lead | Bi-weekly on Mondays, 10:30 AM - 11:15 AM. |
| **All-Hands Sync** | Main Stage | Leadership | Every Friday at 4:30 PM with live Q&A. |
| **Documentation Rule** | Notion Knowledge Base | Everyone | If a question is asked twice, write an SOP. |

---

## ⚡ Quick Resources
- 💬 [Slack / Discord Workspace](https://slack.com)
- 📁 [Team Shared Drive / GitHub](https://github.com)
- 🎨 [Figma Workspace](https://figma.com)
- 📊 [Financial & Expense Policy](sops/expense_and_budgeting.md)

---

## 🎯 Active Projects (Connected to Tasks)
*View projects grouped by status. Rollup bars track child task completion automatically.*

| Project Name | Category | Status | Owner | Timeline | Priority | Target Deliverable |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V1 Product MVP Launch** | Product | `In Progress` | Alex Chen | Nov 1 - Dec 15 | 🔴 High | Working production prototype |
| **Q4 Team Onboarding & Playbook** | Operations | `In Progress` | Sarah Connor | Nov 10 - Nov 30 | 🟡 Medium | Scalable new member onboarding |
| **Community & Partner Pilot** | Growth | `Not Started` | Marcus Aurelius | Dec 1 - Jan 15 | 🟢 Low | 5 verified pilot partners |

---

## ✅ Daily Tasks Board
*Filtered by: `Assignee = "Me"` and `Status ≠ Done`.*

| Task Name | Project | Assignee | Due Date | Priority | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Finalize schema and database migrations | V1 Product MVP Launch | Alex Chen | 2026-11-05 | High | In Progress |
| Draft Team Code of Conduct & Rituals | Q4 Team Onboarding & Playbook | Sarah Connor | 2026-11-08 | Medium | In Progress |
| Configure production monitoring & error alerts | V1 Product MVP Launch | Alex Chen | 2026-11-12 | High | To Do |
| Compile outreach list of 25 pilot partners | Community & Partner Pilot | Marcus Aurelius | 2026-11-20 | Low | To Do |
| Audit knowledge base for stale documentation | Q4 Team Onboarding & Playbook | Sarah Connor | 2026-11-25 | Medium | To Do |

---

## 📚 Knowledge Base (SOPs & Policies)
*All documentation is tracked with a 90-day verification health formula.*

1. 📘 [How We Run Meetings (The 15-Minute Sync)](sops/meeting_protocol.md) — *Owner: Sarah Connor (Status: ✅ Current)*
2. 📘 [Team Onboarding Checklist & System Access](sops/member_onboarding.md) — *Owner: Sarah Connor (Status: ✅ Current)*
3. 🛠️ [Engineering Git & PR Standards](sops/engineering_workflow.md) — *Owner: Alex Chen (Status: ✅ Current)*
4. ⚖️ [Reimbursement & Equipment Policy](sops/expense_and_budgeting.md) — *Owner: Marcus Aurelius (Status: ✅ Current)*

---
### 🗄️ Backend Databases (Free-Tier Architecture)
- `🎯 [HQ] Projects`: Relational project parent table.
- `✅ [HQ] Tasks`: Atomic task items linked to Projects.
- `📚 [HQ] Knowledge Base`: Centralized wiki with health formulas.
