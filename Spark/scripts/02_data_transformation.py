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
from pyspark.sql.functions import col, trim, to_date

from Spark.config import PARQUET_OUTPUT, TRANSFORMED_OUTPUT

# -----------------------------------------------------
# Spark Session
# -----------------------------------------------------

spark = (
    SparkSession.builder
    .appName("Netflix Data Transformation")
    .config("spark.hadoop.io.native.lib.available", "false")
    .getOrCreate()
)

print("=" * 60)
print("PHASE 2 - DATA TRANSFORMATION")
print("=" * 60)

# -----------------------------------------------------
# Read Parquet
# -----------------------------------------------------

df = spark.read.parquet(PARQUET_OUTPUT)

print("Original Records:", df.count())

# -----------------------------------------------------
# Cleaning
# -----------------------------------------------------

df = df.dropDuplicates()

df = df.dropna(subset=["title"])

string_columns = [
    "title",
    "director",
    "country",
    "rating"
]

for column in string_columns:
    if column in df.columns:
        df = df.withColumn(column, trim(col(column)))

# Clean and convert date
df = df.withColumn(
    "date_added",
    to_date(
        trim(col("date_added")),
        "MMMM d, yyyy"
    )
)

df = df.withColumn(
    "release_year",
    col("release_year").cast("int")
)

print("Cleaned Records:", df.count())

df.printSchema()

df.show(5, truncate=False)

# -----------------------------------------------------
# Save
# -----------------------------------------------------

df.write.mode("overwrite").parquet(TRANSFORMED_OUTPUT)

print("\nSaved to:")
print(TRANSFORMED_OUTPUT)

spark.stop()

print("\nTransformation Completed Successfully!")