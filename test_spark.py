import os
import tempfile

# Force Spark to use a known temp folder
os.environ["TMP"] = r"C:\Temp"
os.environ["TEMP"] = r"C:\Temp"

os.makedirs(r"C:\Temp", exist_ok=True)

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("Test")
    .config("spark.local.dir", r"C:\Temp")
    .getOrCreate()
)

print("Spark Started Successfully!")

spark.stop()