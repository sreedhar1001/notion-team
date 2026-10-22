# NOTION_AI_TEMPLATES.md — Team HQ AI Prompt Library
<!-- Ready-to-Use Notion AI & LLM Execution Prompts -->

Use these prompts inside Notion AI blocks (`/ai prompt`) or in your external LLM assistant to automate routine workspace tasks.

---

## Template 1: Instant SOP & How-To Generator
**Trigger**: When an engineer or team member types quick messy notes about a process.

```markdown
Prompt:
"You are a technical documentation specialist. Transform the following rough notes into a standardized Standard Operating Procedure (SOP) for our Team Knowledge Base.

Follow this exact structure:
1. # [Clear Title Starting with a Verb, e.g., 'How to Deploy Staging']
2. **Context & Goal**: 1-2 sentences explaining why this SOP exists and what success looks like.
3. **Prerequisites**: Bullet list of tools, credentials, or permissions needed before starting.
4. **Step-by-Step Instructions**: Numbered steps with interactive checkboxes [ ] for each action. Be explicit and concise.
5. **Common Gotchas & Troubleshooting**: A 2-column table with 'Issue / Error' and 'Resolution'.

Notes to transform:
[PASTE UNSTRUCTURED NOTES HERE]"
```

---

## Template 2: Meeting Minutes to Structured Tasks
**Trigger**: After a weekly sync, product kickoff, or all-hands.

```markdown
Prompt:
"Analyze the following meeting transcript/notes. Extract:
1. **Core Decisions Made**: Bulleted list of final decisions (ignore conversational debate).
2. **Action Item Table**: Create a clean markdown table with the following columns:
   - | Task Name (Imperative verb, e.g. 'Draft Q4 marketing brief') |
   - | Suggested Assignee |
   - | Due Date (Infer from conversation or flag as 'TBD') |
   - | Priority (P1-Critical, P2-Normal, P3-Low) |
   - | Related Project Context |

Meeting Notes:
[PASTE MEETING MINUTES HERE]"
```

---

## Template 3: Weekly Executive Status Digest
**Trigger**: End-of-week reporting for leadership or all-team channels.

```markdown
Prompt:
"Based on the following list of tasks marked 'Done' this week and the current status of active projects, write a concise 3-part weekly digest suitable for Slack or email:

Structure:
🚀 **Shipped This Week**: 3-5 bullet points highlighting major milestones achieved.
🚧 **In Progress & Focus for Next Week**: Top 2-3 focus areas.
⚠️ **Blockers & Dependencies**: Any item marked blocked or flagged for attention.

Data:
[PASTE COMPLETED TASKS & ACTIVE PROJECT LIST HERE]"
```

---

## Template 4: Project Scope & Deliverables Blueprint
**Trigger**: When a teammate has an initial idea for a new project.

```markdown
Prompt:
"Act as a Senior Technical Product Manager. Turn this project idea into a complete Notion Project Brief.

Provide:
1. **Executive Summary**: 2 sentences on the objective.
2. **In-Scope vs. Out-of-Scope**: Two clear bulleted lists to prevent scope creep.
3. **Key Results / Definition of Done**: Quantifiable success criteria.
4. **Milestone Breakdown**: 3-4 sequential phases.
5. **Initial Task List**: 5-8 atomic tasks ready to be copied into our Notion Tasks database.

Project Idea:
[PASTE BRIEF IDEA HERE]"
```
