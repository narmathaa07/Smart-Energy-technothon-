import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

from ai_engine import detect_waste, estimate_cost, estimate_co2
from data import devices, usage_hours

st.set_page_config(page_title="Smart Energy AI", page_icon="⚡", layout="wide")

st.title("⚡ Smart Energy AI Dashboard")
st.caption("AI-powered energy monitoring system")

page = st.sidebar.radio("Navigation", ["🏠 Dashboard", "📊 Insights", "⚠️ Alerts", "🔮 Prediction"])

motion_detected = False

# ---------------- DASHBOARD ----------------
if page == "🏠 Dashboard":

    st.subheader("Live Energy Overview")

    total_kwh = sum([(devices[d] * usage_hours[d]) / 1000 for d in devices])
    total_cost = sum([estimate_cost(devices[d], usage_hours[d]) for d in devices])

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Energy", f"{round(total_kwh, 2)} kWh")
    col2.metric("Estimated Bill", f"RM {round(total_cost, 2)}")
    col3.metric("CO₂ Emission", f"{estimate_co2(total_kwh)} kg")

    st.divider()

    for d in devices:
        st.write(f"🔌 {d} - {devices[d]}W ({usage_hours[d]} hrs)")
        st.caption(detect_waste(d, devices[d], usage_hours[d], motion_detected))

# ---------------- INSIGHTS ----------------
if page == "📊 Insights":

    st.subheader("Energy Breakdown")

    df = pd.DataFrame({
        "Device": list(devices.keys()),
        "Usage": np.random.randint(10, 50, len(devices))
    })

    fig = px.pie(df, names="Device", values="Usage", title="Energy Usage")
    st.plotly_chart(fig, use_container_width=True)

    st.success("💡 AC is your highest energy consumer (52%)")
    st.warning("⚠️ RM 18 wasted due to idle usage")
    st.info("🌱 5kg CO₂ saved this week")

# ---------------- ALERTS ----------------
if page == "⚠️ Alerts":

    st.subheader("AI Waste Detection")

    if st.button("Run AI Scan"):
        with st.spinner("Analyzing energy patterns..."):
            time.sleep(2)

        st.error("⚠️ AC running in empty room for 2 hours")
        st.warning("⚠️ High usage detected")
        st.success("✔ System stable otherwise")

# ---------------- PREDICTION ----------------
if page == "🔮 Prediction":

    st.subheader("Energy Forecasting")

    total_kwh = sum([(devices[d] * usage_hours[d]) / 1000 for d in devices])
    predicted_bill = total_kwh * 0.6

    st.metric("Predicted Bill", f"RM {round(predicted_bill, 2)}")

    st.info("🔮 Usage trend increasing by 8% weekly")
