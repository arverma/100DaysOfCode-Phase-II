"""
Suppose you have a big text log file and there are three columns:

------------------------------------
Name    |  City     | Timestamp
-------------------------------------
Jamie      city1        ts4
Dana       city1        ts3
Jamie      city2        ts1
Jamie      city3        ts3
Dana       city3        ts2
Jamie      city4        ts2
Dana       city4        ts1
===============================

The first column is a rider name, the second column is a city name, the final column is a timestamp (32 bit integer).
This log file maintains a history of riders. We define a "triple" to be a tuple of three consecutive cities a rider has been to that are ordered by timestamp.
Suppose t1<t2<t3<t4, then we will have the following triples:
for Jamie, we have: (city2, city4, city3) , (city4, city3, city1)
for Dana, we have: (city4, city3, city1)

Write a program
- to output all the triples in the file and
- for each triple, output the count of unique riders that have been to that triple.

For the example input, the output would be
(city2, city4, city3) 1
(city4, city3, city1) 2 ...

sample input"
input = Jamie,city1,1231321249
Dana,city1,1231321248
Jamie,city2,1231321245
Jamie,city3,1231321248
Dana,city3,1231321247
Jamie,city4,1231321247
Dana,city4,1231321245

k = 1, x xlogx
k = 2, y, ylogy



    Jamie,city1,1, 1
    Dana,city1,2, 1
    Dana,city2,5, 2
    Jamie,city2,3, 2

group by name, list(city, timestamp)
    Jamie,[(city1,1), (city2, 2)]
    Dana, [(city2, 2), (city1,1)]

"""


def find_city_visited_by_each_user(log):
    """

    """
    user_dict = {}
    for user_info in log:
        temp = user_dict.get(user_info[0], [])
        temp.append((user_info[1], user_info[2]))
        user_dict[user_info[0]] = temp
    return user_dict


def create_triple(user_nav):
    """

    """
    triple_dict = {}
    for val in user_nav.values():
        val.sort(key=lambda x: x[1])
        val = [v[0] for v in val]
        for i in range(len(val) - 2):
            triple_dict[" ".join(val[i:i + 3])] = triple_dict.get(" ".join(val[i:i + 3]), 0) + 1
    return triple_dict


if __name__ == '__main__':
    input = (
        ("Jamie", "city1", 1231321249),
        ("Dana", "city1", 1231321248),
        ("Jamie", "city2", 1231321245),
        ("Jamie", "city3", 1231321248),
        ("Dana", "city3", 1231321247),
        ("Jamie", "city4", 1231321247),
        ("Dana", "city4", 1231321245))
    user_dict = find_city_visited_by_each_user(input)  # O(n)
    print(user_dict)
    result = create_triple(user_dict)
    for key, val in result.items():
        print(tuple(key.split()), val)
