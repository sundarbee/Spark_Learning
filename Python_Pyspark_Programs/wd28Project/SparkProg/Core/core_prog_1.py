#Simple python program
sallist=[10000,20000,10000,15000]
lam=lambda x:x+(x*.10)
def lam1(x):
    return x+(x*.10)

bonsallist=list(map(lam1,sallist))
print(bonsallist)
bonsallist=[]
for i in sallist:
    bonsallist.append(lam(i))
print(bonsallist)

#rdd=sallist1+sallist2
sallistpart1=[10000,20000]
sallistpart2=[10000,15000]
bonsallist1=list(map(lam1,sallistpart1))
bonsallist2=list(map(lam1,sallistpart2))

print(bonsallist1)
for i in sallistpart1:
    print(lam(i))

print(bonsallist2)
for i in sallistpart2:
    print(lam(i))


#map first iteration -> I will take 10000 pass to the lam1(10000)-> bonsallist=list(11000.0)
#map second iteration -> I will take 20000 pass to the lam1(20000)-> bonsallist=list(22000.0)
#Traditional way of instantiating the Spark Context
#If any program has to be deemed a spark prog, then we have to have the class SparkContext instantiated
from pyspark.context import SparkContext
sc=SparkContext('local[*]','weekday 28 app')
#sqlContext=new org.apache.spark.sql.SQLContext(sc)
#import org.apache.spark.sql.hive.HiveContext
#hqlc=new HiveContext(sc)
print(sc)
#sc1=SparkContext('local[2]','weekday 29 app')
#rdd1=sc.parallelize(sallist)
rdd1=sc.parallelize(sallist,2)
print(rdd1.glom().collect())
print(rdd1.getNumPartitions())
rdd2=rdd1.map(lam1)
bonsallist=rdd2.collect()
print(bonsallist)
print("trying to print rdd output using collect")
rdd2.collect()
sc.stop()

#Modern way of writing spark program using Spark Session objects introduced in V2 of Spark
#spark session object internally instantiate the SparkContext class in the name of sparkContext object and sqlContext object
from pyspark.sql import SparkSession
#spark1=SparkSession()
spark=SparkSession.builder.master("local[2]").appName("Wd28 Spark App").getOrCreate()
# the above spark session object will internally creates spark context object in the name of sparkContext and
# sqlContext in the name of spark itself, if you want to create rdds invoke the func inside spark.sparkContext obj
# or if you want to create dataframes/dataset/tempviews/hive queries then use the func inside spark obj itself
#sparkContext=SparkContext("local[2]",'weekday 28 session app')
#spark=SQLContext(sparkContext)
#spark=HiveContext(sparkContext)
#spark.sql("create external table tblname() location")
spark.sparkContext.setLogLevel("INFO")
print(spark.sparkContext)
#sqlContext=spark
sc=spark.sparkContext
#mi='mohamed irfan'
rddsess1=sc.parallelize(sallist)
print(rddsess1.glom().collect())
print(rddsess1.getNumPartitions())
rddsess2=rddsess1.map(lam1)
bonsallist=rddsess2.collect()
print(bonsallist)

#spark.read.json
#df1=spark.read.json("file:///home/hduser/sparkdata/auctiondata.json/")
#df1.select("*").where("bid>50.0").show()

#Not so important - because in Organizations we prefer doing data transformation using Spark SQL rather than Spark Core func
#RDD Functions (transformatons/actions)
#Transformations -> Active/Passive transformations
#Active - if a transformation returns the number of output not equal to the number of input
#Passive - if a transformation returns the number of output equal to the number of input
#map - select (for loop and some functionality applied on the looped data) - for loop in python programming
lines = sc.textFile("file:/home/hduser/sparkdata/empdata.txt")
lengths = lines.map(lambda l:len(l))
lengths.collect()
lengths = lines.map(lambda x:x.split(",")).map(lambda l:len(l))
lengths.collect()

#filter - where (for loop and if condition applied on the looped data, if the condition returns true return the looped original data else dont return)
chennaiLines = lines.map(lambda x:x.split(",")).filter(lambda l : l[1].upper()=='CHENNAI' )
chennaiLines.collect()

