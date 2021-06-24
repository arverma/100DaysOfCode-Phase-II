import boto3


def get_matching_s3_objects(bucket, prefix="", suffix=""):
    """
    Generate objects in an S3 bucket.
    :param bucket: Name of the S3 bucket.
    :type bucket: str
    :param prefix: Only fetch objects whose key starts with this prefix (optional).
    :type prefix: tuple, list, str
    :param suffix: Only fetch objects whose keys end with this suffix (optional).
    :type suffix: str
    :return: None
    :rtype:
    """

    if isinstance(prefix, str):
        prefixes = (prefix, )
    else:
        prefixes = prefix

    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('BucketName')

    for key_prefix in prefixes:
        for object_summary in my_bucket.objects.filter(Prefix=key_prefix):
            key = object_summary.key
            if key.endswith(suffix):
                print(key)


if __name__ == '__main__':
    # Example 1
    get_matching_s3_objects("bucket_name")
    # Example 2
    get_matching_s3_objects("bucket_name", "subfolder1")
    # Example 3
    get_matching_s3_objects("bucket_name", "subfolder1/sub_subfolder2")
    # Example 4
    get_matching_s3_objects("bucket_name", ["subfolder1", "subfolder2"])
    # Example 5
    get_matching_s3_objects("bucket_name", ("subfolder1", "subfolder2"))
    # Example 5
    get_matching_s3_objects("bucket_name", ("subfolder1", "subfolder2/sub_subfolder1"), ".csv")
    # Example 5
    get_matching_s3_objects("bucket_name", ["subfolder1/sub_subfolder1", "subfolder2/sub_subfolder1"], ".parquet")