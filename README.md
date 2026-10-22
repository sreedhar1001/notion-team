# Notion Team HQ — Iceberg Agent Architecture

This repository contains the complete specification, agent operating system, and automation runbooks for building and running a modern **Team HQ in Notion** on a 100% Free Plan.

---

## 🧊 The Iceberg Technique

In autonomous agent design, stuffing every detail into a single system prompt leads to high latency, hallucinations, and context exhaustion. The **Iceberg Technique** structures agent context into three progressive layers:

```
                            ▲
                           / \      1. ABOVE THE WATERLINE (10%)
                          /   \     • AGENTS.md: Always-on operating charter,
                         /     \      personas, routing, and guardrails.
    ═════════════════════/═══════\══════════════════════════════════════════ [Waterline]
                        /         \ 2. AT THE WATERLINE (30%)
                       /           \• SKILLS.md: Modular procedural capabilities
                      /             \ (schemas, blueprints, formulas) loaded on-demand.
                     /               \
                    /                 \ 3. DEEP SUBMERGED (60%)
                   /                   \• MEMORY.md: Persistent state, ADRs,
                  /                     \ anti-patterns, and project history.
                 /                       \• WORKFLOWS.md: Deterministic runbooks.
                /─────────────────────────\• NOTION_AI_TEMPLATES.md: Prompt library.
```

---

## 📁 Repository Manifest

| Layer | File | Purpose |
| :--- | :--- | :--- |
| **Tier 1: Surface** | [AGENTS.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/AGENTS.md) | Universal operating charter, agent personas, routing matrix, and strict guardrails. |
| **Tier 2: Waterline** | [SKILLS.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/SKILLS.md) | Modular procedural capabilities loaded via progressive disclosure (database schemas, formulas, blueprints). |
| **Tier 3: Submerged** | [MEMORY.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/MEMORY.md) | Long-term memory, Architectural Decision Records (ADRs), entity topology, and anti-patterns. |
| **Tier 3: Playbooks** | [WORKFLOWS.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/WORKFLOWS.md) | Step-by-step execution playbooks (Bootstrapping, Self-referencing templates, Weekly triage). |
| **Tier 3: Prompts** | [NOTION_AI_TEMPLATES.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/NOTION_AI_TEMPLATES.md) | Copy-pasteable Notion AI prompts for instant SOPs, meeting-to-task parsing, and status digests. |

---

## 🚀 Quick Start: Building Your Team HQ

1. Read [WORKFLOWS.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/WORKFLOWS.md) for the 30-minute step-by-step build guide.
2. Follow the 3-Database Triad schema defined in [SKILLS.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/SKILLS.md#skill-2-skilldatabase-relations).
3. Use the self-referencing project template pattern so tasks automatically link to projects.
4. Set up the automated stale doc health formula from [SKILLS.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/SKILLS.md#41-knowledge-base-stale-doc-formula-free-tier-compatible).
5. Run the 15-minute weekly triage routine with [NOTION_AI_TEMPLATES.md](file:///c:/Users/sridh/Documents/antigravity/goofy-curie/NOTION_AI_TEMPLATES.md).
