"""Given two positive numbers X and Y, check if Y is a power of X or not.

Example 1
Input:
X = 2, Y = 8
Output:
1
Explanation:
2^3 is equal to 8.

Example 2
Input:
X = 1, Y = 3
Output:
0
Explanation:
Any power of 1 is not
equal to 8.
"""

# 8/2 = 4
# 4/2 = 2
# 2/2 = 1
#
# 9/2 = 4.5
#
# 10/2 = 5
# 5/2 = 2.5

"""

y = 8
x = 2

temp_y = 8
y = 4.0
    if 4.0 != 4
        
y = 4.0
temp_y = 4.0
y = 4.0/2 = 2.0
    if 2.0 != 2
        
y = 2.0
temp_y = 2.0
y = 1.0
    if 1.0 != 1
        
return 1
"""


def find_if_y_is_power_of_x(x, y):
    if x in (0, 1):
        return 0
    if y == 0:
        return 0
    while y > 1:
        temp_y = y
        y = y/x
        # 4.0 == 4
        # 4.5 != 4
        if y != temp_y//x:
            return 0
    return 1


if __name__ == '__main__':
    y = 8
    x = 2
    print(find_if_y_is_power_of_x(x, y))


"""
y = 10
x = 2

x^n = y
n = [0, m]

10> 1:
temp_y = 10
y = 5.0
if 5.0 != 5

5.0 > 1
    temp_y = 5.0
    y = 2.5
    if 2.5 != 2
        return 0
"""
#
# y = 0
# x = 5
# 5^0 = 1
#
# log[n] base[x]














