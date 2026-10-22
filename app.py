"""
app.py — Interactive Team HQ Autopilot Web Application.
Uses Tavily Search API to research and generate custom Notion Team HQs.
"""

import os
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
from team_hq_builder import TeamHQBuilder

load_dotenv()

st.set_page_config(
    page_title="Team HQ Architect & Autopilot",
    page_icon="🏛️",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E293B;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 2rem;
    }
    .badge-card {
        background: #F8FAFC;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #E2E8F0;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🏛️ Notion Team HQ Architect</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Build a battle-tested Team HQ in Notion grounded with real-time research using <b>Tavily Search API</b>.</div>', unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.header("🔑 Credentials & Settings")
    api_key_input = st.text_input("Tavily API Key", value=os.getenv("TAVILY_API_KEY", ""), type="password")
    
    st.header("🎯 Team Profile Presets")
    preset = st.selectbox(
        "Choose an Archetype",
        ["Early-Stage Tech Startup", "University Student Club", "Mission-Driven Non-Profit", "Product & Design Agency", "Custom"]
    )
    
    if preset == "Early-Stage Tech Startup":
        default_name = "HyperScale AI"
        default_type = "AI Developer Tools Startup"
        default_domain = "AI Agents, Developer Infrastructure, LLMs"
        default_mission = "Build frictionless autonomous agent operating infrastructure for engineers."
        default_north_star = "Ship V1 public beta, acquire 1,000 active developers, maintain 99.9% uptime."
    elif preset == "University Student Club":
        default_name = "Autonomous Robotics Club"
        default_type = "University Engineering Society"
        default_domain = "Robotics, Autonomous Vehicles, Hardware Hackathons"
        default_mission = "Empower undergraduate students to build and compete in international robotics contests."
        default_north_star = "Complete rover chassis by Q3 and qualify for national finals."
    elif preset == "Mission-Driven Non-Profit":
        default_name = "GreenUrban Clean Water"
        default_type = "Environmental Non-Profit"
        default_domain = "Clean Water Access, Community Organizing, Grant Management"
        default_mission = "Deploy clean drinking water filtration systems to under-resourced schools."
        default_north_star = "Deliver 50 school water stations and secure \$250k in foundation grants."
    elif preset == "Product & Design Agency":
        default_name = "Studio Craft"
        default_type = "Boutique Digital Product Agency"
        default_domain = "UI/UX Design, Full-Stack Web Development, Brand Systems"
        default_mission = "Design and ship high-converting digital products for high-growth tech brands."
        default_north_star = "Close 6 client retainer contracts and maintain 95% client satisfaction."
    else:
        default_name = ""
        default_type = ""
        default_domain = ""
        default_mission = ""
        default_north_star = ""

# Main Input Form
col1, col2 = st.columns(2)
with col1:
    team_name = st.text_input("Team / Company Name", value=default_name)
    team_type = st.text_input("Organization Type", value=default_type)
    domain = st.text_input("Core Domain / Industry", value=default_domain)

with col2:
    mission = st.text_area("Team Mission Statement", value=default_mission, height=85)
    north_star = st.text_area("Quarterly North Star Metric", value=default_north_star, height=85)

st.markdown("---")

if st.button("🚀 Generate Team HQ (Powered by Tavily Search)", type="primary"):
    if not api_key_input:
        st.error("Please provide a valid Tavily API Key in the sidebar.")
    elif not team_name or not mission:
        st.error("Please fill in Team Name and Mission.")
    else:
        with st.spinner("🔍 Querying Tavily Search for industry rituals, SOPs, and project structures..."):
            try:
                builder = TeamHQBuilder(api_key=api_key_input)
                output_path = builder.build(
                    team_name=team_name,
                    team_type=team_type,
                    domain=domain,
                    mission=mission,
                    north_star=north_star
                )
                st.success(f"🎉 Team HQ successfully generated! Files created in `{output_path}`.")
                st.session_state["generated"] = True
            except Exception as e:
                st.error(f"Error during generation: {e}")

# Display Outputs if generated
if st.session_state.get("generated"):
    out_dir = Path("build_output")
    
    st.markdown("### 📋 Generated Workspace Previews")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Company Home", "🎯 Projects DB", "✅ Tasks DB", "📚 Knowledge Base SOPs", "📥 Notion Import Guide"])
    
    with tab1:
        if (out_dir / "Company_Home.md").exists():
            with open(out_dir / "Company_Home.md", "r", encoding="utf-8") as f:
                st.markdown(f.read())
                
    with tab2:
        if (out_dir / "HQ_Projects.csv").exists():
            import pandas as pd
            df_proj = pd.read_csv(out_dir / "HQ_Projects.csv")
            st.dataframe(df_proj, use_container_width=True)
            
    with tab3:
        if (out_dir / "HQ_Tasks.csv").exists():
            import pandas as pd
            df_tasks = pd.read_csv(out_dir / "HQ_Tasks.csv")
            st.dataframe(df_tasks, use_container_width=True)

    with tab4:
        sops = list((out_dir / "sops").glob("*.md"))
        if sops:
            sop_sel = st.selectbox("Select an SOP to inspect", [p.name for p in sops])
            with open(out_dir / "sops" / sop_sel, "r", encoding="utf-8") as f:
                st.markdown(f.read())

    with tab5:
        if (out_dir / "NOTION_IMPORT_GUIDE.md").exists():
            with open(out_dir / "NOTION_IMPORT_GUIDE.md", "r", encoding="utf-8") as f:
                st.markdown(f.read())