#3. flatmap - Nested for loop
#['abc','xyz'] -> map[['a','b','c'],['x','y','z']] -> flatMap['a','b','c','x','y','z']
# convert the data from unstructured to structured.
# below data is of what type?
# structed data with space delimiter but malformed and eligible for becoming semi-structured
# how structed - because the below attributes/fields can be related with each other and they are not seperated/unified/individual.
# for eg. irfan's age is 40 or custid 1 is irfan
# 1 irfan 40
# 2 30 venkat chennai
# 33 chennai kavya
#semi structued format
# {id:1,name:irfan,age:40}
# {id:2,age:30,name:venkat,city:chennai}
# {age:33,city:chennai,name:kavya}

#unstructued data
# below is an unstructed data with space delimiter that are seperated/unified/individual and having own identity
# and eligible for becoming structured with the help of some functions preferably flatMap
#Eg. I can't say hadoop is the eco system of kafka
#hadoop spark hadoop spark kafka datascience
#spark hadoop spark datascience
#informatica java aws gcp
#gcp aws azure spark
#gcp pyspark

#['ArunKumar,chennai,33,2016-09-20,100000', 'Lara,chennai,55,2016-09-21,10000', 'vasudevan,banglore,43,2016-09-23,90000', 'irfan,chennai,33,2019-02-20,20000', 'basith,CHENNAI,29,2019-04-22']
#map -> 'ArunKumar,chennai,33,2016-09-20,100000'
#map -> 'Lara,chennai,55,2016-09-21,10000'
#flat -> ["ArunKumar","chennai","33","2016-09-20","100000","Lara",chennai,55,2016-09-21,10000]
#ArunKumar
#chennai
#33
#2016-09-20
#100000

