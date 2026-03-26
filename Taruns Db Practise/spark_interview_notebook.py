# Spark Basic Practice

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("BasicPractice").getOrCreate()

df = spark.createDataFrame([(1,"Tarun",5000),(2,"Rahul",6000)], ["id","name","salary"])
df.show()
