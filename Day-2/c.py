import boto3


def batch_upload(table, items):
    """

    :param table:
    :type table:
    :param items:
    :type items:
    :return:
    :rtype:
    """
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(item)
    print("Timestamp Load: Completed")


def batch_delete(table, items):
    """

    :param table:
    :type table:
    :param items:
    :type items:
    :return:
    :rtype:
    """
    with table.batch_writer() as batch:
        for item in items:
            batch.delete_item(item)
    print("Timestamp Load: Completed")


def construct_items(keys, values):
    """

    :param keys:
    :type keys:
    :param values:
    :type values:
    :return:
    :rtype:
    """
    items = []
    for value in values:
        item = {}
        i = 0
        for key in keys:
            item[key] = value[i]
            i += 1
        items.append(item)
    return items


if __name__ == '__main__':
    """
    Bulk upload and delete in DynamoDB
    """
    res = boto3.resource('dynamodb')
    dyn_table = res.Table("dynm_table_name")

    records_to_upload = construct_items((), [[]])
    batch_upload(dyn_table, records_to_upload)

    records_to_delete = construct_items((), [[]])
    batch_delete(dyn_table, records_to_delete)
