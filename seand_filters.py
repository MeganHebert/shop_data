from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import col

def filtered_data_seand(df):
    result_df = df

    # datetime filter
    result_df = result_df.filter(col("_c9").rlike("^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"))

    # # country filter
    result_df = result_df.filter(col("_c10").isin(["United States", "Mexico", "Canada"]))
    
    # # city filter
    result_df = result_df.filter(~col("_c11").isin(["BOOM!", "ERROR!", "Not This ONe", "This row is bad"]))

    # ecommerce_website filter
    result_df = result_df.filter(col("_c12").rlike("^.+\.com$"))

    # # payment_txn_id filter
    result_df = result_df.filter(col("_c13").rlike("^\d{10}$"))

    # # payment_txn_success filter
    result_df = result_df.filter(col("_c14").isin(["True", "False"]))

    return result_df


sc = SparkContext.getOrCreate()
sc.setLogLevel("WARN")
spark = SparkSession(sc)

data_df = spark.read.csv("/user/seand/p2_data/data_team_2.csv", inferSchema=True)
data_df.show(1000)

data_df = filtered_data_seand(data_df)

data_df.show(1000)