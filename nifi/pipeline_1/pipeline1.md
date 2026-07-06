# Pipeline 1: Data Ingestion using Apache NiFi

## Overview

Pipeline 1 is the first stage of the Netflix Data Engineering Project. Its primary objective is to ingest the raw Netflix dataset into the Apache NiFi workflow. This pipeline establishes the foundation of the ETL process by reading the source CSV file and preparing it for further processing in subsequent pipelines.

---

# Objective

The objective of Pipeline 1 is to automate the ingestion of the Netflix dataset into Apache NiFi for downstream ETL processing.

---

# Technologies Used

- Apache NiFi 1.28.1
- CSV Dataset
- Windows Operating System

---

# Input

**Source File**

```
netflix_titles.csv
```

**Input Format**

- CSV (Comma Separated Values)

---

# Apache NiFi Components Used

## GetFile

Purpose:
Reads the Netflix CSV dataset from the local input directory.

Configuration:
- Input Directory
- Keep Source File (True)

---

## UpdateAttribute (if used)

Purpose:
Adds metadata to the FlowFile for easier tracking and processing.

---

## PutFile

Purpose:
Stores the ingested dataset into the Pipeline 1 output directory.

---

# Workflow

```
Netflix CSV
      │
      ▼
   GetFile
      │
      ▼
UpdateAttribute
      │
      ▼
   PutFile
```

---

# Input Directory

```
pipeline1/input/
```

---

# Output Directory

```
pipeline1/output/
```

---

# Data Flow

1. Apache NiFi monitors the input directory.
2. When a CSV file is detected, GetFile reads the file.
3. Optional metadata is attached using UpdateAttribute.
4. The dataset is written into the output folder using PutFile.
5. The processed FlowFile becomes available for Pipeline 2.

---

# Output

- Successfully ingested Netflix dataset.
- CSV file stored inside the Pipeline 1 output folder.

---

# Business Use Case

Organizations receive datasets from multiple external sources every day. Pipeline 1 automates the ingestion process by eliminating manual file movement and ensuring that incoming data is consistently available for downstream ETL workflows.

---

# Learning Outcomes

Through this pipeline, the following Apache NiFi concepts were learned:

- Data ingestion
- FlowFile creation
- File monitoring
- File movement
- Basic ETL workflow
- Apache NiFi processor configuration

---

# Folder Structure

```
pipeline1/
│
├── input/
├── output/
└── template/
    └── Pipeline_1.xml
```

---

# Conclusion

Pipeline 1 serves as the entry point of the Netflix Data Engineering Project. It demonstrates how Apache NiFi can automate data ingestion by continuously monitoring directories and processing incoming files without manual intervention. This pipeline provides the foundation for all subsequent ETL operations.