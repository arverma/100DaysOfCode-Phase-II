from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, col, concat

if __name__ == '__main__':
    spark = SparkSession.builder.appName("Column Expr").getOrCreate()
    schema = "id INT, name STRING, salary INT"
    df = spark.createDataFrame([
        (1, "aman1", 1),
        (1, "aman2", 12),
        (1, "aman3", 123),
        (1, "aman4", 1234),
        (1, "aman5", 12345),
        (1, "aman6", 123456)
    ], schema)
    df.select(expr("salary * 1000")).show()
    df.select(expr("salary > 100")).show()
    df.select(col("salary") * 1000).show()
    df.select(concat(col("id"), expr("name"), col("salary"))).show()
