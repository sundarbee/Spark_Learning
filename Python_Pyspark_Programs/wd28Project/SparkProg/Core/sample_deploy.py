from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
sc=spark.sparkContext
rdd1=sc.textFile("hdfs://localhost:54310/user/hduser/custs",4)
#rdd1=rdd1.repartition(4)
rdd2=rdd1.map(lambda x:x.split(","))
print("sample customers are ")
print(rdd2.take(10))
print("total customers are ")
print(rdd2.count())
rdd3=rdd2.map(lambda x:(int(x[0]),int(x[3]),x[4])).filter(lambda x:x[1]>60)
rdd3.coalesce(1).saveAsTextFile("hdfs:/user/hduser/custoutdata2")

spark.sparkContext.setLogLevel("INFO")
rdd1=spark.sparkContext.textFile("/user/hduser/empdata2/")
rdd1.cache()
rdd2=rdd1.map(lambda x:x.split(","))
local_python_var_kept_in_driver=rdd2.collect()
#collect action will collect the data from rdd (executors) to driver or collect used for
# converting the rdd to normal values
print(local_python_var_kept_in_driver)
rdd3=rdd2.filter(lambda x:len(x)==5)
df1=rdd3.toDF()
df1.cache()
df1.select("*").show(4)
df1.createOrReplaceTempView("view1")
spark.sql("describe view1").show()
spark.sql("select _1,_2,_3 from view1").write.mode("overwrite").orc("/user/hduser/empdataorc")
spark.read.orc("/user/hduser/empdataorc").show()
print("end of spark core, sql application")

#spark-submit --master yarn --executor-memory 2g --num-executors 2 --deploy-mode client /home/hduser/core_submit.py
#spark-submit --master yarn --executor-memory 2g --num-executors 2 --deploy-mode cluster /home/hduser/core_submit.p
