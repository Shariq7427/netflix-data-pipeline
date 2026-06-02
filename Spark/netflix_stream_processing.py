from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NetflixPipeline") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","netflix-events") \
    .load()

query = df.writeStream \
    .format("console") \
    .start()

query.awaitTermination()