"""
"""

__author__ = 'aman.rv'

import names
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType


if __name__ == '__main__':
    # create a SparkSession
    spark = SparkSession.builder.appName("TopEarningEmployees").getOrCreate()

    # define the schema for the DataFrame
    schema = StructType([
        StructField("employee_name", StringType(), True),
        StructField("department", StringType(), True)
    ])

    # create a list of rows with the data
    data = [
        Row(names.get_full_name(), "IT"),
        Row(names.get_full_name(), "HR"),
        Row(names.get_full_name(), "IT"),
        Row(names.get_full_name(), "HR")
    ]

    # create the DataFrame
    df = spark.createDataFrame(data, schema)
    df.show()




