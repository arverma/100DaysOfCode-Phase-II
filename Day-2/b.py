import boto3
import botocore
from boto3.dynamodb.conditions import Attr


def scan_db(table, scan_kwargs=None):
    """
    Get all records of the dynamodb table where the FilterExpression holds true
    :param scan_kwargs: Filter conditions
    :type scan_kwargs: dict
    :param table: dynamodb table name
    :type table: str
    :return: list of recors
    :rtype: dict
    """
    if scan_kwargs is None:
        scan_kwargs = {}
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)

    complete = False
    records = []
    while not complete:
        try:
            response = table.scan(**scan_kwargs)
        except botocore.exceptions.ClientError as error:
            raise Exception('Error quering DB: {}'.format(error))

        records.extend(response.get('Items', []))
        next_key = response.get('LastEvaluatedKey')
        scan_kwargs['ExclusiveStartKey'] = next_key

        complete = True if next_key is None else False
    return records


if __name__ == '__main__':
    table_name = "job-control-table"
    kwargs = {
        'FilterExpression': Attr("job_status").begins_with('F'),
    }
    [print(i) for i in scan_db(table_name, kwargs)]
