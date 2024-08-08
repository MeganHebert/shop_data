from clean_data import filtered_data_megan
from tony import filtered_data_tony
from seand_filters import filtered_data_seand

from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext.getOrCreate()
sc.setLogLevel("WARN")
spark = SparkSession(sc)

data_df = spark.read.csv("/user/seand/p2_data/data_team_2.csv", inferSchema=True)
data_df.show(1000)

data_df = filtered_data_megan(data_df)
data_df = filtered_data_tony(data_df)
data_df = filtered_data_seand(data_df)

data_df.write.csv("file:///home/seand/Code/unified_filter")