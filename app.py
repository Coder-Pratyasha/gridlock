import streamlit as st

st.set_page_config(
    page_title="FlowGuard AI",
    page_icon="🚦",
    layout="wide"
)

st.markdown("""
<h1 style='margin-bottom:0px;'>
FlowGuard AI
</h1>
<p style='font-size:18px;color:#9CA3AF;margin-top:-8px;'>
Event-Aware Congestion Prediction & Resource Optimization
</p>
""", unsafe_allow_html=True)

st.divider()

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Active Events", "12")

with m2:
    st.metric("Critical Junctions", "8")

with m3:
    st.metric("Resources Deployed", "146")

with m4:
    st.metric("Diversions Active", "5")

st.divider()

st.subheader("Operations")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 📅 Plan Event")
        st.caption("Forecast congestion and pre-plan deployments.")
        if st.button(
            "Launch Planner",
            use_container_width=True,
            type="primary"
        ):
            st.switch_page("pages/1_Plan_Event.py")

with col2:
    with st.container(border=True):
        st.markdown("### 🚨 Report Incident")
        st.caption("Generate real-time response recommendations.")
        st.button(
            "Open Incident Desk",
            use_container_width=True
        )

st.divider()

st.subheader("Live City Overview")

map_placeholder = """
<div style="
height:500px;
border:1px solid rgba(255,255,255,0.1);
border-radius:12px;
display:flex;
align-items:center;
justify-content:center;
background:rgba(255,255,255,0.02);
font-size:20px;
color:#9CA3AF;
">
Interactive Congestion Map
</div>
"""

st.markdown(map_placeholder, unsafe_allow_html=True)

st.divider()

st.subheader("Recent Alerts")

with st.container(border=True):
    st.markdown("""
🔴 **MG Road Junction** — Severe congestion expected

🟠 **Queens Circle** — Diversion recommended

🟢 **Airport Corridor** — Operating normally
""")