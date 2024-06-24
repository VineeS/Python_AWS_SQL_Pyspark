from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()

df = spark.read.format('csv').option('header', True).option('inferschema',True).load('cars.csv')

df.show()

df.createOrReplaceTempView("df")
df.printSchema()
df_new = spark.sql(
    """
    select min()
    """
)

df_new.write.csv()