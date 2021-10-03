# write a function that takes the logs and returns a data structure that associates to each user their earliest and
# latest access times.
import math


def get_user_stat(log):
    res = {}
    for l in log:
        res[l[1]] = [min(res.get(l[1], [math.inf, 0])[0], int(l[0])), max(res.get(l[1], [0, 0])[1], int(l[0]))]
    return res


logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]

print(get_user_stat(logs1))
