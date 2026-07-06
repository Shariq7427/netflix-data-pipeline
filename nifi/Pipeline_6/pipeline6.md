# Pipeline 6: Data Filtering and Classification using Apache NiFi

## Overview

Pipeline 6 is the final stage of the Apache NiFi workflow in the Netflix Data Engineering Project. This pipeline reads the CSV dataset generated in Pipeline 5 and separates the records into two categories: **Movies** and **TV Shows**. The classification is performed using SQL queries within the QueryRecord processor, demonstrating business-rule implementation in an ETL workflow.

---

# Objective

The objective of Pipeline 6 is to classify Netflix content based on its type and generate two separate CSV datasets:

- Movies
- TV Shows

This pipeline demonstrates data filtering and routing using SQL-based record processing.

---

# Technologies Used

- Apache NiFi 1.28.1
- CSV
- QueryRecord
- CSVReader
- CSVRecordSetWriter

---

# Input

Source:

```
Pipeline 5 Output
```

Input Format:

```
CSV
```

---

# Apache NiFi Components Used

## GetFile

Purpose:

Reads the CSV file produced by Pipeline 5.

Configuration:

- Input Directory
- Keep Source File = True

---

## QueryRecord

Purpose:

Executes SQL queries on CSV records and creates multiple output relationships based on business rules.

Configuration:

Record Reader

```
CSVReader
```

Record Writer

```
CSVRecordSetWriter
```

Dynamic Properties:

Movies

```sql
SELECT * FROM FLOWFILE
WHERE type='Movie'
```

TV Shows

```sql
SELECT * FROM FLOWFILE
WHERE type='TV Show'
```

---

## CSVReader

Purpose:

Reads CSV records and converts them into Apache NiFi record objects.

---

## CSVRecordSetWriter

Purpose:

Writes filtered records back into CSV format.

---

## PutFile (Movies)

Purpose:

Stores Movie records.

Output Folder:

```
pipeline6/output/movies/
```

---

## PutFile (TV Shows)

Purpose:

Stores TV Show records.

Output Folder:

```
pipeline6/output/tvshows/
```

---

# Workflow

```
Pipeline 5 CSV
        │
        ▼
     GetFile
        │
        ▼
    QueryRecord
      │      │
      │      │
      ▼      ▼
 PutFile   PutFile
(Movies) (TV Shows)
```

---

# Data Flow

1. GetFile reads the CSV dataset.
2. QueryRecord loads the CSV into Apache NiFi Record format.
3. SQL queries classify the records based on the **type** column.
4. Movie records are sent to one relationship.
5. TV Show records are sent to another relationship.
6. Two separate CSV files are generated.
7. The classified datasets are stored in separate output folders.

---

# Output

Generated Files:

```
movies.csv
```

```
tvshows.csv
```

Output Locations:

```
pipeline6/output/movies/
```

```
pipeline6/output/tvshows/
```

---

# Business Use Case

Many organizations need to classify data before reporting or analytics. For example:

- Product Categories
- Customer Segments
- Transaction Types
- Content Classification

Pipeline 6 demonstrates how Apache NiFi can automate data categorization using SQL without requiring custom application code.

---

# Learning Outcomes

This pipeline demonstrates:

- QueryRecord processor
- SQL on record-based data
- Dynamic relationships
- CSVReader configuration
- CSVRecordSetWriter configuration
- Data filtering
- Business rule implementation
- Record routing

---

# Folder Structure

```
pipeline6/
│
├── output/
│   ├── movies/
│   └── tvshows/
│
└── template/
    └── Pipeline_6_Split_Movies_TVShows.xml
```

---

# Complete Apache NiFi Workflow

```
Pipeline 1
      │
      ▼
Pipeline 2
      │
      ▼
Pipeline 3
      │
      ▼
PostgreSQL
      │
      ▼
Pipeline 4
(PostgreSQL → JSON)
      │
      ▼
Pipeline 5
(JSON → CSV)
      │
      ▼
Pipeline 6
(CSV → Movies & TV Shows)
```

---

# Conclusion

Pipeline 6 concludes the Apache NiFi implementation of the Netflix Data Engineering Project. It demonstrates SQL-based record filtering and content classification, producing separate datasets for Movies and TV Shows. This pipeline highlights Apache NiFi's capability to implement business logic within ETL workflows using record-oriented processors and SQL queries.