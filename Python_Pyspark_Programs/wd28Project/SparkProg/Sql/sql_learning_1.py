#How we are going to learn Spark SQL (ETL):
#1. how to create dataframes from RDD using named list/reflection (least bothered) and
# how to create DF from different sources by inferring the schema automatically or manually defining the schema (very important)
#3. how to store the transformed data to targets
#2. how to apply transformations using DSL(DF) and SQL(view) (main portition level 1)
#4. how to create pipelines using different data processing techniques by connecting with different sources/targets (level 2)
#5. how to create reusable frameworks (level 3) - masking engine, reusable transformation, data movement automation engine, quality suite, audit engine, data observability, data modernization...
#6. how to submit the jobs/monitor/log analysis/packaging and deployment ...
#7. performance tuning ...
from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local[*]").appName("wd28 first spark sql app").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# How to Create Dataframes
#1. Create DF from RDD (regularly we don't create RDD then convert to DF, rarely if we have to convert or clean the RDD data
# before converting to DF)
spark.sparkContext.parallelize(["hello","hi","gm"]).flatMap(lambda x:x.split(",")).map(lambda x:[x]).toDF(["greetings"]).show()
#1. Create an RDD
filerdd1=spark.sparkContext.textFile("file:///home/hduser/cust1.txt")
#2. Create column list as per the the structure of data
#1,Chennai
#2,Chennai
#3,Hyd
collist=["id","city"]

#3. Iterate on every filerdd1 of rdd, split on the delimiter
splitrdd2=filerdd1.map(lambda x:x.split(","))
#[['1', 'Chennai'], ['2', 'Chennai'], ['3', 'Hyd'], ['4', 'Chennai'], ['3', 'Hyd'], ['2', 'Chennai']]

#4. Iterate on every elements of splitrdd2  apply the respective datatype (SchemaedRDD)
schemardd3=splitrdd2.map(lambda x:(int(x[0]),x[1]))

# 5. Convert the schemaedRDD to DF using toDF or createDataFrame apply the column names by calling the column lists
dftoDF=schemardd3.toDF(collist)
dfcreateDF=spark.createDataFrame(schemardd3,collist)

# 6. Ready to write DSL (Domain specific Language)
dftoDF.repartition(10).select("*").dropDuplicates().show()
dfcreateDF.repartition(10).select("*").dropDuplicates().show()

#4. Reflection - Iterate on every elements of splitrdd2  apply the respective datatype and column names also (SchemaedRDD)
from pyspark.sql import Row
schemaRowrdd3=splitrdd2.map(lambda x:Row(id=int(x[0]),city=x[1]))

# 5. Convert the schemaedRDD to DF using toDF or createDataFrame apply the column names by calling the column lists
dftoDF=schemaRowrdd3.toDF()
dfcreateDF=spark.createDataFrame(schemaRowrdd3)

# 6. Ready to write DSL (Domain specific Language)
dftoDF.repartition(10).select("*").dropDuplicates().show()
dfcreateDF.repartition(10).select("*").dropDuplicates().show()

#2. Creating dataframe using different modules
#file systems as sources (lfs, hdfs, windows, cloudFS)
#csv module:
df1=spark.read.csv("file:///home/hduser/sparkdata/usdata.csv") #csv native (databricks) methodology
databricks_df1=spark.read.option("delimiter","~").option("header","true").option("inferschema","true").csv("file:///home/hduser/sparkdata/nyse.csv")
apache_df1=spark.read.csv("file:///home/hduser/sparkdata/nyse.csv",sep='~',header="true",inferSchema="true")

#json module:
#orc module:
#parquet module:
#table module:
#jdbc module:
#external connector module (any)

# at the time of creation - How to change the column names or define column names for the dataframe if no header is present
#if header is available, i will go simply with header=true
df1=spark.read.csv("file:///home/hduser/sparkdata/nyse.csv",sep='~',header='true',inferSchema="true")

#if header is available but need to change MOST of the column names at the time of creating the DF we use toDF("column list")
df1=spark.read.csv("file:///home/hduser/sparkdata/nyse.csv",sep='~',header='true',inferSchema="true").toDF("exch","sto","rate")

#if header is not available, i can mention my own column names, i will go simply toDF("column list") at the time of creating the DF
df1=spark.read.csv("file:///home/hduser/sparkdata/nyse_noheader.csv",sep='~',header='false',inferSchema="true").toDF("exch","sto","rate")

#Is it possible to change the column names after creating the DF - if header is available but need to change FEW of the column names (we will learn more in detail in the transformation part)
df1=spark.read.csv("file:///home/hduser/sparkdata/nyse.csv",sep='~',header='true',inferSchema="true")
df1=df1.withColumnRenamed("closerate","rate").withColumnRenamed("stock","sto")

#If header is available need to change few column names after applying some transformations/aggregations then use .alias()
df1=spark.read.csv("file:///home/hduser/sparkdata/nyse.csv",sep='~',header='true',inferSchema="true")
from pyspark.sql.functions import count,avg
df2=df1.groupby("exchange").agg(count("closerate").alias("cnt"),avg("closerate").alias("avg")).show() #DSL query
df2=df1.groupby("exchange").agg(count("closerate"),avg("closerate")).withColumnRenamed("count(closerate)","cnt").show() #DSL query

#If header is available need to change few column name after applying some transformations/aggregations then use sql 'as' clause also to change the column names
df1.createOrReplaceTempView("view1")
spark.sql("select exchange,count(closerate) as cnt,avg(closerate) avg from view1 group by exchange").show()

# At the time of creating DF - If header is available need to change name and the datatype also - we need to go with custom schema, use schema option (important)
#define the structure and apply the structure to the DF rather than asking spark to inferschema

#stock_schema1=StructType([StructField("colname",sqldatatype,nullable?),StructField("colname",sqldatatype,nullable?)...])
from pyspark.sql.types import StructType,StructField,StringType,DecimalType
stock_schema1=StructType([StructField("exch",StringType(),True),StructField("sto",StringType(),True),StructField("rate",DecimalType(10,2),True)])
df1=spark.read.csv("file:///home/hduser/sparkdata/nyse.csv",sep='~',header='true',schema=stock_schema1)
df1.printSchema()
#writing the df into files/tables
