__author__ = 'aman.rv'

from pyspark.sql import SparkSession
from google.cloud import storage
from urllib.parse import urlparse


def write_spark_df_to_gcs_with_specific_file_name(df, output_path):
    # Repartition and write spark dataframe to GCS
    file_format = output_path.split(".")[-1]
    output_prefix = "/".join(output_path.split("/")[0:-1])
    df.repartition(1).write.mode("overwrite").format(file_format).save(output_prefix)

    # Extract bucket and key name given a GCS file path
    gcs_path = urlparse(output_path, allow_fragments=False)
    bucket_name, key = gcs_path.netloc, gcs_path.path.lstrip("/")

    # Rename the part file
    try:
        storage_client = storage.Client()
        blobs = storage_client.list_blobs(bucket_name, prefix="/".join(key.split("/")[0:-1])+"/part")
        existing_file_name = [blob.name for blob in blobs][0]
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(existing_file_name)
        bucket.rename_blob(blob, key)
    except Exception as err:
        raise Exception("Error renaming the part file to {}: {}".format(output_path, err))


def create_dataframe(spark):
    simple_data = [("James", "Sales", "NY", 90000),
                   ("Michael", "Sales", "NY", 86000),
                   ("Robert", "Sales", "CA", 81000),
                   ("Maria", "Finance", "CA", 90000),
                   ("Jeff", "Marketing", "CA", 80000),
                   ("Kumar", "Marketing", "NY", 91000)
                   ]
    schema = ["employee_name", "department", "state", "salary"]
    return spark.createDataFrame(data=simple_data, schema=schema)


if __name__ == '__main__':
    spark_session = SparkSession.builder.getOrCreate()
    df = create_dataframe(spark_session)

    write_spark_df_to_gcs_with_specific_file_name(
        df,
        "gs://bucket-name/path/to/destination/keep_this_filename.csv"
    )
