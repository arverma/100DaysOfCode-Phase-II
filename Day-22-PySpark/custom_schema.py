from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName("Custom Schema").getOrCreate()
    schema = "id INT, name STRING, subject ARRAY<STRING>"
    df = spark.createDataFrame([
        (1, "aman", ["science", "math"]),
        (2, "ranjan", ["hindi", "english"]),
        (3, "verma", ["social science", "sanskrit"])
    ], schema)
    print(df.printSchema())
    df.show()
    print(df.schema)
