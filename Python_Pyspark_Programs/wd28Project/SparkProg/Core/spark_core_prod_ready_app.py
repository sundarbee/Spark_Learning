#Function definitions are here
def redfunc(x,y):
 if y > 20.0 :
  return(x+y)
 else :
  return(x)

#libraries are imported here
from pyspark.sql import SparkSession
from pyspark import StorageLevel

#main program body is kept below
def main():
   #define spark configuration object
   #conf = SparkConf().setAppName("Local-sparkcore").setMaster("local[*]")
   print("Inside the main method, our actual code is going to execute")
   spark = SparkSession.builder.appName("Spark core pyspark").getOrCreate()
   #Set the logger level to error
   spark.sparkContext.setLogLevel("ERROR")
   sc=spark.sparkContext
   # Create a file rdd with 4 partitions
   rdd = sc.textFile("file:/home/hduser/hive/data/txns",4)
   print(rdd.count())

   # create a hadoop rdd with 4 partitions
   # create the below dir in hadoop and place the file txns in the below dir
   #hadoop fs -mkdir -p /user/hduser/hive/data/
   #hadoop fs -put -f ~/hive/data/txns hive/data/
   hadooprdd = sc.textFile("hdfs://127.0.0.1:54310/user/hduser/txns",4)
   #we can read data from different hadoop cluster also by mentioning the ip address/domain name of the namenode
   #hadooprdd=rdd
   print('total number of lines in hadoop - ' + str(hadooprdd.count()));
   print('print a sample of 20 rows with seed of 100 for dynamic data');
   for x in rdd.takeSample("true", 10, 111) :
      print(x)
   print("print only the first line of the dataset " );
   print(rdd.first())
   print('type of rdd is ' + str(type(rdd)));
   print('Number of partition of the base file is ' + str(rdd.getNumPartitions()))
   #Create a splitted rdd to split the line of string to line of list of string
#x=>x , lambda x:x
   rddsplit=rdd.map(lambda x:x.split(","))
   print("number of partitions before filtering")
   # filter only the category contains exercise or product contains jumping.
   rddexerjump = rddsplit.filter(lambda x:(x[4].upper().__contains__("EXERCISE") or x[5].upper().__contains__("JUMP")))
   #select * from rddsplit where upper(category) like "%EXERCISE%" or upper(product) like "%JUMP%"
   print("number of partitions after filtering")
   print(rddexerjump.getNumPartitions())
   valexerjumpcnt= rddexerjump.count()
   print("Dynamically increase or decrease the number of partitions based on the volume of data")
   print("Partition handling in Spark")
   #Try to convert this as a function
   # volume of data varies on a daily basis, how do u improve the performance
   if (valexerjumpcnt > 0 and valexerjumpcnt <= 30000) :
    rddexerjumpnew=rddexerjump.coalesce(2)
    print('Number of partition of the filtered data with $valexerjumpcnt count ' + str(rddexerjumpnew.getNumPartitions()));
   elif valexerjumpcnt > 30001 and valexerjumpcnt < 60000 :
    rddexerjumpnew=rddexerjump.coalesce(3)
    print('Number of partition of the filtered data with $valexerjumpcnt count ' + str(rddexerjumpnew.getNumPartitions()));
   else :
    rddexerjumpnew=rddexerjump.repartition(6)
    print('Number of partition of the filtered data with $valexerjumpcnt count ' + str(rddexerjumpnew.getNumPartitions()));
    print(" Caching of RDDs ")
   rddcredit = rddsplit.filter(lambda x : not(x.__contains__("credit")))
   #00014686,12-22-2011,4006684,136.19,Team Sports,Football,Brownsville,Texas,credit
   #any one of the list of columns contains the credit means just ignore
   #select * from rddsplit
   # where all_column_values_in_the_row not in 'credit';
   # where col1='credit' or col2='credit' .......
   print("How many California state people transacted using cash with the game of credit")
   #How many California state people transacted using cash with the game of credit
   rdd2 = rddexerjumpnew.filter(lambda x : x[7] == "California" and x[8] == "cash")
   # convert the type and take one column
   rdd3 = rdd2.map(lambda x : (float(x[3])))
   rdd3.cache() #is it meaningful to cache?
   # we will be caching when the volume of data is fit in the memory, even though if the volume of data is high
   # what happens if i use cache ie data volume is 2gb executor memory is 1gb what happens? OOM Will not occur
   rdd3.unpersist()
   rdd3.persist(StorageLevel.MEMORY_AND_DISK)
   #or is it meaningful to persist in both memory and disk?
   # we will be persisting in both levels when the volume of data is very high and it can't fit in the entire memory
   sumofsales = rdd3.sum()
   print("Sum of Sales in california with cash: " + str(sumofsales))
   sumofsalesreduce= rdd3.reduce(lambda x,y:x+y); #rdd3.reduce((x,y)=>x+y)
   print("Sum of total Sales in california with cash using reduce : " + str(sumofsalesreduce))
   sumofsalesreduce1= rdd3.reduce(lambda x,y : redfunc(x,y));
   maxofsales = rdd3.max()
   print("Max sales value : " + str(maxofsales))
   totalsales = rdd3.count()
   print("Total no fo sales: " + str(totalsales))
   avgofsales = rdd3.sum()/rdd3.count()
   print("Avg sales value : " + str(avgofsales))
   rdd3.unpersist(); # after using rdd3 you can unpersist before your application finish
   print("Sum of Sales where trans amount is > 10 dollar: " + str(sumofsalesreduce1))
   print(" Lets try to achieve the same above functionality using filter")
   rddfilter3a = rdd2.filter(lambda x :float(x[3])>10.0)
   #rddfilter3=rdd2.map(lambda x : float(x[3]))
   #rddfilter3=rdd2.map(lambda x:float(x[3]))
   rddfilter3a.count()

#calling the main program, from here I will start execute the entire application
if __name__ == '__main__':
   print("Calling the main program, check whether we got enough arguments to this program or not....")
   main()
   print("post execution of the main method... write some more programs after the main method to do some cleanup or call some other functions")