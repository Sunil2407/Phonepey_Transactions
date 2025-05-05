# Phonepey_Transactions
# PhonePe Pulse Data Analysis and Visualization Project

## Overview

With the rise of digital payment platforms like *PhonePe*, analyzing transaction data, user engagement, and insurance behavior is vital for driving business strategies. This project focuses on extracting, analyzing, and visualizing data from PhonePe to generate actionable business insights.

## Objectives

- Understand and analyze digital transaction patterns.
- Visualize payment data at state, district, and pincode levels.
- Segment users for targeted marketing and product development.
- Explore user engagement, insurance trends, and payment category performance.

---

## Business Use Cases

- *Customer Segmentation:* Identify user groups based on behavior and spending.
- *Fraud Detection:* Analyze anomalies and patterns for early fraud detection.
- *Geographical Insights:* Study payment trends across regions for targeted strategy.
- *Payment Category Performance:* Determine which payment categories are most used.
- *User Engagement Analysis:* Track user activity over time.
- *Product Development:* Leverage insights to build new features.
- *Insurance Analytics:* Explore how insurance products are performing.
- *Marketing Optimization:* Align campaigns with transaction behavior.
- *Trend Analysis:* Detect shifts in user behavior and volume over time.
- *Competitive Benchmarking:* Compare performance against competitors.

---

## Project Workflow

### 1. Data Extraction

- Cloned PhonePe Pulse GitHub data repository.
- Transformed JSON files into structured formats.

### 2. SQL Database Setup

- Created a *MySQL/PostgreSQL* database.
- Created tables for:
  - aggregateusers
  - aggregatetransaction
  - aggregateinsurance
  - mapusers
  - mapmap
  - mapinsurance
  - topusers
  - topmap
  - topinsurance

### 3. SQL Queries

Executed complex SQL queries for:
- Top-performing states and districts.
- Transaction volume trends.
- Quarterly and yearly comparisons.
- Category-wise analysis.
- Insurance transaction trends.

---

## Data Analysis using Python

- *Tools:* Pandas, Matplotlib, Seaborn
- Loaded SQL outputs into Pandas DataFrames.
- Created visualizations:
  - Bar charts for top states/districts.
  - Pie charts for category-wise usage.
  - Line plots for trend analysis.

---

## Dashboard

### Streamlit Dashboard
- Built an interactive web app using *Streamlit*.
- Enabled real-time filtering by state, year, and category.

### Power BI/Tableau Dashboard
- Visual storytelling with maps and trend lines.
- Drill-downs by state, district, and pincode.

---

## Key Insights

- Identified top 5 states contributing to total digital transactions.
- Detected peak transaction periods and seasonal fluctuations.
- Found underperforming regions and suggested targeted strategies.
- Highlighted surge in insurance adoption in select regions.

---

## Tools and Technologies

- *Database:* MySQL / PostgreSQL
- *Languages:* SQL, Python
- *Libraries:* Pandas, Seaborn, Matplotlib
- *Dashboarding:* Streamlit, Power BI, Tableau

---

## Results

- Gained expertise in real-world data handling.
- Demonstrated ability to convert business requirements into technical analysis.
- Delivered end-to-end analytical workflow from data ingestion to visualization.
- Showcased ability to build interactive and insightful dashboards.

---

## Folder Structure

PhonePe-Data-Analysis/ │ ├── SQL/                      # SQL scripts for analysis ├── Python/                   # Jupyter notebooks for analysis ├── Dashboard/                # Streamlit or Power BI dashboard files ├── Visualizations/           # PNGs of key charts ├── README.md                 # Project readme └── requirements.txt          # Python packages

---

## How to Run

1. Clone the repo:

git clone https://github.com/your-username/PhonePe-Data-Analysis.git

2. Set up the database and load data.

3. Run the Streamlit dashboard:

streamlit run dashboard/app.py

4. Explore Power BI dashboard