#4. union - is a transforman used for merging/combining/connecting/differentiating/finding the similarity of multiple datasets
rdd1=sc.textFile("file:///home/hduser/hive/data/custsnopilot")
rdd2=sc.textFile("file:///home/hduser/hive/data/custsnopilot1")
rdd3=rdd1.union(rdd2).distinct()
rdd3.collect()
#['4000002,Paige,Chen,77,Teacher', '4000003,Sherri,Melton,34,Firefighter', '4000004,Gretchen,Hill,66,Computer hardware engineer', '4000005,Karen,Puckett,74,Lawyer', '4000006,Patrick,Song,42,Veterinarian', '4000001,Kristina,55,Pilot', '4000007,Elsie,43,Pilot', '4000229,Faye,64,Pilot', '4000230,Kathy,28,Pilot', '4000251,Jeremy,61,Pilot', '4000271,Alice,59,Pilot', '4000322,Geraldine,50,Pilot', '4000002,Paige,Chen,77,Teacher']
#rdd3=rdd1.union(rdd2)
#rdd4=rdd3.map(lambda x:x.split(",")).map(lambda x:x[3])
#rdd4.collect()
#['77', '34', '66', '74', '42', 'Pilot', 'Pilot', 'Pilot', 'Pilot', 'Pilot', 'Pilot', 'Pilot', '77']
#rdd4_5cols=rdd3.filter(lambda x:len(x.split(","))==5)
#rdd4_5cols.collect()
#['4000002,Paige,Chen,77,Teacher', '4000003,Sherri,Melton,34,Firefighter', '4000004,Gretchen,Hill,66,Computer hardware engineer', '4000005,Karen,Puckett,74,Lawyer', '4000006,Patrick,Song,42,Veterinarian', '4000002,Paige,Chen,77,Teacher']
#rdd4_4cols=rdd3.filter(lambda x:len(x.split(","))<5)
#rdd4_4cols.collect()
#['4000001,Kristina,55,Pilot', '4000007,Elsie,43,Pilot', '4000229,Faye,64,Pilot', '4000230,Kathy,28,Pilot', '4000251,Jeremy,61,Pilot', '4000271,Alice,59,Pilot', '4000322,Geraldine,50,Pilot']
#rdd4_4cols=rdd3.filter(lambda x:len(x.split(","))<5).map(lambda x:(x[0],x[1],'NA',x[2],x[3]))
#rdd4_4cols.collect()
#[('4', '0', 'NA', '0', '0'), ('4', '0', 'NA', '0', '0'), ('4', '0', 'NA', '0', '0'), ('4', '0', 'NA', '0', '0'), ('4', '0', 'NA', '0', '0'), ('4', '0', 'NA', '0', '0'), ('4', '0', 'NA', '0', '0')]
rdd3.collect()
#['4000002,Paige,Chen,77,Teacher', '4000003,Sherri,Melton,34,Firefighter', '4000004,Gretchen,Hill,66,Computer hardware engineer', '4000005,Karen,Puckett,74,Lawyer', '4000006,Patrick,Song,42,Veterinarian', '4000001,Kristina,55,Pilot', '4000007,Elsie,43,Pilot', '4000229,Faye,64,Pilot', '4000230,Kathy,28,Pilot', '4000251,Jeremy,61,Pilot', '4000271,Alice,59,Pilot', '4000322,Geraldine,50,Pilot', '4000002,Paige,Chen,77,Teacher']
rdd4_4cols=rdd3.map(lambda x:x.split(",")).filter(lambda x:len(x)<5).map(lambda x: [x[0],x[1],'NA',x[2],x[3]])
rdd4_4cols.collect()
#[['4000001', 'Kristina', 'NA', '55', 'Pilot'], ['4000007', 'Elsie', 'NA', '43', 'Pilot'], ['4000229', 'Faye', 'NA', '64', 'Pilot'], ['4000230', 'Kathy', 'NA', '28', 'Pilot'], ['4000251', 'Jeremy', 'NA', '61', 'Pilot'], ['4000271', 'Alice', 'NA', '59', 'Pilot'], ['4000322', 'Geraldine', 'NA', '50', 'Pilot']]
rdd1_5cols=rdd3.map(lambda x:x.split(",")).filter(lambda x:len(x)==5).map(lambda x:[x[0],x[1],x[2],x[3],x[4]])
rdd1_5cols.collect()
#[['4000002', 'Paige', 'Chen', '77', 'Teacher'], ['4000003', 'Sherri', 'Melton', '34', 'Firefighter'], ['4000004', 'Gretchen', 'Hill', '66', 'Computer hardware engineer'], ['4000005', 'Karen', 'Puckett', '74', 'Lawyer'], ['4000006', 'Patrick', 'Song', '42', 'Veterinarian']]
rdd4_4cols.collect()
#[['4000001', 'Kristina', 'NA', '55', 'Pilot'], ['4000007', 'Elsie', 'NA', '43', 'Pilot'], ['4000229', 'Faye', 'NA', '64', 'Pilot'], ['4000230', 'Kathy', 'NA', '28', 'Pilot'], ['4000251', 'Jeremy', 'NA', '61', 'Pilot'], ['4000271', 'Alice', 'NA', '59', 'Pilot'], ['4000322', 'Geraldine', 'NA', '50', 'Pilot']]
rdd4_4cols.union(rdd1_5cols).collect()
#[['4000001', 'Kristina', 'NA', '55', 'Pilot'], ['4000007', 'Elsie', 'NA', '43', 'Pilot'], ['4000229', 'Faye', 'NA', '64', 'Pilot'], ['4000230', 'Kathy', 'NA', '28', 'Pilot'], ['4000251', 'Jeremy', 'NA', '61', 'Pilot'], ['4000271', 'Alice', 'NA', '59', 'Pilot'], ['4000322', 'Geraldine', 'NA', '50', 'Pilot'], ['4000002', 'Paige', 'Chen', '77', 'Teacher'], ['4000003', 'Sherri', 'Melton', '34', 'Firefighter'], ['4000004', 'Gretchen', 'Hill', '66', 'Computer hardware engineer'], ['4000005', 'Karen', 'Puckett', '74', 'Lawyer'], ['4000006', 'Patrick', 'Song', '42', 'Veterinarian']]
rdd4_4cols.union(rdd1_5cols).map(lambda x:int(x[3])).collect()
#['55', '43', '64', '28', '61', '59', '50', '77', '34', '66', '74', '42']

