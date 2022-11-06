# Codility Test: Upler

from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType


def get_english_name(species):
    return species.split("(")[0].strip()


def get_start_year_unregistered(period):
    return int(period.split("-")[0][1::])


def get_trend(annual_percentage_change):
    annual_percentage_change = float(annual_percentage_change)
    if annual_percentage_change < -3:
        return "strong decline"
    elif -3 <= annual_percentage_change <= -0.5:
        return "weak decline"
    elif -0.5 < annual_percentage_change < 0.5:
        return "no change"
    elif 0.5 <= annual_percentage_change <= 3:
        return "weak increase"
    elif annual_percentage_change > 3:
        return "strong increase"


get_english_name = udf(get_english_name)
get_start_year = udf(lambda x: get_start_year_unregistered(x), IntegerType())
get_trend = udf(get_trend)


from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql.functions import col


class BirdsETLJob:
    input_path = '../mmt/birds.csv'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                                          .master("local[1]")
                                          .appName("BirdsETLJob")
                                          .getOrCreate())

    def extract(self):
        input_schema = StructType([StructField("Species", StringType()),
                                   StructField("Category", StringType()),
                                   StructField("Period", StringType()),
                                   StructField("Annual percentage change", DoubleType())
                                   ])
        return self.spark_session.read.csv(self.input_path, header=True, schema=input_schema)

    def transform(self, df):
        df = df.withColumn("species", get_english_name(df.Species)).withColumn("category", df.Category).withColumn("collected_from_year", get_start_year(df.Period)).withColumn("annual_percentage_change", col("Annual percentage change")).withColumn("trend", get_trend(col("Annual percentage change")))

        return df.select(["species", "category", "collected_from_year", "annual_percentage_change", "trend"])

    def run(self):
        return self.transform(self.extract())


bird = BirdsETLJob()
df = bird.run()
df.write.mode("overwrite").csv("./output", header=True)


