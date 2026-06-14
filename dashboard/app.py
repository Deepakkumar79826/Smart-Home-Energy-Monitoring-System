import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

import streamlit as st
import pandas as pd
import plotly.express as px

from python_simulation.analytics import Analytics
from python_simulation.report_generator import ReportGenerator

st.set_page_config(
    page_title="Smart Home Energy Dashboard",
    page_icon="⚡",
    layout="wide"
)

CSV_FILE = "data/energy_log.csv"

st.title("⚡ Smart Home Energy Monitoring Dashboard")

if not os.path.exists(CSV_FILE):

    st.warning(
        "No energy data found.\n\nRun main.py first."
    )

    st.stop()

df = pd.read_csv(CSV_FILE)

analytics = Analytics(CSV_FILE)

st.sidebar.header("Dashboard Controls")

refresh = st.sidebar.button(
    "🔄 Refresh Data"
)

if refresh:
    st.rerun()

st.sidebar.success(
    f"Records Loaded: {len(df)}"
)

# ==========================
# METRIC CARDS
# ==========================

latest = df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Voltage (V)",
    round(latest["voltage"], 2)
)

col2.metric(
    "Current (A)",
    round(latest["current"], 2)
)

col3.metric(
    "Power (W)",
    round(latest["power"], 2)
)

col4.metric(
    "Cost (₹)",
    round(latest["cost"], 2)
)

st.divider()

# ==========================
# ANALYTICS
# ==========================

st.subheader("📊 Analytics Overview")

a1, a2, a3, a4 = st.columns(4)

a1.metric(
    "Average Voltage",
    analytics.average_voltage()
)

a2.metric(
    "Average Current",
    analytics.average_current()
)

a3.metric(
    "Average Power",
    analytics.average_power()
)

a4.metric(
    "Peak Power",
    analytics.peak_power()
)

st.divider()

# ==========================
# POWER GRAPH
# ==========================

st.subheader(
    "⚡ Power Consumption Trend"
)

power_chart = px.line(
    df,
    x="timestamp",
    y="power",
    title="Power Usage Over Time"
)

st.plotly_chart(
    power_chart,
    use_container_width=True
)

# ==========================
# ENERGY GRAPH
# ==========================

st.subheader(
    "🔋 Energy Consumption Trend"
)

energy_chart = px.line(
    df,
    x="timestamp",
    y="energy",
    title="Energy Usage (kWh)"
)

st.plotly_chart(
    energy_chart,
    use_container_width=True
)

# ==========================
# COST GRAPH
# ==========================

st.subheader(
    "💰 Cost Trend"
)

cost_chart = px.line(
    df,
    x="timestamp",
    y="cost",
    title="Estimated Electricity Cost"
)

st.plotly_chart(
    cost_chart,
    use_container_width=True
)

# ==========================
# ALERT SECTION
# ==========================

st.subheader(
    "🚨 Alert Status"
)

high_alerts = df[
    df["alert"] ==
    "HIGH CONSUMPTION"
]

if len(high_alerts) > 0:

    st.error(
        f"{len(high_alerts)} High Consumption Events Detected"
    )

else:

    st.success(
        "No High Consumption Events"
    )

# ==========================
# RAW DATA
# ==========================

st.subheader(
    "📄 Energy Logs"
)

st.dataframe(
    df.tail(100),
    use_container_width=True
)

# ==========================
# CSV DOWNLOAD
# ==========================

st.download_button(
    label="⬇ Download CSV",
    data=df.to_csv(index=False),
    file_name="energy_log.csv",
    mime="text/csv"
)

# ==========================
# REPORT SUMMARY
# ==========================

generator = ReportGenerator(
    CSV_FILE
)

summary = generator.summary()

st.subheader(
    "📋 Report Summary"
)

st.json(summary)

st.success(
    "Dashboard Loaded Successfully"
)