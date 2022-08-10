from pyspark.sql import SparkSession
sparkSession = SparkSession.builder.appName("sample session app").master("local[*]").getOrCreate()



