#simple python program to calculate bonus for all employees
sallst=[10000,200000,15000,25000,30000]
bonus=.5
#traditional way of writing the common code
salbonuslst=[]
for sal in sallst:
    salbonuslst.append(sal+(sal*bonus))
print(salbonuslst)

#FBP way of writing the python code
lam=lambda sal:sal+(sal*bonus)
salbonuslst=list(map(lam,sallst)) #features of python programming HOF, lambda func, collection
print(salbonuslst)

def fun1(sal):
    return sal+(sal*bonus)
salbonuslst=list(map(fun1,sallst)) #50 seconds to process this data
print(salbonuslst)

#I am going to conver the above python to a pyspark prog why?
# Ans0: For handling bigdata with high throughput and low latency
# Ans1: for distributed/parallel/multithreading/concurrancy In memory computing
# ans2: improving the performance
# ans3: scalability, fault tolerant

sallst=[10000,200000,15000,25000,30000]
bonus=.5

#traditional way of writing the spark core programming
#from pyspark.context import *
#sc=SparkContext("local[2]","WE39 Application1") #cluster managers - local/standalone/yarn/mesos/kuberneties
#rdd1=sc.parallelize(sallst)
#print(rdd1.getNumPartitions())
#print(rdd1.glom().collect())
#rdd2=rdd1.map(fun1)
#print(rdd2.collect())
#50 seconds to process this data
#salbonuslst=map(fun1,sallst)
#print(salbonuslst)
#sc.stop()

#modern way of writing the spark core programming and spark sql programming
from pyspark.sql.session import SparkSession
spark=SparkSession.builder.master("local[2]").appName("WE39 Application2").getOrCreate()
#the above line has instantiated spark object (used for writing SQL queries),
# sparkContext object (used for writing core programming)
#sql program
spark.read.csv("file:///home/hduser/cust_bkp.txt").show()
#RDD program
print(spark.sparkContext.textFile("file:///home/hduser/cust_bkp.txt").collect())

#We are going to learn the Spark Core Transformations and Actions (not so important interms of working in Orgs,
# rather important to know once for all)
#Creating RDDs
#1. From files, 2. From another RDD, 3. From memory, 4. programatically
sc=spark.sparkContext
rdd1=sc.textFile("file:///home/hduser/cust_bkp.txt")
print(rdd1.getNumPartitions())

#2. From another RDD
rdd1.collect()
#['1,1000', '2,3000', '3,4000', '4,2000']
lam=lambda x:x.split(",")
rdd2=rdd1.map(lam)
#[['1', '1000'], ['2', '3000'], ['3', '4000'], ['4', '2000']]

#3. RDD from memory
rdd2.cache()
rdd3=rdd2.map(lambda x:int(x[3]))
print(rdd3.collect())
print(rdd3.sum())
print(rdd3.count())
rdd2.unpersist()

#4. Create RDD Programatically
rdd1=sc.parallelize(sallst)
print(rdd1.getNumPartitions())
print(rdd1.glom().collect())

#Transformations :
#Passive - if a transformation produces the no. of elements output that is equal to the input
#Active - If a transformation produces the no. of elements output that is not equal to the input
# core - sql - programming lang
#1.map - select - for loop
hadooplines= sc.textFile("hdfs://127.0.0.1:54310/user/hduser/empdata.txt")
print(hadooplines.collect())

rdd2=hadooplines.map(lambda rec:rec.split(","))
#below type can be defined as list(list(string))
#[
# ['ArunKumar', 'chennai', '33', '2016-09-20', '100000'],
# ['Lara', 'chennai', '55', '2016-09-21', '10000'],
# ['vasudevan', 'banglore', '43', '2016-09-23', '90000'],
# ['irfan', 'chennai', '33', '2019-02-20', '20000'],
# ['basith', 'CHENNAI', '29', '2019-04-22']
# ]
rdd3=rdd2.map(lambda delimitedrec:delimitedrec[1].upper())
print(rdd3.collect())

#2.filter - where - for loop and if condition
rdd4=rdd2.filter(lambda delimitedrec:delimitedrec[1].upper()=='CHENNAI')
print(rdd4.collect())

