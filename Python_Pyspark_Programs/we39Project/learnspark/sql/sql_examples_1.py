#How we are going to learn Spark SQL:
#1. how to create dataframes from different sources by inferring the schema automatically or manually
#2. how to apply transformations using DSL(DF) and SQL(view) (main portition level 1)
#3. how to store the transformed data to targets
#4. how to create pipelines using different data processing techniques by connecting with different sources/targets (level 2)
#5. how to create reusable frameworks (level 3) - masking engine, reusable transformation, move engine, quality suite, audit engine
#6. how to submit the jobs/monitor/log analysis/packaging and deployment ...
#7. performance tuning ...
#when can we go for Spark SQL - if the data is structured/semi structured
# when we go for rdd to spark sql - if the data unstructured or if we need to pre process the raw data
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("we39 spark sql").master("local[*]").getOrCreate() #This line created spark context and sql context objects
spark.sparkContext.setLogLevel("ERROR")

#How to create Dataframes
#below way of creating rdd to df is used very rarely in the Orgs by the developers, rather we use the second method of using modules/functions
#1. Create dataframes from RDD (if the data unstructured or if we need to pre process the raw data to make it ready for DF to consume)
#a. using named list of columns
#1. Create an RDD
filerdd1=spark.sparkContext.textFile("file:///home/hduser/cust1.txt")
#2. Iterate on every filerdd1 of rdd, split using the delimiter, Iterate on every splitted elements apply the respective
# datatype to get the SchemaRDD
schemardd2=filerdd1.map(lambda x:x.split(",")).map(lambda x:(int(x[0]),x[1]))

#3. Create column list as per the the structure of data
collist=["cid","city"]

# 4. Convert the schemaRDD to DF using toDF or createDataFrame apply the column names by calling the column lists
df1=schemardd2.toDF(collist)
df1.printSchema()
df1.select("city").distinct().show() #we are good to write DSLs here

df1=spark.createDataFrame(schemardd2,collist)
df1.printSchema()
df1.select("city").distinct().show() #we are good to write DSLs here

#b. using concept of reflection (reflect each row of the schema rdd to the Row class to get the row objects created)
#2. Iterate on every filerdd1 of rdd, split using the delimiter, Iterate on every splitted elements apply the Row function to define
# name and respective datatype to get the SchemaRDD
from pyspark.sql import Row
schemardd2=filerdd1.map(lambda x:x.split(",")).map(lambda x:Row(cid=int(x[0]),city=x[1]))

# 4. (skip step 3 of creating column list is no more needed) Convert the schemaRDD to DF using toDF or createDataFrame apply the column names by calling the column lists
df1=schemardd2.toDF()
df1.printSchema()
df1.select("city").distinct().show() #we are good to write DSLs here

df1=spark.createDataFrame(schemardd2)
df1.printSchema()
df1.select("city").distinct().show() #we are good to write DSLs here

#2. Create dataframes using the modules (builtin (csv, orc, parquet, jdbc,table) / external (cloud, api, nosql))
# or programatically
df_csv1=spark.read.csv("file:///home/hduser/sparkdata/nyse.csv",header=True,sep='~',inferSchema=True)
df_csv1=spark.read.option("header","True").option("delimiter","~").option("inferschema","true").csv("file:///home/hduser/sparkdata/nyse.csv")

# How to change the column names or define column names for the dataframe at the time of creation
#if header is available, i will go simply with header=true
df_csv1=spark.read.option("header","True").option("delimiter","~").option("inferschema","true").csv("file:///home/hduser/sparkdata/nyse.csv")
#if header is not available, i will go simply toDF("column list")
df_csv1=spark.read.option("delimiter","~").option("inferschema","true").csv("file:///home/hduser/sparkdata/nyse_noheader.csv").toDF("exchange","stock","closerate")

#if header is available but need to change most of the column name
df_csv1=spark.read.option("header","True").option("delimiter","~").option("inferschema","true").csv("file:///home/hduser/sparkdata/nyse.csv").toDF("exc","sto","rate")

#if header is available but need to change few of the column name
df_csv1=spark.read.option("header","True").option("delimiter","~").option("inferschema","true").csv("file:///home/hduser/sparkdata/nyse.csv")
df_csv1=df_csv1.withColumnRenamed("closerate","rate")

#If header is available need to change few column name after applying some transformations/aggregations then use .alias()
from pyspark.sql.functions import *
df_csv1=df_csv1.groupBy("exchange").agg(count(col("rate")).alias("cnt")).show()
df_csv2=df_csv1.groupBy("exchange").agg(count(col("closerate")),sum(col("closerate"))).withColumnRenamed("count(closerate)","cnt").withColumnRenamed("sum(closerate)","sumclose").where("cnt >2 and sumclose>50").show()
df_csv2=df_csv1.groupBy("exchange").agg(count(col("closerate")).alias("cnt"),sum(col("closerate")).alias("sumclose")).where("cnt >2 and sumclose>50").show()

#If header is available need to change few column name after applying some transformations/aggregations then use sql as function also
df_csv1.createOrReplaceTempView("view1")
df_csv2=spark.sql("select exchange,stock,closerate rate from view1")

#If header is available need to change name and the datatype also - we need to go with custom schema, use schema option
from pyspark.sql.types import StringType,StructType,StructField,DecimalType
#struct1=StructType([StructField("columnname",sqldatatype,nullable true/false)])
struct1=StructType([StructField("exc",StringType(),False),StructField("stock",StringType(),True),StructField("closerate",DecimalType(10,2),False)])
df_csv1=spark.read.csv("file:///home/hduser/sparkdata/nyse.csv",header=True,sep='~',schema=struct1)
df_csv1.printSchema()
df_csv1.show()


#writing the df into files/tables
df_csv1.write.mode("overwrite").json("file:///home/hduser/sparkdata/nysejson/")
df_csv1.write.mode("overwrite").partitionBy("exchange").orc("file:///home/hduser/sparkdata/nyseorc/")
df_csv1.write.mode("overwrite").orc("file:///home/hduser/sparkdata/nyseorc/")
df_csv1.write.mode("overwrite").parquet("file:///home/hduser/sparkdata/nyseparquet/")
df_csv1.write.mode("overwrite").bucketBy(3,"stock").saveAsTable("hive_json_tbl1")
df_csv1.write.mode("overwrite").partitionBy("exchange").saveAsTable("hive_json_part_tbl1")
df_csv1.write.mode("overwrite").partitionBy("exchange").bucketBy(3,"stock").saveAsTable("hive_json_tbl2")

#spark sql can handle semi structured data
df_json1=spark.read.json("file:///home/hduser/sparkdata/nysejson/",columnNameOfCorruptRecord="rejected_data")

#reading orc data
df_orc1=spark.read.orc("file:///home/hduser/sparkdata/nyseorc/")

#reading parquet data
df_parquet1=spark.read.parquet("file:///home/hduser/sparkdata/nyseparquet/")

#read data from hive table
df_hive1=spark.read.table("hive_json_tbl2")

#read data from other database tables
sqldf = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost/custdb").option("driver","com.mysql.jdbc.Driver").option("dbtable","custprof").option("user", "root").option("password", "Root123$").load()

#can we tranfer data between one spark app to another ? not directly, but by persisting the app1 data to fs/hive table in a serialized format
# raw(csv) -> DE curation -> parquet -> new spark app DS model -> hive table -> visualization





