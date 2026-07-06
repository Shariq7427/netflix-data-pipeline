# 🎬 Netflix Data Engineering Pipeline & Analytics Dashboard

A complete end-to-end **Data Engineering** project that demonstrates how Netflix data can be ingested, transformed, orchestrated, stored, and visualized using modern data engineering tools.

The project simulates a real-world data pipeline by integrating **Apache Kafka**, **Apache Spark**, **Apache Airflow**, **PostgreSQL**, **Docker**, and **Power BI** to process Netflix content data and generate business insights through interactive dashboards.

---

# 📌 Project Overview

This project demonstrates the complete lifecycle of a modern data engineering pipeline.

The pipeline performs:

- Data Ingestion using Apache Spark
- Data Cleaning & Transformation
- Workflow Scheduling using Apache Airflow
- SQL Layer using PostgreSQL
- Containerization using Docker
- Interactive Business Intelligence Dashboard using Power BI
- Live Analytics Dashboard using Streamlit

---

# 👨‍💻 Team Members

- Mohammad Shariq Ali
- Shiva Sai Addanki
- Sankara Vamsi Raju Sarikonda
- Sai Vinay Pyatla
- Sajan

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Apache Spark | Data Processing |
| Apache Kafka | Data Streaming |
| Apache Airflow | Workflow Orchestration |
| PostgreSQL | SQL Data Warehouse |
| Docker | Containerization |
| Power BI | Business Intelligence Dashboard |
| Streamlit | Live Dashboard |
| Python | Pipeline Development |
| Pandas | Data Analysis |

---

# 🏗 System Architecture

The complete architecture of the project is shown below.

![Architecture](images/architecture.png)

---

# 🔄 Complete Pipeline Workflow

```
Netflix Dataset
        │
        ▼
Apache Spark Data Ingestion
        │
        ▼
Data Cleaning & Transformation
        │
        ▼
Apache Kafka
        │
        ▼
Apache Airflow Scheduling
        │
        ▼
PostgreSQL Database
        │
        ▼
Power BI Dashboard
        │
        ▼
Streamlit Live Dashboard
```

---

# 📂 Project Structure

```
netflix-data-pipeline/
│
├── airflow/
│   ├── dags/
│   ├── docker-compose.yml
│   ├── logs/
│   └── plugins/
│
├── Spark/
│   ├── scripts/
│   └── config.py
│
├── Producer/
│
├── sql/
│   └── create_tables.sql
│
├── dashboard/
│   └── app.py
│
├── powerbi/
│   ├── screenshots/
│   └── dashboard.pbix
│
├── images/
│
├── data/
│
├── output/
│
├── README.md
│
└── requirements.txt
```

---

# ⚙ Data Engineering Pipeline

## Phase 1 — Data Ingestion

The Netflix dataset is loaded using Apache Spark.

Operations performed

- Read CSV Dataset
- Infer Schema
- Display Records
- Store Data as Parquet

---

## Phase 2 — Data Transformation

Spark performs preprocessing before analytics.

Operations

- Remove Duplicate Records
- Remove Null Values
- Trim Text Columns
- Convert Date Formats
- Cast Data Types
- Store Cleaned Dataset

---

## Phase 3 — Apache Kafka

Kafka is configured to simulate streaming architecture.

Components

- Zookeeper
- Kafka Broker
- Kafka Producer

---

## Phase 4 — Apache Airflow

Airflow orchestrates the Spark pipeline using DAGs.

Pipeline Tasks

- Data Ingestion
- Data Transformation

Airflow manages scheduling, execution, monitoring, and dependency management of the ETL workflow.

---

## Phase 5 — SQL Layer

The transformed dataset is loaded into PostgreSQL.

Implemented SQL

- Database Creation
- Table Creation
- Structured Storage
- SQL Analytics Support

---

## Phase 6 — Dashboard Layer

Processed data is visualized using Power BI and Streamlit.

---

# 📊 Live Dashboard

