import streamlit as st
import pandas as pd
import plotly.express as px

from data_stream import get_power_signal
from nilm_engine import disaggregate_power, detect_anomaly
from ai_copilot import energy_copilot
from energy_score import calculate_score, score_label

st.set_page_config(page_title="NILM Energy AI", layout="wide")

st.title("⚡ NILM Energy Intelligence Platform")
st.caption("AI-based Non-Intrusive Load Monitoring System")

page = st.sidebar.radio("Navigate", ["Dashboard", "AI Copilot", "Energy Score"])

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    total_power = get_power_signal()
    devices = disaggregate_power(total_power)

    st.subheader("Live Power Signal (Main Line)")
    st.metric("Total Load", f"{total_power} W")

    st.subheader("AI Disaggregated Devices")

    for d, w in devices.items():
        st.write(f"🔌 {d}: {w} W")

    st.subheader("AI Detection")
    st.warning(detect_anomaly(devices))

    df = pd.DataFrame({
        "Device": list(devices.keys()),
        "Power": list(devices.values())
    })

    fig = px.bar(df, x="Device", y="Power", title="Energy Breakdown")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- COPILOT ----------------
if page == "AI Copilot":

    st.subheader("🧠 Energy AI Copilot")

    query = st.text_input("Ask your energy assistant:")

    if query:
        total_power = get_power_signal()
        response = energy_copilot(query, total_power)

        st.success(response)

# ---------------- ENERGY SCORE ----------------
if page == "Energy Score":

    st.subheader("🏠 Household Energy Score")

    total_kwh = get_power_signal() / 1000
    score = calculate_score(total_kwh)

    st.metric("Energy Score", score)
    st.info(score_label(score))
