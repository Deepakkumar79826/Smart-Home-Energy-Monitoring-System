# ⚡ Smart Home Energy Monitoring System

## 📌 Overview

The **Smart Home Energy Monitoring System** is an Industry-Oriented IoT project designed to monitor, analyze, and visualize household energy consumption in real time.

This project simulates smart energy monitoring using Python and IoT concepts. It calculates power consumption, energy usage, electricity cost, generates alerts for high energy consumption, logs data into CSV files, and displays analytics through an interactive Streamlit dashboard.

The system demonstrates how modern smart homes and energy management platforms track electricity usage to reduce waste and optimize energy efficiency.

---

## 🎯 Problem Statement

Most homeowners receive electricity bills without knowing which appliances consume the most energy.

This project aims to:

* Monitor energy consumption in real time
* Estimate electricity costs
* Detect excessive power usage
* Generate energy reports
* Visualize energy trends through dashboards

---

## 🚀 Features

### Energy Monitoring

* Real-time Voltage Monitoring
* Real-time Current Monitoring
* Power Consumption Calculation
* Energy Consumption Tracking (kWh)

### Cost Analysis

* Electricity Cost Estimation
* Daily Consumption Projection
* Monthly Consumption Projection

### Alert System

* High Power Consumption Detection
* Threshold-Based Alerts

### Dashboard Analytics

* Interactive Streamlit Dashboard
* Power Trend Visualization
* Energy Usage Charts
* Cost Analysis Graphs
* Alert Monitoring

### Data Management

* CSV Data Logging
* Historical Data Storage
* Report Generation
* Analytics Processing

### IoT Integration

* MQTT Communication Support
* Cloud-Ready Architecture
* Industry-Oriented Design

---

# 🏗 Project Architecture

```text
Voltage Sensor Simulation
            │
            ▼
Current Sensor Simulation
            │
            ▼
      Power Calculation
            │
            ▼
     Energy Calculation
            │
            ▼
      Cost Estimation
            │
            ▼
      Alert Detection
            │
            ▼
       CSV Logging
            │
            ▼
     Streamlit Dashboard
            │
            ▼
      PDF Reporting
```

---

# 📂 Project Structure

```text
Smart-Home-Energy-Monitoring-System/

│
├── main.py
├── requirements.txt
├── .gitignore
├── Dockerfile
│
├── config/
│   └── settings.py
│
├── python_simulation/
│   ├── __init__.py
│   ├── sensor_simulator.py
│   ├── appliance_manager.py
│   ├── energy_calculator.py
│   ├── cost_estimator.py
│   ├── alert_engine.py
│   ├── mqtt_client.py
│   ├── csv_logger.py
│   ├── report_generator.py
│   └── analytics.py
│
├── dashboard/
│   └── app.py
│
├── reports/
│   └── pdf_report.py
│
├── data/
│   ├── appliances.json
│   └── energy_log.csv
│
├── outputs/
│   └── energy_report.pdf
│
├── docs/
│   └── architecture.md
│
└── .github/
    └── workflows/
        └── python-ci.yml
```

---

# 🛠 Technologies Used

### Programming Language

* Python

### Dashboard

* Streamlit

### Data Analysis

* Pandas
* NumPy

### Visualization

* Plotly

### Reporting

* ReportLab

### IoT Communication

* MQTT (Paho MQTT)

### CI/CD

* GitHub Actions

### Containerization

* Docker

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Smart-Home-Energy-Monitoring-System.git

cd Smart-Home-Energy-Monitoring-System
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Start Energy Monitoring

```bash
python main.py
```

This will:

* Generate simulated sensor readings
* Calculate power consumption
* Calculate energy usage
* Estimate electricity cost
* Generate alerts
* Save data into CSV

---

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard Features:

* Real-Time Voltage Monitoring
* Current Monitoring
* Power Usage Tracking
* Energy Analytics
* Cost Estimation
* Alert Monitoring
* Historical Data Visualization

---

## Generate PDF Report

```bash
python reports/pdf_report.py
```

Generated file:

```text
outputs/energy_report.pdf
```

---

# 📊 Sample Output

```text
{
    "voltage": 231.56,
    "current": 4.25,
    "power": 984.13,
    "energy": 0.00125,
    "cost": 0.01,
    "alert": "NORMAL"
}
```

---

# 📈 Dashboard Metrics

* Voltage (V)
* Current (A)
* Power (W)
* Energy (kWh)
* Electricity Cost (₹)
* Peak Power Usage
* Average Power Consumption
* Alert Status

---

# 📋 Future Enhancements

* ESP32 Hardware Integration
* ACS712 Current Sensor Support
* ThingSpeak Integration
* Blynk Integration
* Smart Meter Integration
* AI-Based Consumption Prediction
* Mobile Application
* Email Notifications
* SMS Alerts
* Cloud Database Storage

---

# 📷 Screenshots to Include

* Project Folder Structure
* Streamlit Dashboard
* Power Consumption Graph
* Energy Trend Graph
* Cost Trend Graph
* Alert Monitoring Screen
* CSV Log File
* Generated PDF Report
* GitHub Repository Overview

---

# 🎓 Learning Outcomes

This project demonstrates:

* IoT Fundamentals
* Smart Energy Monitoring
* Python Development
* Dashboard Development
* Data Analytics
* MQTT Communication
* Report Generation
* GitHub Workflow
* CI/CD Pipeline
* Software Architecture Design

---

# 💼 Industry Applications

* Smart Homes
* Commercial Buildings
* Smart Cities
* Energy Management Systems
* Industrial Monitoring
* Utility Analytics Platforms
* Building Automation Systems

---

# 👨‍💻 Author

**Deepak Kumar**

B.Tech Student | IoT Enthusiast | Python Developer | Future Software Engineer

Passionate about building real-world projects in IoT, AI/ML, Data Analytics, Cloud Computing, and Software Development.

---

## ⭐ If you found this project useful, consider giving it a Star!
