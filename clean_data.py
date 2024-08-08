from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import col

def filtered_data_megan(df):
    name_error_msg = ["46284y924", "BOOM!", "corrupted data", "ERROR!", "This is a bad row", "THisISN't a GoOd RoW"]
    prod_name_error_msg = ["46284y924", "BOOM!", "ERROR!", "This is a bad row", "Not This ONe"]

    filter_customerID = df.filter(~col('_c1').rlike('^[^0-9]*$') & (col('_c1') != '') & (col('_c1') != "46284y924"))

    filter_customer_name = filter_customerID.filter(~col('_c2').isin(name_error_msg))

    filter_productID = filter_customer_name.filter(~col('_c3').rlike('^[^0-9]*$') & (col('_c3') != '') & (col('_c3') != "46284y924"))

    filter_prod_name = filter_productID.filter(~col('_c4').isin(prod_name_error_msg))
    return filter_prod_name


sc = SparkContext.getOrCreate()
sc.setLogLevel("WARN")
 
spark = SparkSession(sc)

path = sc.textFile("file:///home/username/data_team_2.csv")

df = spark.read.csv(path)

df = filtered_data_megan(df)

df.show()