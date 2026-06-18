import streamlit as st

st.set_page_config(
    page_title="Event Congestion Management System",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Event Congestion Management System")
st.markdown(
    """
    Intelligent congestion prediction, resource allocation,
    hotspot detection, and adaptive event learning.
    """
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Plan Event")

    st.markdown("""
    Use this mode for:
    - Sports Events
    - Political Rallies
    - Festivals
    - Marathons
    - VIP Visits

    Predict congestion before the event occurs.
    """)

    if st.button("Open Event Planner", use_container_width=True):
        st.success("Event Planner Selected")

with col2:
    st.subheader("🚨 Report Event")

    st.markdown("""
    Use this mode for:
    - Accidents
    - Tree Falls
    - Road Blockages
    - Waterlogging
    - Emergencies

    Generate immediate deployment recommendations.
    """)

    if st.button("Report Incident", use_container_width=True):
        st.success("Incident Reporting Selected")

st.divider()

st.subheader("📊 System Capabilities")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        label="Event Types",
        value="17"
    )

with c2:
    st.metric(
        label="Tracked Junctions",
        value="294"
    )

with c3:
    st.metric(
        label="Hotspot Detection",
        value="Enabled"
    )

with c4:
    st.metric(
        label="Adaptive Learning",
        value="Enabled"
    )

st.divider()

st.subheader("⚙️ Workflow")

st.markdown("""
1. Event Reported / Planned
2. Event Severity Analysis
3. Junction Risk Analysis
4. Hotspot Detection
5. Resource Allocation
6. Diversion Planning
7. Deployment Recommendations
8. Feedback-Based Learning
""")

st.divider()

st.info(
    "The system continuously learns from previous events to improve future deployment recommendations."
)