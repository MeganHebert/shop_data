from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import upper, col

def filtered_data_tony(rdd):
    # Filter rows where '_c5' is null and show the results
    filtered_not_null_product_cat_rdd = rdd.filter(~col('_c5').isNull()).show()
    filtered_not_null_payment_type_rdd = filtered_not_null_product_cat_rdd.filter(~col('_c6').isNull()).show()
    filtered_not_null_qty_rdd = filtered_not_null_payment_type_rdd.filter(~col('_c7').isNull()).show()
    filtered_not_null_price_rdd = filtered_not_null_qty_rdd.filter(~col('_c8').isNull()).show()
    # There are no null values from c5-c8 which is what matters so this is fine


    #_c5 is product category
    # None of them contain any numbers so the data seems to be clean
    filtered_no_number_product_cat_rdd = filtered_not_null_price_rdd.filter(~col('_c5').rlike('\D+'))
    filtered_no_number_payment_type_rdd = filtered_no_number_product_cat_rdd.filter(~col('_c6').rlike('\D+'))
    filtered_no_number_failure_reason_rdd = filtered_no_number_payment_type_rdd.filter(~col('_c15').rlike('\D+'))
    # None of the word required columns have digits

    filtered_qty_rdd = filtered_no_number_failure_reason_rdd.filter(~col('_c7').rlike('^[^0-9]*$') & (col('_c7') != ''))


    filtered_price_rdd = filtered_qty_rdd.filter(~col('_c8').rlike('^[^0-9]*$') & (col('_c8') != ''))

    #filtered_price_rdd.show()

    # We found one error we can filter out
    filtered_product_category_rdd = filtered_price_rdd.filter(~upper(col('_c5')).contains("ERROR"))


    #_c6 payment_type 4 Errors for payment type
    filtered_payment_type_rdd = filtered_product_category_rdd.filter(~upper(col('_c6')).contains("ERROR"))

    #_c7 qty 1 error found
    filtered_qty_rdd = filtered_payment_type_rdd.filter(~upper(col('_c7')).contains("ERROR"))

    #_c8 price 2 errors
    filtered_price_rdd = filtered_qty_rdd.filter(~upper(col('_c8')).contains("ERROR"))

    #_c15 failure reason (NO ERRORS)
    filtered_failure_reason_rdd = filtered_price_rdd.filter(~upper(df._c15).contains("ERROR"))

    #filtered_failure_reason_rdd.show()

    return filtered_failure_reason_rdd

sc = SparkContext.getOrCreate()
# Create Spark Session 
spark = SparkSession(sc)
#conf = SparkConf().setAppName("Example1").setMaster("local")


#sc = SparkContext(conf = conf)

#team2_rdd = sc.textFile("/csv_data/data_team_2.csv")
path = sc.textFile("file:///root/data_team_2.csv")

df = spark.read.csv(path)

#df.printSchema()

filtered_rdd = filtered_data_tony(df)

filtered_rdd.show()

# To run:  spark-submit PySpark_Example.py