from pyspark.sql.functions import avg
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName("demo").getOrCreate()
    df = spark.createDataFrame([("Brooke", 20), ("Brooke", 25), ("Denny", 31), ("TD", 35)], ["name", "age"])
    df = df.groupBy("name").agg(avg("age"))
    df.show()
    spark.stop()