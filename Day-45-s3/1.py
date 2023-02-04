__author__ = 'aman.rv'

import boto3
from urllib.parse import urlparse

from pyspark.sql.session import SparkSession


def write_spark_df_to_s3_with_specific_file_name(df, output_path):
    # Repartition and write spark dataframe to S3
    df.repartition(1).write.mode("overwrite").format(
        output_path.split(".")[-1]
    ).save(
        "/".join(output_path.split("/")[0:-1])
    )

    # Extract bucket and key name given a S3 file path
    s3_path = urlparse(output_path, allow_fragments=False)
    bucket_name, key = s3_path.netloc, s3_path.path.lstrip("/")

    # Rename the part file
    try:
        s3 = boto3.resource('s3')
        prefix = "/".join(key.split("/")[0:-1]) + "/part"
        for obj in s3.Bucket(bucket_name).objects.filter(Prefix=prefix):
            s3.Bucket(bucket_name).copy({'Bucket': bucket_name, 'Key': obj.key}, key)
            s3.Object(bucket_name, obj.key).delete()
    except Exception as err:
        raise Exception("Error renaming the part file to {}: {}".format(output_path, err))


def create_dataframe(spark):
    simple_data = [("James", "Sales", "NY", 90000),
                   ("Michael", "Sales", "NY", 86000),
                   ("Robert", "Sales", "CA", 81000)
                   ]
    schema = ["employee_name", "department", "state", "salary"]
    return spark.createDataFrame(data=simple_data, schema=schema)


if __name__ == '__main__':
    spark_session = SparkSession.builder.getOrCreate()
    df = create_dataframe(spark_session)

    write_spark_df_to_s3_with_specific_file_name(
        df,
        "gs://bucket-name/path/to/destination/keep_this_filename.csv"
    )
