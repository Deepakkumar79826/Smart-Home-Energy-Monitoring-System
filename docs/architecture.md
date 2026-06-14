# Smart Home Energy Monitoring System

## Architecture

```text
+----------------------+
| Sensor Simulator     |
| Voltage Generator    |
| Current Generator    |
+----------+-----------+
           |
           v
+----------------------+
| Energy Calculator    |
| Power Calculation    |
| Energy Calculation   |
+----------+-----------+
           |
           v
+----------------------+
| Cost Estimator       |
| Tariff Engine        |
+----------+-----------+
           |
           v
+----------------------+
| Alert Engine         |
| Threshold Detection  |
+----------+-----------+
           |
           v
+----------------------+
| CSV Logger           |
| MQTT Publisher       |
+----------+-----------+
           |
           v
+----------------------+
| Streamlit Dashboard  |
| Analytics Engine     |
| PDF Report Generator |
+----------------------+
```

## Data Flow

Voltage
↓
Current
↓
Power
↓
Energy
↓
Cost
↓
Alert
↓
CSV
↓
Dashboard
↓
PDF Report

## Features

- Real-Time Monitoring
- Energy Tracking
- Cost Estimation
- Alert Generation
- CSV Logging
- MQTT Integration
- Dashboard Analytics
- PDF Reports