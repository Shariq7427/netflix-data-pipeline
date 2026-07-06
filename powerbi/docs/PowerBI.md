# Power BI Dashboard

## Overview

The Power BI dashboard provides an interactive visualization of the Netflix dataset processed through the ETL pipeline. It helps analyze the distribution of Netflix content using KPIs, charts, and filters to support business decision-making.

---

# Dashboard Objectives

- Visualize Netflix content distribution.
- Compare Movies and TV Shows.
- Analyze ratings across titles.
- Identify top content-producing countries.
- Observe release year trends.
- Enable interactive filtering using slicers.

---

# Data Source

- Dataset: `netflix_titles.csv`
- Source: Kaggle Netflix Dataset
- Records: Approximately 8,800 titles
- Imported from PostgreSQL after ETL processing.

---

# KPIs

## 1. Total Titles

Displays the total number of Netflix titles available in the dataset.

Business Value:
Provides an overall measure of the content library.

---

## 2. Total Movies

Displays the total number of movies.

Business Value:
Helps compare movie content against TV shows.

---

## 3. Total TV Shows

Displays the total number of TV shows.

Business Value:
Measures Netflix's television content.

---

## 4. Average Release Year

Displays the average release year of all titles.

Business Value:
Provides an indication of the age of the content available on Netflix.

---

# Visualizations

## Content Type Distribution

Visual Type:
Donut Chart

Fields Used:
- Legend: Type
- Values: Count of Titles

Purpose:
Shows the proportion of Movies and TV Shows.

---

## Content Rating Distribution

Visual Type:
Clustered Bar Chart

Fields Used:
- Axis: Rating
- Values: Count of Titles

Purpose:
Displays the distribution of maturity ratings.

---

## Top 10 Content Producing Countries

Visual Type:
Clustered Bar Chart

Fields Used:
- Axis: Country
- Values: Count of Titles

Purpose:
Identifies the countries contributing the highest number of titles.

---

## Netflix Content Release Trend

Visual Type:
Line Chart

Fields Used:
- X-Axis: Release Year
- Y-Axis: Count of Titles

Purpose:
Shows how Netflix content production has changed over time.

---

# Interactive Filters

The dashboard includes slicers for:

- Content Type
- Country
- Release Year

These filters update all dashboard visuals simultaneously.

---

# Key Insights

- Movies represent a larger share of Netflix content than TV Shows.
- TV-MA and TV-14 are among the most common content ratings.
- The United States contributes the highest number of Netflix titles.
- Netflix content production has increased significantly over recent years.

---

# Tools Used

- Microsoft Power BI Desktop
- PostgreSQL
- Apache NiFi
- Netflix Dataset

---

# Project Structure

powerbi/
│
├── dashboard/
│   └── Netflix_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard_overview.png
│   ├── kpi_cards.png
│   ├── charts.png
│   └── filters.png
│
├── data/
│   └── netflix_titles.csv
│
└── README.md

---

# Learning Outcomes

This dashboard demonstrates:

- KPI creation
- Interactive dashboards
- Data visualization
- Business intelligence reporting
- Dashboard filtering using slicers
- Storytelling with data

---

# Conclusion

The Power BI dashboard transforms the processed Netflix dataset into an interactive business intelligence solution. It enables users to explore Netflix content through KPIs, charts, and filters, providing meaningful insights into content distribution, ratings, production trends, and geographical availability.