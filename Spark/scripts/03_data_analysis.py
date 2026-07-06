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
from Spark.config import TRANSFORMED_OUTPUT

# -----------------------------------------------------
# Output Folder
# -----------------------------------------------------

REPORT_OUTPUT = os.path.join(
    os.path.dirname(TRANSFORMED_OUTPUT),
    "reports"
)

# -----------------------------------------------------
# Spark Session
# -----------------------------------------------------

spark = (
    SparkSession.builder
    .appName("Netflix Data Analysis")
    .config("spark.hadoop.io.native.lib.available", "false")
    .getOrCreate()
)

print("=" * 60)
print("PHASE 3 - DATA ANALYSIS")
print("=" * 60)

# -----------------------------------------------------
# Read Cleaned Data
# -----------------------------------------------------

df = spark.read.parquet(TRANSFORMED_OUTPUT)

print("\nTotal Records:", df.count())

# =====================================================
# 1. Movies vs TV Shows
# =====================================================

print("\nMovies vs TV Shows")

type_count = df.groupBy("type").count()

type_count.show()

type_count.write.mode("overwrite").option(
    "header", True
).csv(os.path.join(REPORT_OUTPUT, "type_count"))

# =====================================================
# 2. Rating Distribution
# =====================================================

print("\nRating Distribution")

rating = (
    df.groupBy("rating")
    .count()
    .orderBy("count", ascending=False)
)

rating.show()

rating.write.mode("overwrite").option(
    "header", True
).csv(os.path.join(REPORT_OUTPUT, "rating_distribution"))

# =====================================================
# 3. Top Countries
# =====================================================

print("\nTop Countries")

country = (
    df.groupBy("country")
    .count()
    .orderBy("count", ascending=False)
)

country.show(10, truncate=False)

country.write.mode("overwrite").option(
    "header", True
).csv(os.path.join(REPORT_OUTPUT, "top_countries"))

# =====================================================
# 4. Top Directors
# =====================================================

print("\nTop Directors")

director = (
    df.filter(df.director.isNotNull())
    .groupBy("director")
    .count()
    .orderBy("count", ascending=False)
)

director.show(10, truncate=False)

director.write.mode("overwrite").option(
    "header", True
).csv(os.path.join(REPORT_OUTPUT, "top_directors"))

# =====================================================
# 5. Movies Per Year
# =====================================================

print("\nMovies Released Per Year")

release = (
    df.groupBy("release_year")
    .count()
    .orderBy("release_year")
)

release.show()

release.write.mode("overwrite").option(
    "header", True
).csv(os.path.join(REPORT_OUTPUT, "release_year"))

spark.stop()

print("\nAnalysis Completed Successfully!")