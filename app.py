import streamlit as st
import folium
import json
from datetime import datetime
from pathlib import Path
from streamlit_folium import st_folium

from components.event_layer import add_event_layer
from components.junction_layer import add_junction_layer
from components.critical_zone_layer import add_critical_zone_layer
from components.deployment_layer import add_deployment_layer
from components.infrastructure_layer import add_infrastructure_layer
from components.diversion_layer import add_diversion_layer
from components.emergency_layer import add_emergency_layer

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


def safe_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def is_truthy(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "1", "yes", "y"}
    return bool(value)


def parse_event_datetime(event):
    event_date = event.get("event_date")
    if not event_date:
        return None

    event_time = event.get("event_time") or "00:00:00"

    try:
        return datetime.fromisoformat(f"{event_date}T{event_time}")
    except ValueError:
        return None


def format_event_entry(event):
    title = event.get("event_name") or str(event.get("event_type", "Untitled Event")).replace("_", " ").title()
    details = []

    event_dt = parse_event_datetime(event)
    if event_dt:
        details.append(event_dt.strftime("%Y-%m-%d, %H:%M"))
    elif event.get("event_date"):
        details.append(event["event_date"])

    if event.get("event_location"):
        details.append(event["event_location"])
    elif event.get("event_type"):
        details.append(str(event["event_type"]).replace("_", " ").title())

    return f"{title} — {', '.join(details)}" if details else title


events_path = Path(__file__).resolve().parent / "datasets" / "events.json"
with events_path.open(encoding="utf-8") as f:
    events = json.load(f)

event_records = events if isinstance(events, list) else []
scheduled_events = [event for event in event_records if event.get("event_date")]
upcoming_events = [event for event in scheduled_events if str(event.get("status", "")).lower() == "planned"]
if not upcoming_events:
    upcoming_events = scheduled_events

live_events = [event for event in event_records if str(event.get("status", "")).lower() == "live"]
if not live_events:
    live_events = [event for event in event_records if not event.get("event_date")]

active_events_count = len(event_records)
critical_junctions_count = len({event.get("event_location") for event in event_records if event.get("event_location")})
resources_deployed = sum(safe_int(event.get("attendance")) for event in event_records)
diversions_active = sum(1 for event in event_records if is_truthy(event.get("divergence_required")))

st.divider()

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Active Events", active_events_count)

with m2:
    st.metric("Critical Junctions", critical_junctions_count)

with m3:
    st.metric("Resources Deployed", resources_deployed)

with m4:
    st.metric("Diversions Active", diversions_active)

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
        if st.button(
            "Open Incident Desk",
            use_container_width=True,
            type="primary"
        ):
            st.switch_page("pages/2_Report_Event.py")

st.divider()
with open("datasets/dummy.json") as f:
    data = json.load(f)

venue = data["event"]["venue"]

m = folium.Map(
    location=[venue["lat"], venue["lon"]],
    zoom_start=16
)

add_event_layer(m, data)
add_junction_layer(m, data)
add_critical_zone_layer(m, data)
add_deployment_layer(m, data)
add_infrastructure_layer(m, data)
add_diversion_layer(m, data)
add_emergency_layer(m, data)

st_folium(
    m,
    height=600,
    use_container_width=True
)

# st.subheader("Live City Overview")

# map_placeholder = """
# <div style="
# height:500px;
# border:1px solid rgba(255,255,255,0.1);
# border-radius:12px;
# display:flex;
# align-items:center;
# justify-content:center;
# background:rgba(255,255,255,0.02);
# font-size:20px;
# color:#9CA3AF;
# ">
# Interactive Congestion Map
# </div>
# """

# st.markdown(map_placeholder, unsafe_allow_html=True)

st.divider()

st.subheader("Recent Alerts")

with st.container(border=True):
    st.markdown("""
🔴 **MG Road Junction** — Severe congestion expected

🟠 **Queens Circle** — Diversion recommended

🟢 **Airport Corridor** — Operating normally
""")
    
st.divider()

st.subheader("Upcoming Events")

with st.container(border=True):
    if upcoming_events:
        st.markdown("\n".join(f"{index}. {format_event_entry(event)}" for index, event in enumerate(upcoming_events, start=1)))
    else:
        st.caption("No upcoming events found in events.json.")
    
st.divider()

st.subheader("Live Events")

with st.container(border=True):
    if live_events:
        st.markdown("\n".join(f"{index}. {format_event_entry(event)}" for index, event in enumerate(live_events, start=1)))
    else:
        st.caption("No live events found in events.json.")