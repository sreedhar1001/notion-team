# SOP: Engineering Git & PR Standards

> **Category**: Knowledge Base Standard Operating Procedure  
> **Status**: Verified  
> **Last Audited**: 2026-10-22  
> **Grounding Context**: The best branching strategy is the simplest one your team will follow consistently; trunk-based development is ideal, with GitHub Flow as a good middle ground. Enforce commit conventions with a pre-commit hook (commitlint) for automated enforcement. Use Gitmore to track adherence to these standards, focusing on PR size, branch lifespan, and commit frequency. For most teams, trunk-based development (short-lived branches merged to main daily) or GitHub Flow (feature branches merged via PR) is recommended, with Gitflow reserved for maintaining multiple release versions simultaneously. Simpler branching strategies are preferred to avoid complications.

---

## 1. Purpose & Objective
This document outlines the standard operating procedures for **Engineering Git & PR Standards** within Autonomous Robotics Club. The goal is to eliminate recurring confusion, enable full async transparency, and maintain a lightweight execution cadence.

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
