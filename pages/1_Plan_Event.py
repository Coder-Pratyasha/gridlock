import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Plan Event",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Event Planner")
st.caption(
    "Create a planned event and generate congestion forecasts."
)

st.divider()

event_types = [
    "debris",
    "water_logging",
    "vehicle_breakdown",
    "tree_fall",
    "congestion",
    "others",
    "pot_holes",
    "construction",
    "road_conditions",
    "Debris",
    "accident",
    "test_demo",
    "protest",
    "Fog / Low Visibility",
    "procession",
    "public_event",
    "vip_movement",
]

route_based_events = {
    "VIP Movement",
    "Political Rally",
    "Festival",
    "Marathon",
    "Sports Event"
}

junctions = [
    "Junction A",
    "Junction B",
    "Junction C",
    "Junction D",
    "Junction E",
    "Junction F",
    "Junction G",
    "Junction H"
]

col1, col2 = st.columns(2)

with col1:
    event_type = st.selectbox(
        "Event Type",
        event_types
    )

with col2:
    expected_attendance = st.number_input(
        "Expected Attendance",
        min_value=0,
        step=100
    )

col1, col2 = st.columns(2)

with col1:
    event_date = st.date_input(
        "Event Date",
        value=date.today()
    )

with col2:
    event_time = st.time_input(
        "Start Time"
    )

st.divider()

st.subheader("Event Location")

event_location = st.selectbox(
    "Location",
    junctions
)

if event_type in route_based_events:

    st.divider()

    st.subheader("Route Information")

    start_point = st.selectbox(
        "Start Point",
        junctions
    )

    if "via_count" not in st.session_state:
        st.session_state.via_count = 0

    if st.button("➕ Add Via Point"):
        st.session_state.via_count += 1

    via_points = []

    for i in range(st.session_state.via_count):
        via = st.selectbox(
            f"Via Point {i + 1}",
            junctions,
            key=f"via_{i}"
        )

        via_points.append(via)

    end_point = st.selectbox(
        "End Point",
        [""] + junctions
    )

else:
    start_point = None
    end_point = None
    via_points = []

st.divider()

if st.button(
    "Generate Deployment Plan",
    type="primary",
    use_container_width=True
):

    payload = {
        "event_type": event_type,
        "event_date": str(event_date),
        "event_time": str(event_time),
        "attendance": expected_attendance,
        "event_location": event_location,
        "start_point": start_point,
        "via_points": via_points,
        "end_point": end_point
    }

    st.success("Event submitted successfully.")

    st.json(payload)
