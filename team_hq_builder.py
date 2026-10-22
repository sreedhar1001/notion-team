"""
team_hq_builder.py — Autonomous Team HQ Generator grounded with Tavily Search.
Builds accurate, production-grade Notion workspaces from live industry research.
"""

import os
import sys
import csv
import json
from pathlib import Path
from dotenv import load_dotenv
from tavily import TavilyClient

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Load environment variables
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

class TeamHQBuilder:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("TAVILY_API_KEY")
        if not self.api_key:
            raise ValueError("TAVILY_API_KEY not found. Please set it in .env or environment.")
        self.tavily = TavilyClient(api_key=self.api_key)
        self.output_dir = Path("build_output")
        self.output_dir.mkdir(exist_ok=True)
        (self.output_dir / "sops").mkdir(exist_ok=True)

    def research_industry_norms(self, team_type: str, domain: str) -> dict:
        """Query Tavily for real-world team rituals, OKRs, and operational norms."""
        query = f"best practices Notion team HQ workspace structure for {team_type} {domain} OKRs norms"
        print(f"🔍 [Tavily Search] Querying: '{query}'...")
        try:
            res = self.tavily.search(query=query, max_results=3, include_answer=True)
            summary = res.get("answer") or "Standard agile operating model with weekly syncs and async documentation."
            sources = [r["url"] for r in res.get("results", [])]
            return {"summary": summary, "sources": sources}
        except Exception as e:
            print(f"⚠️ Tavily query failed: {e}. Falling back to standard agile profile.")
            return {
                "summary": "Agile operating model with high-transparency sprint cadences, async-first documentation, and continuous deliverable tracking.",
                "sources": []
            }

    def research_sop_content(self, sop_title: str, domain: str) -> str:
        """Fetch real-world operational steps for a standard operating procedure."""
        query = f"standard operating procedure template {sop_title} {domain} steps checklist"
        print(f"📖 [Tavily Search] Researching SOP: '{sop_title}'...")
        try:
            res = self.tavily.search(query=query, max_results=2, include_answer=True)
            answer = res.get("answer")
            if answer and len(answer) > 80:
                return answer
        except Exception as e:
            print(f"⚠️ Tavily SOP query error: {e}")
        return "1. Schedule sync. 2. Define clear objectives. 3. Document action items. 4. Assign single owners. 5. Follow up in 7 days."

    def build(self, team_name: str, team_type: str, domain: str, mission: str, north_star: str):
        """Construct the complete Notion workspace export grounded in Tavily research."""
        print(f"\n🚀 Generating Team HQ for '{team_name}' ({team_type} - {domain})...")
        
        # 1. Research industry norms
        research = self.research_industry_norms(team_type, domain)
        
        # 2. Build Root Company Home Markdown
        company_home = f"""# 🏛️ {team_name} — Team HQ

> **🎯 Mission**: {mission}  
> **⚡ Current North Star**: {north_star}  
> **💡 Operating Model Research**: {research['summary']}

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
"""
        with open(self.output_dir / "Company_Home.md", "w", encoding="utf-8") as f:
            f.write(company_home)

        # 3. Build CSVs for Direct Notion Import
        # Projects CSV
        projects_csv_path = self.output_dir / "HQ_Projects.csv"
        with open(projects_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Project Name", "Category", "Status", "Owner", "Timeline", "Priority", "Progress"])
            writer.writerow(["V1 Product MVP Launch", "Product", "In Progress", "Alex Chen", "2026-11-01 -> 2026-12-15", "High", "60%"])
            writer.writerow(["Q4 Team Onboarding & Playbook", "Operations", "In Progress", "Sarah Connor", "2026-11-10 -> 2026-11-30", "Medium", "40%"])
            writer.writerow(["Community & Partner Pilot", "Growth", "Not Started", "Marcus Aurelius", "2026-12-01 -> 2027-01-15", "Low", "0%"])

        # Tasks CSV
        tasks_csv_path = self.output_dir / "HQ_Tasks.csv"
        with open(tasks_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Task Name", "Status", "Assignee", "Due Date", "Priority", "Project"])
            writer.writerow(["Finalize schema and database migrations", "In Progress", "Alex Chen", "2026-11-05", "High", "V1 Product MVP Launch"])
            writer.writerow(["Draft Team Code of Conduct & Rituals", "In Progress", "Sarah Connor", "2026-11-08", "Medium", "Q4 Team Onboarding & Playbook"])
            writer.writerow(["Configure production monitoring & error alerts", "To Do", "Alex Chen", "2026-11-12", "High", "V1 Product MVP Launch"])
            writer.writerow(["Compile outreach list of 25 pilot partners", "To Do", "Marcus Aurelius", "2026-11-20", "Low", "Community & Partner Pilot"])
            writer.writerow(["Audit knowledge base for stale documentation", "To Do", "Sarah Connor", "2026-11-25", "Medium", "Q4 Team Onboarding & Playbook"])

        # Knowledge Base CSV
        kb_csv_path = self.output_dir / "HQ_Knowledge_Base.csv"
        with open(kb_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Doc Title", "Category", "Owner", "Last Verified", "Health", "Pinned"])
            writer.writerow(["How We Run Meetings (The 15-Minute Sync)", "SOP", "Sarah Connor", "2026-10-20", "✅ Verified", "Yes"])
            writer.writerow(["Team Onboarding Checklist & System Access", "SOP", "Sarah Connor", "2026-10-18", "✅ Verified", "Yes"])
            writer.writerow(["Engineering Git & PR Standards", "Tools & Stack", "Alex Chen", "2026-10-15", "✅ Verified", "Yes"])
            writer.writerow(["Reimbursement & Equipment Policy", "Policy", "Marcus Aurelius", "2026-09-01", "✅ Verified", "No"])

        # 4. Generate Research-Grounded SOP Markdown Files
        sop_configs = [
            ("meeting_protocol.md", "How We Run Meetings", "effective asynchronous and synchronous 15-minute standup agenda"),
            ("member_onboarding.md", "Team Member Onboarding Checklist", "new hire 30-60-90 onboarding checklist and tooling setup"),
            ("engineering_workflow.md", "Engineering Git & PR Standards", "code review checklist pull request standards trunk-based development"),
            ("expense_and_budgeting.md", "Reimbursement & Equipment Policy", "team expense reimbursement policy submission and approval limits")
        ]

        for filename, title, query_suffix in sop_configs:
            sop_research = self.research_sop_content(title, query_suffix)
            sop_doc = f"""# SOP: {title}

> **Category**: Knowledge Base Standard Operating Procedure  
> **Status**: Verified  
> **Last Audited**: 2026-10-22  
> **Grounding Context**: {sop_research}

---

## 1. Purpose & Objective
This document outlines the standard operating procedures for **{title}** within {team_name}. The goal is to eliminate recurring confusion, enable full async transparency, and maintain a lightweight execution cadence.

## 2. Prerequisites & Permissions
- Confirmed account in team Notion workspace and communication hub.
- Read and accepted the team operating norms.

## 3. Step-by-Step Instructions
- [ ] **Step 1**: Review the current deliverable status before initiating any sync or modification.
- [ ] **Step 2**: If proposing a change, reference the parent Project in `🎯 [HQ] Projects`.
- [ ] **Step 3**: Document explicit decisions directly in the page body; avoid leaving decisions in transient chat threads.
- [ ] **Step 4**: Assign direct single owners and due dates for any newly created action items.

## 4. Troubleshooting & Gotchas
| Problem | Root Cause | Solution |
| :--- | :--- | :--- |
| Missing permissions | Account not added to guest group | Contact workspace admin with verified email. |
| Stale information | Doc unverified > 90 days | Run Notion AI audit prompt or notify document owner. |
"""
            with open(self.output_dir / "sops" / filename, "w", encoding="utf-8") as f:
                f.write(sop_doc)

        # 5. Notion Import Guide
        import_guide = f"""# 📥 How to Import this Team HQ into Notion in 2 Minutes

This folder contains pre-built, production-ready assets grounded in live Tavily industry research.

### Step 1: Create your Root Page
1. Open Notion and click **+ Add a page** in the sidebar.
2. Title it: `{team_name} HQ` and select **Full width** in the page menu (`...` top right).
3. Copy the markdown content from `{self.output_dir / "Company_Home.md"}` and paste it directly into the page.

### Step 2: Import Databases
1. At the bottom of your root page, create a toggle: `> 🗄️ Backend Databases`.
2. Inside the toggle:
   - Click Notion's **Import** option (or `/import`) ➔ Select **CSV**.
   - Import `HQ_Projects.csv` ➔ Creates `🎯 [HQ] Projects`.
   - Import `HQ_Tasks.csv` ➔ Creates `✅ [HQ] Tasks`.
   - Import `HQ_Knowledge_Base.csv` ➔ Creates `📚 [HQ] Knowledge Base`.

### Step 3: Link Tasks to Projects
1. In `HQ_Tasks`, open property `Project` ➔ Change type from Text to **Relation** ➔ Choose `🎯 [HQ] Projects`.
2. Notion will automatically connect matching project names!

### Step 4: Import SOPs
1. Drag and drop the `.md` files from `{self.output_dir / "sops"}` directly into your Notion `Knowledge Base` database!
"""
        with open(self.output_dir / "NOTION_IMPORT_GUIDE.md", "w", encoding="utf-8") as f:
            f.write(import_guide)

        print(f"\n✅ Build complete! All assets saved to '{self.output_dir.absolute()}'.")
        return self.output_dir

if __name__ == "__main__":
    builder = TeamHQBuilder()
    builder.build(
        team_name="HyperScale AI",
        team_type="Early-Stage AI Startup",
        domain="AI Developer Infrastructure & Autonomous Agents",
        mission="Build the single operating system for autonomous agents and developer tooling.",
        north_star="Ship V1 public beta with 1,000 active developers and 99.9% uptime."
    )
