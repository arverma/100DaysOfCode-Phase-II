__author__ = 'aman.rv'

from google.cloud import storage
from urllib.parse import urlparse


def list_files_stored_under_gcs_bucket(prefix, suffix=""):
    """
    Returns list of all the file names that matches a certain prefix and suffix.
    """
    gcs_path = urlparse(prefix, allow_fragments=False)
    bucket_name, key = gcs_path.netloc, gcs_path.path.lstrip("/")
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name, prefix=key)
    return [blob.name for blob in blobs if blob.name.endswith(suffix)]


if __name__ == '__main__':
    # List all objects in side a bucket with certain prefix and suffix
    prefix = "gs://bucket_name/prefix/path"
    object_names = list_files_stored_under_gcs_bucket(prefix, suffix=".csv")
    print(object_names)

    # List all objects in side a bucket with certain prefix
    prefix = "gs://bucket_name/prefix/path"
    object_names = list_files_stored_under_gcs_bucket(prefix)
    print(object_names)

    # List all objects inside a bucket
    prefix = "gs://bucket_name"
    object_names = list_files_stored_under_gcs_bucket(prefix)
    print(object_names)