The project includes a **Streamlit Live Dashboard** for interactive exploration of the Netflix dataset.

### Features

- Search Netflix Titles
- Genre Analysis
- Country Analysis
- Rating Distribution
- Movie vs TV Shows
- Release Year Trends
- Interactive Charts

### Live Dashboard Preview

> *(Replace with your Streamlit dashboard screenshot)*

![Live Dashboard](dashboard/dashboard_preview.png)

---

# 📈 Power BI Dashboard

The Power BI dashboard provides business insights using interactive visualizations.

---

## Dashboard Overview

A complete overview of the Netflix dataset.

![Dashboard Overview](powerbi/screenshots/dashboard_overview.png.png)

---

## KPI Cards

Key business metrics include:

- Total Titles
- Movies
- TV Shows
- Directors
- Countries

![KPI Cards](powerbi/screenshots/kpi_cards.png.png)

---

## Dashboard Charts

Interactive charts include

- Movie vs TV Shows
- Country Distribution
- Rating Analysis
- Release Year Trends
- Genre Distribution
- Top Directors

![Charts](powerbi/screenshots/charts.png.png)

---

## Interactive Filters

Dashboard slicers allow users to filter by

- Country
- Rating
- Release Year
- Genre
- Type

![Filters](powerbi/screenshots/filters.png)

---

# 📌 Dashboard Features

## Power BI

- Interactive KPI Cards
- Country-wise Analysis
- Genre Analysis
- Rating Analysis
- Release Year Trends
- Movie vs TV Show Comparison
- Dynamic Filtering

---

## Streamlit Dashboard

- Interactive UI
- Live Filtering
- Search Functionality
- Plotly Charts
- Dataset Statistics
- Real-time Visualization

---

# 📊 Dataset Information

Dataset

Netflix Movies and TV Shows Dataset

Includes

- Movies
- TV Shows
- Directors
- Cast
- Countries
- Ratings
- Genres
- Release Years
- Duration
- Date Added

---

# 🚀 How to Run the Project

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/netflix-data-pipeline.git

cd netflix-data-pipeline
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Spark Ingestion

```bash
python -m Spark.scripts.01_data_ingestion
```

---

## Run Spark Transformation

```bash
python -m Spark.scripts.02_data_transformation
```

---

## Start Kafka

```bash
docker compose up -d
```

---

## Start Airflow

```bash
cd airflow

docker compose up -d
```

Open

```
http://localhost:8080
```

Username

```
admin
```

Password

```
admin
```

---

## Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📊 Business Insights

The dashboard answers several business questions such as

- Which country has the highest Netflix content?
- Which genres dominate Netflix?
- Movie vs TV Show distribution
- Ratings analysis
- Release year trends
- Top contributing directors
- Country-wise content production

---

# 📌 Future Improvements

- Real-time Kafka Streaming
- Spark Structured Streaming
- Cloud Deployment (AWS/Azure/GCP)
- Data Lake Integration
- Machine Learning Recommendation System
- CI/CD Pipeline
- Automated Data Validation

---

# 📷 Project Demonstration

## Architecture

![Architecture](images/architecture.png)

---

## Power BI Dashboard

![Dashboard](powerbi/screenshots/dashboard_overview.png.png)

---

## KPI Cards

![KPI](powerbi/screenshots/kpi_cards.png.png)

---

## Charts

![Charts](powerbi/screenshots/charts.png.png)

---

## Filters

![Filters](powerbi/screenshots/filters.png)

---

## Live Dashboard

> *(Replace with your Streamlit dashboard screenshot.)*

![Live Dashboard](dashboard/dashboard_preview.png)

---

# 📄 License

This project is developed for academic and educational purposes as part of the Master's Data Engineering coursework.

---

# ⭐ Acknowledgements

Special thanks to our course instructor and project team for their guidance and support throughout the development of this project.

---

## Developed By

**Mohammad Shariq Ali**

Master's in Data Engineering

2026