#3. Flatmap - pivot/explode - nested for loop
# convert the data to structured from unstructured.
# below data is of what type?
# structed data with space delimiter but malformed and eligible for becoming semistructured
# how structed - because the below can be related with each other and they are not seperated/unified/seperated.
# for eg. irfan's age is 40 or custid 1 is irfan
# 1 irfan 40
# 2 30 venkat chennai
# 33 chennai kavya
#semi structued format
# {id:1,name:irfan,age:40}
# {id:2,age:30,name:venkat,city:chennai}
# {age:33,city:chennai,name:kavya}
linesrdd= sc.textFile("file:/home/hduser/mrdata/courses.log")
fmrdd=linesrdd.flatMap(lambda x:x.split(" "))
fmrdd.foreach(print)

pythonlist=linesrdd.collect()
#['hadoop spark hadoop spark kafka datascience', 'spark hadoop spark datascience', 'informatica java aws gcp', 'gcp aws azure spark', 'gcp pyspark']
for i in pythonlist:
 for j in i.split(" "):
  print(j)

#4. union function (merge vertically) - if i pass 5 rows with 3 columns in 2 datsets it returns exactly 10 rows with 3 columns
rdd1=sc.textFile("file:///home/hduser/hive/data/custspilot").map(lambda x:x.split(",")).map(lambda x:(x[0],x[1],'NA',x[2],x[3]))
rdd2=sc.textFile("file:///home/hduser/hive/data/custsnopilot").map(lambda x:x.split(",")).map(lambda x:(x[0],x[1],x[2],x[3],x[4]))
rdd3=rdd1.union(rdd2)
rdd4=rdd1.intersection(rdd2)
rdd5=rdd1.subtract(rdd2)

rdd1=sc.textFile("file:///home/hduser/hive/data/custsnopilot").map(lambda x:x.split(",")).map(lambda x:(x[0],x[1],'NA',x[2],x[3]))
rdd2=sc.textFile("file:///home/hduser/hive/data/custsnopilot1").map(lambda x:x.split(",")).map(lambda x:(x[0],x[1],'NA',x[2],x[3]))
rdd1.union(rdd2).count()

#5. Distinct transformation
rdd1.union(rdd2).distinct().count()

#6. Zip (merge horizontally without a join condition) - if i pass 5 rows with 3 columns in 2 datsets it returns exactly 5 rows with 6 columns
#Thumb rules:
# number of rows should be same across both rdds
# number of rows at every partition should be same across both rdds
# Used only when there is no key columns available to join the RDDs otherwise Joins are preferred.
rdd1=sc.textFile("file:/home/hduser/cust1.txt")
rdd2=sc.textFile("file:/home/hduser/cust2.txt")
#rdd1.coalesce(1).zip(rdd2.coalesce(1)).collect()

#Zip With Index - add index to all the elements of the rdd
rdd2=sc.textFile("file:/home/hduser/cust2.txt")
rdd2.zipWithIndex().collect()
#usecase - return only the 3rd row of the rdd
print(rdd2.zipWithIndex().filter(lambda x:x[1]==2).map(lambda x:x[0]).collect())
#I have source datafile with header and footer, I want to remove it?

#Very Important:

#Partition - Horizontal division of data or grouping of data or splitting of data or seperation of data
#why partition - Inorder to divide, distribute, parallelize, throughput, concurrent access/processing of data
#how to control the partitioning - naturally how it occured or using coalesce and repartition how to change the degree of parallelism
#using partitioning concepts in our so far learning and subsequent learning
#HDFS - Blocks, MR - Input split (mappers/reducers), YARN AM/containers, SQOOP Mappers, HIVE Partitions/Buckets,
# SPARK - partitions (naturally partition created (size, Blocks/Input split/mappers/reducers/Containers/Partitions/Buckets),
# change the partition)

#naturally how partitions created when we create rdds (in spark core, we learn spark sql and streaming partitioning soon)
#1. parallelize will go with the number of cores defined in the sparksession object for default partitions
#2. parallelize will go with the second argument value if  i pass a higher or lower number of partitions
#3. textFile will go with the size of data in a chunk of 32mb by default if the size of the data is >32 mb size
#4. textFile will go with the default partition of 2 if the data is <32 mb size
#5. textFile will go with the second argument value if  i override with the higher number of partitions that naturally created

#1
rdd1=sc.parallelize(range(1,100))
print(rdd1.getNumPartitions())

#2
rdd1=sc.parallelize(range(1,100),1)
print(rdd1.getNumPartitions())

