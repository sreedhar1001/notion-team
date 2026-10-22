# 📥 How to Import this Team HQ into Notion in 2 Minutes

This folder contains pre-built, production-ready assets grounded in live Tavily industry research.

### Step 1: Create your Root Page
1. Open Notion and click **+ Add a page** in the sidebar.
2. Title it: `Autonomous Robotics Club HQ` and select **Full width** in the page menu (`...` top right).
3. Copy the markdown content from `build_output\Company_Home.md` and paste it directly into the page.

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
1. Drag and drop the `.md` files from `build_output\sops` directly into your Notion `Knowledge Base` database!
