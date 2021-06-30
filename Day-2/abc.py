# Rate limiter API
# Shared resource -> client
# 1:20PM-2:20PM (K-times per n Hr)
from datetime import datetime


def rate_limiter(client_id, client_limit, expiry_time, limit):
    """
    client_limit = {}
    expiry_time = 1hr
    limit = 100
    cl1 = {"cl1": [1, 2:40]}
    cl2 = {"cl1": [1, 2:40], "cl2": [1, 2:41]}
    cl1(2:42) = {"cl1": [2, 2:40], "cl2": [1, 2:41]}

    :param client_id:
    :type client_id:
    :param client_limit:
    :type client_limit:
    :param expiry_time:
    :type expiry_time:
    :param limit:
    :type limit:
    :return:
    :rtype:
    """
    if client_id not in client_limit:
        current_time = datetime.now()
        client_limit[client_id] = [1, current_time]
    else:
        current_time = datetime.now()
        start_time = client_limit.get(client_id)[1]
        if current_time-start_time <= expiry_time and client_limit.get(client_id)[0] < limit:
            client_limit[client_id] = [client_limit.get(client_id)[0] + 1, start_time]
        elif current_time-start_time <= expiry_time and client_limit.get(client_id)[0] > limit:
            raise Exception("Limit Crossed")
        else:
            client_limit[client_id] = [1, current_time]
    return client_limit


if __name__ == '__main__':
    client_limit = {}
    limit = 100
    expiry_time = 60  # minute
    for client_id in range(10):
        client_limit = rate_limiter(client_id, client_limit, expiry_time, limit)
    print(client_limit)



