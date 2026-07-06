import os

# -----------------------------------------------------
# Hadoop Configuration
# -----------------------------------------------------

os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"

# -----------------------------------------------------
# Spark Imports
# -----------------------------------------------------

from pyspark.sql import SparkSession
from Spark.config import INPUT_PATH, PARQUET_OUTPUT

# -----------------------------------------------------
# Create Spark Session
# -----------------------------------------------------

spark = (
    SparkSession.builder
    .appName("Netflix Data Ingestion")
    .config("spark.hadoop.io.native.lib.available", "false")
    .getOrCreate()
)

print("=" * 60)
print("NETFLIX DATA ENGINEERING PROJECT")
print("PHASE 1 - DATA INGESTION")
print("=" * 60)

# -----------------------------------------------------
# Read CSV
# -----------------------------------------------------

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .option("quote", '"')
    .option("escape", '"')
    .option("multiLine", True)
    .csv(INPUT_PATH)
)

print("\nDataset Loaded Successfully!")

print("\nSchema:")
df.printSchema()

print("\nTotal Records:")
print(df.count())

print("\nFirst Five Records:")
df.show(5, truncate=False)

# -----------------------------------------------------
# Save as Parquet
# -----------------------------------------------------

df.write.mode("overwrite").parquet(PARQUET_OUTPUT)

print("\nParquet File Saved Successfully!")

spark.stop()

print("\nSpark Session Closed.")