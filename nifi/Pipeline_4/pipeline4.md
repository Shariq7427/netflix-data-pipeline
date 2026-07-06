# Pipeline 4: PostgreSQL to JSON using Apache NiFi

## Overview

Pipeline 4 is the data extraction stage of the Netflix Data Engineering Project. This pipeline reads data from the PostgreSQL data warehouse and exports it into JSON format. It demonstrates how Apache NiFi can connect to relational databases, execute SQL queries, and generate JSON files for downstream applications.

---

# Objective

The objective of Pipeline 4 is to extract Netflix data from PostgreSQL and convert it into JSON format for further processing and data exchange.

---

# Technologies Used

- Apache NiFi 1.28.1
- PostgreSQL
- JDBC Driver
- JSON
- DBCPConnectionPool
- JsonRecordSetWriter

---

# Input

Source:

```
PostgreSQL Database
```

Database:

```
netflix_dw
```

Table:

```
netflix_titles
```

---

# Apache NiFi Components Used

## ExecuteSQLRecord

Purpose:

Executes an SQL query on PostgreSQL and retrieves records.

SQL Query:

```sql
SELECT * FROM netflix_titles;
```

---

## JsonRecordSetWriter

Purpose:

Converts SQL query results into JSON format.

---

## PutFile

Purpose:

Writes the generated JSON file into the Pipeline 4 output directory.

---

## DBCPConnectionPool

Purpose:

Maintains a reusable connection to PostgreSQL.

Configuration:

Database URL

```
jdbc:postgresql://localhost:5432/netflix_dw
```

Database

```
netflix_dw
```

JDBC Driver

```
postgresql-42.7.12.jar
```

---

# Workflow

```
PostgreSQL
      │
      ▼
ExecuteSQLRecord
      │
      ▼
JsonRecordSetWriter
      │
      ▼
   PutFile
      │
      ▼
 JSON Output
```

---

# Output Directory

```
pipeline4/output/
```

Output Format:

```
JSON
```

---

# Data Flow

1. Apache NiFi establishes a connection with PostgreSQL.
2. ExecuteSQLRecord executes the SQL query.
3. Records are retrieved from the `netflix_titles` table.
4. JsonRecordSetWriter converts the records into JSON format.
5. PutFile stores the generated JSON file in the output folder.
6. Pipeline 5 uses this JSON file as its input.

---

# Output

- JSON file containing all Netflix records.
- Successfully exported approximately **8,807 records**.

---

# Business Use Case

JSON is one of the most widely used formats for data exchange between applications, APIs, and cloud platforms. Pipeline 4 demonstrates how enterprise ETL workflows extract relational data and prepare it for downstream systems using a platform-independent format.

---

# Learning Outcomes

This pipeline demonstrates:

- Database extraction
- SQL execution using Apache NiFi
- JDBC connectivity
- JSON generation
- Record-oriented processing
- Data export workflows

---

# Folder Structure

```
pipeline4/
│
├── output/
└── template/
    └── Pipeline_4_PostgreSQL_to_JSON.xml
```

---

# Conclusion

Pipeline 4 represents the **Extract** stage from the PostgreSQL data warehouse. It successfully retrieves Netflix data using SQL and converts it into JSON format, making the dataset portable for downstream processing, integration, and analytics.