#3
rdd1=sc.textFile("file:/home/hduser/sparkdata/youtube_videos.tsv") #size of this data is 143mb
print(rdd1.getNumPartitions())

#4
rdd1=sc.textFile("file:/home/hduser/cust1.txt")
print(rdd1.getNumPartitions())

#5
rdd1=sc.textFile("file:/home/hduser/sparkdata/youtube_videos.tsv",10)
print(rdd1.getNumPartitions()) #10
rdd1=sc.textFile("file:/home/hduser/sparkdata/youtube_videos.tsv",1)
print(rdd1.getNumPartitions()) #5

#Partition Handling
# Difference between coalesce and repartition
# 1. coalese used to reduce no. of partitions - Repartition is used for increase the no. of partition despite it support decrease the no. of partition also
# 2. Coalesce will be applied if the data is aggregated or filtered - Repartition will be applied if the data is joined or unioned
# 3. Coalesce is efficient in distributing the data by avoid shuffling - Repartition is costly because it always shuffles
# 4. Coalesce is costly in maintaining partition size in equally - Repartition maintains partition size equally
# 5. why inequal partition because Coalesce uses range partitioning - Repartition uses round robin partitioning

#How to increase or decrease the partitions

#coalesce - Used to Decrease the no. of partions we use coalesce function,
# coalesce supports only decrease the number of partitions,
#Coalesce use range of partitioning
#1,2,3,4,5 -> 3- [1,2],[3,4],[5]
# benefit - try to aviod shuffling (copying of data from mapper/one executor to the reducer/another executor)
# will happen rarely hence less cost
# drawback - in-equal number of distribution of partitions happens because of range partitioning
#When to use Coalesce? applied when we wanted to process the rdd further with less number of tasks or finalize/store the rdds
rdd2=sc.textFile("file:///home/hduser/hive/data/custs2")
rdd3=rdd1.union(rdd2)
rdd3.getNumPartitions()
#6
rdd1.getNumPartitions()
#2
rdd2.getNumPartitions()
4
rdd4=rdd3.repartition(10)
rdd4=rdd3.map(lambda x:x.split(",")).filter(lambda x:int(x[3])>60)
rdd4.count()
#758280
rdd3.count()
#2669733
rdd4.getNumPartitions()
6
rdd4.getNumPartitions()
#10
rdd5=rdd4.coalesce(3)
print(rdd5.getNumPartitions())


#Repartition - Used to Increase the no. of partions we use repartition function,
# repartition supports both increase or decrease the number of partitions (preferably coalesce has to be used for decreasing)
#repartition uses round robin/hash partitioning
#1,2,3,4,5, -> 3- [1,4],[2,5],[3,6]
# benefit - equal number of distribution of partitions
# drawback - shuffling happens hence costly
#When to use Repartition? applied when we wanted to process the rdd further with more number of tasks (map, filter, flatmap)

#Reduce by key transformation
#First lets understand reduce function
# calculate the total sales happened with the transaction amt >1000
rdd1=sc.textFile("file:/home/hduser/cust_bkp.txt")
rdd1.collect()
#['1,Chennai,Mobile,1000', '2,Chennai,Laptop,3000', '3,Hyd,mobile,4000', '4,Chennai,mobile,2000']
rdd2=rdd1.map(lambda x:x.split(",")).map(lambda x:int(x[3])).filter(lambda x:x>1000)
mapfilterrdd2=rdd1.map(lambda x:x.split(",")).map(lambda x:int(x[3])).filter(lambda x:x>1000)
mapfilterrdd2.collect()
#[3000, 4000, 2000]
mapfilterrdd2.getNumPartitions()
#2
mapfilterrdd2.reduce(lambda b,f:b+f)
#9000

# calculate the city wise total sales happened with the transaction amt >1000
mapfilterrdd2=rdd1.map(lambda x:x.split(",")).map(lambda x:((x[1]),int(x[3]))).filter(lambda x:x[1]>1000)
reducedrdd3=mapfilterrdd2.reduceByKey(lambda x,y:x+y)
print(reducedrdd3.collect())

#Checkpoint
#Below code work well if the source is batch or static or permenant

#What if the source is dynamic or transient or STREAMING in nature, below code will not work well if the source is streaming