#5. Zip - Help us merging horizontally (row by row) the equal sized data from more than one rdds
rdd1=sc.textFile("file:/home/hduser/hive/data/custsnopilot_a")
rdd2=sc.textFile("file:/home/hduser/hive/data/custsnopilot_b")
rdd1.zip(rdd2).collect()
#[('4000002,Paige,Chen', '77,Teacher'), ('4000003,Sherri,Melton', '34,Firefighter'), ('4000004,Gretchen,Hill', '66,Computer hardware engineer'), ('4000005,Karen,Puckett', '74,Lawyer'), ('4000006,Patrick,Song', '42,Veterinarian')]
rdd1.zip(rdd2).map(lambda x:[x[0].split(","),x[1].split(",")]).collect()
#[[['4000002', 'Paige', 'Chen'], ['77', 'Teacher']], [['4000003', 'Sherri', 'Melton'], ['34', 'Firefighter']], [['4000004', 'Gretchen', 'Hill'], ['66', 'Computer hardware engineer']], [['4000005', 'Karen', 'Puckett'], ['74', 'Lawyer']], [['4000006', 'Patrick', 'Song'], ['42', 'Veterinarian']]]
rdd1.zip(rdd2).map(lambda x:[x[0].split(","),x[1].split(",")]).map(lambda x:[x[0][0],x[0][1],x[0][2],x[1][0],x[1][1]]).collect()
#[['4000002', 'Paige', 'Chen', '77', 'Teacher'], ['4000003', 'Sherri', 'Melton', '34', 'Firefighter'], ['4000004', 'Gretchen', 'Hill', '66', 'Computer hardware engineer'], ['4000005', 'Karen', 'Puckett', '74', 'Lawyer'], ['4000006', 'Patrick', 'Song', '42', 'Veterinarian']]

rdd1=sc.textFile("file:/home/hduser/hive/data/custsnopilot_aa").map(lambda x:x.split(","))
rdd2=sc.textFile("file:/home/hduser/hive/data/custsnopilot_bb").map(lambda x:x.split(","))
rdd3=rdd1.zip(rdd2).map(lambda x:[x[0][0],x[0][1],x[0][2],x[1][0],x[1][1]])
rdd3.collect()

#6. zipWithIndex - Help us assign row numbers to the rdd elements
rdd4=rdd3.zipWithIndex()
rdd4.collect()
rdd4.filter(lambda x:x[1]!=0).map(lambda x:x[0]).collect()

#Very Important:
#Partition - Horizontal division of data or grouping of data or splitting of data or seperation
#why partition - Inorder to parallelize, distribute, throughput, concurrent access of data
#how to control the partitioning - naturally how it occured or using coalesce and repartition how to change the degree of parallelism
#using partitioning concepts
#hdfs (blocks), mr(input split), hive(partitions/buckets), sqoop(split-by/mappers), spark(partitioning)

#naturally how partitions created when we create rdds (in spark core, we learn spark sql and streaming partitioning soon)
#1. parallelize will go with the number of cores defined in the sparksession object for default partitions
#2. parallelize will go with the second argument value if  i pass a higher or lower number of partitions
#3. textFile will go with the size of data in a chunk of 32mb by default if the data is >32 mb size
#4. textFile will go with the default partition of 2 if the data is <32 mb size
#5. textFile will go with the second argument value if  i override with the higher number of partitions that naturally created

rdd1=sc.textFile("file:///home/hduser/hive/data/txns_20201213_PADE1")
rdd1.getNumPartitions()
#2
rdda=sc.parallelize(range(1,100))
rdda.getNumPartitions()
#4
rdd1=sc.textFile("file:///home/hduser/sparkdata/youtube_videos.tsv")
rdd1.getNumPartitions()
#5
rdd1=sc.textFile("file:///home/hduser/sparkdata/sales.csv")
rdd1.getNumPartitions()
#2
rdda=sc.parallelize(range(1,100),1)
rdda.getNumPartitions()
#1
rdd1=sc.textFile("file:///home/hduser/sparkdata/youtube_videos.tsv",2)
rdd1.getNumPartitions()
#5
rdd1=sc.textFile("file:///home/hduser/sparkdata/youtube_videos.tsv",6)
rdd1.getNumPartitions()
#6
rdd1=sc.textFile("file:///home/hduser/sparkdata/youtube_videos.tsv",8)
rdd1.getNumPartitions()
#8

#How to increase or decrease the partitions
rdda=sc.parallelize(range(1,100),10)

#coalesce - Used to Decrease the no. of partions we use coalesce function,
# coalesce supports only decrease the number of partitions,
#Coalesce use range of partitioning
#1,2,3,4,5 -> 3- [1,2],[3,4],[5]
# benefit - shuffling (copying of data from mapper/one executor to the reducer/another executor) will happen rarely hence less cost
# drawback - in-equal number of distribution of partitions happens because of range partitioning
# applied when we wanted to process the rdd further with less number of tasks or finalize/store the rdds

rdda=sc.parallelize(range(1,1000),10)
print(rdda.getNumPartitions())
rddb=rdda.map(lambda x:x+10)
rddx=rddb.filter(lambda x:x>500)
rddb=rddx.coalesce(5)
rddx=rddb.map(lambda x:x+2)
print(rddx.collect())
print(rddb.getNumPartitions())
rddb.glom().collect() #shows partition elements
rdde=rddb.coalesce(8) #not possible
print(rdde.getNumPartitions()) #doesn't increase the number of partitions
rddb.glom().collect() #shows partition elements

