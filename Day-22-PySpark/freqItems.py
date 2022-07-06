from pyspark.sql import SparkSession
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Column Expr").getOrCreate()
    schema = "id INT, efficiency DOUBLE, salary INT"
    df = spark.createDataFrame([
        (1, 23.45, 1),
        (1, 23.451, 12),
        (2, 23.4512, 123),
        (2, 23.45123, 1234),
        (3, 23.451234, 12345),
        (4, 23.4512345, 123456)
    ], schema)
    # df.describe().show()
    print(df.freqItems(["id"]).show())