#Narrow and wide transformations
#Narrow transformation - if a transformation depends on the output of the other transformation directly
#No stage split will happen


#Cache and Persist
#What is- Cache is a transformation used to inform spark not to run the Garbage collection on the rdd that has been cached
# after we perform an action on the rdd
#When do we use caching - If we are going to use an rdd or the subsequent rdds repeatedly for performing transformation or action
#What is Persist - is a transformation used to inform spark not to run the Garbage collection on the rdd that has been persisted
#  in memory/disk/both/with replica/without replica/serialized/non-serialized after we perform an action on the rdd
#When do we use Persist - If we are going to use an rdd or the subsequent rdds repeatedly for performing transformation or action
# Persist will be used for leveraging more options than than cache in situations such as more volume of data that can't fit in the
# entire memory or we need to replicate for better fault tolerance or we wanted to try with/without serialized dataset for processing
# to manage the tradeoff between ser-de and the volume of data  - if the volume is not so high then we can keep in a deserialized
# fashion (we will get the benefits of processing faster without again deserializing)

rdd1=sc.textFile("file:/home/hduser/cust_bkp.txt")
mapfilterrdd2=rdd1.map(lambda x:x.split(",")).map(lambda x:((x[1]),int(x[3]))).filter(lambda x:x[1]>1000)
reducedrdd3=mapfilterrdd2.reduceByKey(lambda x,y:x+y)
reducedrdd4=mapfilterrdd2.map(lambda x:x[0])
reducedrdd3.collect()
#[('Chennai', 5000), ('Hyd', 4000)]
rdd1=sc.textFile("file:/home/hduser/cust_bkp.txt")
reducedrdd4.collect()
#['Chennai', 'Hyd', 'Chennai']
rdd1=sc.textFile("file:/home/hduser/cust_bkp.txt")
mapfilterrdd2=rdd1.map(lambda x:x.split(",")).map(lambda x:((x[1]),int(x[3]))).filter(lambda x:x[1]>1000)
mapfilterrdd2.cache()
#PythonRDD[357] at RDD at PythonRDD.scala:53
reducedrdd3=mapfilterrdd2.reduceByKey(lambda x,y:x+y)
reducedrdd4=mapfilterrdd2.map(lambda x:x[0])
reducedrdd3.count()
#2
reducedrdd4.count()
#3
mapfilterrdd2.count()
#3
rdd1.count()
#4
mapfilterrdd2.unpersist()
#PythonRDD[357] at RDD at PythonRDD.scala:53

from pyspark import StorageLevel
mapfilterrdd2.persist(StorageLevel.DISK_ONLY)
mapfilterrdd2.count()
mapfilterrdd2.persist(StorageLevel.DISK_ONLY_2)
mapfilterrdd2.unpersist()
mapfilterrdd2.persist(StorageLevel.DISK_ONLY_2)
mapfilterrdd2.count()
mapfilterrdd2.persist(StorageLevel.DISK_ONLY_3)
mapfilterrdd2.unpersist()
mapfilterrdd2.persist(StorageLevel.DISK_ONLY_3)
mapfilterrdd2.count()
mapfilterrdd2.unpersist()
mapfilterrdd2.persist(StorageLevel.MEMORY_AND_DISK)
mapfilterrdd2.count()
mapfilterrdd2.unpersist()
mapfilterrdd2.unpersist()
mapfilterrdd2.persist(StorageLevel.MEMORY_AND_DISK_2)
mapfilterrdd2.count()

#Cache/Persist vs Checkpoint
#Cache and Persist will retain the lineage but the Checkpoint will Truncate or cut the lineage and stores the data in HD/HDFS Checkpoint directory

#Cache/Persist will retain the lineage, but use the lineage for the first time materialize the data
# subsequently provide the data from cache memory/persisted DISK location, if the data in the mem/disk is lost then
# get it from original source using lineage

#Checkpoint removes the lineage in the DAG and use the lineage for the first time,
# subsequently always provide the data from checkpoint dir
sc.setCheckpointDir("file:/home/hduser/ckptdir/") #need to ensure this ckpt dir is present in all workers
sc.setCheckpointDir("/user/hduser/ckptdir/")#use hdfs for better fault tolerance and performance also
rdd2.checkpoint()
rdd2.count()

#saveAsTextFile will help us store the data in the hdfs/linux/cloud fs for using this data across the applications