#Repartition - Used to Increase the no. of partions we use repartition function,
# repartition supports both increase or decrease the number of partitions (preferably coalesce has to be used for decreasing)
#repartition uses round robin/hash partitioning (gives the reminder of 10 which is not hardcoded)
#1,2,3,4,5 -> 3- [1,4],[2,5],[3]
# benefit - equal number of distribution of partitions
# drawback - shuffling happens hence costly
#applied when we wanted to process the rdd further with more number of tasks (map, filter, flatmap)
rdda=sc.parallelize(range(1,100),1)
rddb=sc.parallelize(range(101,200),1)
rddc=rdda.union(rddb)
rdde=rddc.repartition(10)
rdda.getNumPartitions()
rddx=rdde.map(lambda x:x+2)
print(rdde.glom().collect())
rdde.getNumPartitions()
print(rdde.glom().collect())

rddf=rdde.repartition(2)

rdd1=sc.textFile("file:///home/hduser/hive/data/custs",1)
print(len(rdd1.repartition(14).glom().collect()))

#Reduce by key function
rdd1=sc.textFile("file:/home/hduser/cust.txt").map(lambda x:x.split(",")).map(lambda x:(x[1].lower(),int(x[3])))
rdd1.collect()
#[('mobile', 1000), ('laptop', 3000), ('mobile', 4000), ('mobile', 2000)]
rdd2=rdd1.reduceByKey(lambda a,i:a+i)
rdd2.collect()
#[('mobile', 7000), ('laptop', 3000)]
rdd1.glom().collect()
#[[('mobile', 1000), ('laptop', 3000), ('mobile', 4000)], [('mobile', 2000)]]
rdd1=sc.textFile("file:/home/hduser/cust.txt").map(lambda x:x.split(",")).map(lambda x:((x[1],x[2].lower()),int(x[3])))
rdd1.collect()
#[(('Chennai', 'mobile'), 1000), (('Chennai', 'laptop'), 3000), (('Hyd', 'mobile'), 4000), (('Chennai', 'mobile'), 2000)]
rdd2=rdd1.reduceByKey(lambda a,i:a+i)
rdd2.collect()
#[(('Chennai', 'mobile'), 3000), (('Chennai', 'laptop'), 3000), (('Hyd', 'mobile'), 4000)]

#Below code work well if the source is batch or static or permenant
rdd1=sc.textFile("file:/home/hduser/cust.txt")
rdd2=rdd1.map(lambda x:x.split(","))
rdd2.collect()
rdd2.count()

#What if the source is dynamic or transient or STREAMING in nature, below code will not work well if the source is streaming
rdd_moving_vehicle=sc.textFile("file:/home/hduser/cust.txt")#lat long position
rdd_moving_vehicle.persist()
#rdd_moving_vehicle.unpersist()
rdd_moving_vehicle.collect()
rdd_moving_vehicle.count()
sc.setCheckpointDir("file:///tmp/ckptdir")
rdd_moving_vehicle.checkpoint()
rdd_moving_vehicle.collect()
rdd_moving_vehicle.count()


#Narrow and wide transformations
#Narrow transformation - if a transformation depends on the output of the other transformation directly
#No stage split will happen
rdd1=sc.textFile("file:/home/hduser/cust.txt")
print(rdd1.getNumPartitions())
rdd2=rdd1.map(lambda x:x.split(","))
rdd3=rdd2.map(lambda x:[x[1],int(x[3])+(int(x[3])*.18)])
rdd3.glom().collect()
narrowrdd4=rdd3.filter(lambda x:x[1]>2000)
rdd3.collect()
#[['Chennai', 1180.0], ['Chennai', 3540.0], ['Hyd', 4720.0], ['Chennai', 2360.0]]
rdd3.glom().collect()
#[[['Chennai', 1180.0], ['Chennai', 3540.0]], [['Hyd', 4720.0], ['Chennai', 2360.0]]]
narrowrdd4=rdd3.filter(lambda x:x[1]>2000)
narrowrdd4.glom().collect()
#[[['Chennai', 3540.0]], [['Hyd', 4720.0], ['Chennai', 2360.0]]]
rdd3=rdd2.map(lambda x:(x[1],int(x[3])+(int(x[3])*.18)))
narrowrdd4=rdd3.filter(lambda x:x[1]>2000)
narrowrdd4.glom().collect()
#[[('Chennai', 3540.0)], [('Hyd', 4720.0), ('Chennai', 2360.0)]]
widerdd5=narrowrdd4.reduceByKey(lambda a,i:a+i)
widerdd5.glom().collect()
#[[('Chennai', 5900.0), ('Hyd', 4720.0)], []]
rdd2.collect()
rdd2.count()

