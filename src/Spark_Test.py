from pyspark.sql import SparkSession
from pyspark import SparkContext 
from pyspark.sql import SQLContext 
from pyspark.sql.window import Window
from pyspark.sql.functions import lag,lead,to_timestamp,col, when, mean, split, explode, expr,row_number, sum, max, min,avg, countDistinct, substring,dense_rank
from pyspark.sql.types import DoubleType, LongType, _infer_schema
from pyspark.sql.types import StructField, StructType, IntegerType, StringType,DoubleType,DecimalType

spark = SparkSession.builder.appName("Testing Spark").master("local[*]").getOrCreate()

# Test the spark
df = spark.createDataFrame([{"hello": "world"} for x in range(1000)])
df.show(3, False)