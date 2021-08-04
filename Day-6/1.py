# Write a python program to print all prime numbers between a given input range
import math


def find_prime_numbers(s, e):
    res = []
    for i in range(max(s, 2), e):
        if all(i % j != 0 for j in range(2, math.floor(math.sqrt(i))+1)):
            res.append(i)
    return res


if __name__ == '__main__':
    print(find_prime_numbers(s=-3, e=100))