#Cache/Persist will retain the lineage, but use the lineage for the first time,
# subsequently provide the data from cache memory/persisted location, if the data is lost then get it from original source
# using lineage
#Checkpoint removes the lineage in the DAG and use the lineage for the first time,
# subsequently always provide the data from checkpoint dir
sc.setCheckpointDir("file:///tmp/ckptdir2")
rdd2=sc.textFile("file:/home/hduser/cust.txt")
rdd2.checkpoint()
print(rdd2.count())
sc.setCheckpointDir("hdfs:///user/hduser/ckptdir2")

#Interview - 3 equal priority items in Spark
#1. Architecture/Terminologies
#executor1 (rdd1.p0 raw ->m0-> rdd2.p0 splitted -> m0 -> rdd3.p0 columns id,age,profession -> saveAsTextFile0 -> hdfs (part-00000))
#executor2 (rdd1.p1 raw ->m1-> rdd2.p1 splitted -> m1 -> rdd3.p1 columns id,age,profession -> saveAsTextFile1 -> hdfs (part-00000))

# Spark Context - Spark context is simply the object of SparkContext class, we create sc to use the functions such as textFile, parallelize
# etc., sc says how to access the cluster whether in spark context with given configuration or in a normal python/scala context

# Driver - Is the name given for a jvm created either in the edgenode/client or in any one of the node of the cluster where
# the spark context is initialized, rdds are defined, transformations/actions are applied and the DAG with lineages will be created

# Cluster Managers (local/sa/yarn/measos/kb) -
# local for learning/dev/repl/testing/snippetting (in a single jvm everything (driver/master/worker/executor/executorlauncher) will be executed),
# standalone used for productionization/performance tuning/debugging (spark native CM, used incase if hadoop cluster
# is not available for storage or for other processing like mr/hive/sqoop/tez/impala/presto otherwise using nosql/cloud/db as storage)
# yarn used for productionization/performance tuning/debugging (hadoop's CM, used incase where ever hadoop cluster
# is already running ie being used for storage and resource management for other processing like mr/hive/sqoop/tez/impala/presto including using of nosql/cloud/db as storage)

# Deployment modes (client/cluster)- start with the client mode then move to cluster mode
# decides where the driver has to run either in edgenode where we can test/tune/evalute/debug/
# /fixing of issues the jobs
# (client mode) or in any one of the node in cluster (cluster mode) where production run will happen because in client mode
# if run prod workloads also it will create resource issue when more number of jobs are submitted in client mode because more driver
# jvms will be created in one node (edgenode) rather than in the cluster nodes

# Job/Stage/Partition/Task
# Irfan is a project manager (spark-submit client jvm) getting a project(job/app) and dividing it into multiple
# modules (partitions) and assigning these modules in a form of (tasks) to different team members (containers/executors)
# sitting in different locations (nodemanagers/workers).

# YARN+Spark Components-> RM/NM/AM(Driver) cluster mode/Driver(client mode)/Containers (executors)
# Spark Standalone CM + Spark Components -> MASTER/WORKERs/Driver cluster mode/Driver client mode/executors
# Local mode -> all above components run inside a single jvm (abstracted for us)

#2. Performance Optimization
#3. Data Engeering using not much of spark core (RDD, DAG, Transformation, Actions, Partitioning, Caching),
# importantly Spark SQL/DF/DSL/UDFs

#Actions:
#Actions are functions that return value by applying some functionality on the RDDs
# Actions are immediate rather than lazy.
# Actions triggers the transformations using lineage kept in the DAG graph inside the Driver

#1. Collect - collects the data from RDD (in memory partitions across multiple nodes) and convert to local value
print(rdd2.collect())

#2. Count - is a iterative function run on all the partitions and get the executor's aggregated results
#  to the driver and driver will do the final count and produce the result
print(rdd2.count())

#3. take(number of elements)
print(rdd2.take(10))