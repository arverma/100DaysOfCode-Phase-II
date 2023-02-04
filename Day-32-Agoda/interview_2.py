# # import requests
# # import mysql.connector
# # import pandas as pd
# import math
#
#
# # print('Hello')
#
# # List of prime number between 2 - 100 (Call minimum % or / operator)
#
# # def is_prime(num):
# #     for i in range(2, int(math.sqrt(num))+1):
# #         if num%i == 0:
# #             return False
# #     return True
#
#
# # def find_prime(start, end):
# #     for num in range(start, end+1):
# #         if is_prime(num):
# #             print(num)
#
#
# # find_prime(2, 100)
#
# # Given 2 very long number strings, return sum of these 2 number
# # Example
# # String a 		    = "100000000000000000000000000001"
# # String b 		    = "100000000000000000000000000002"
# # Expected result   = "200000000000000000000000000003"
# # Don't parse whole string to one number variable e.g. don't use int.Parse(a)
# # String a 		    = "10000000000000001"
# # String b 		    =           "1000002"
# # Expected result   = "10000000001000003"
#
# # def add_two_number(a, b):
# #     m = len(a) - 1
# #     n = len(b) - 1
# #     res = ""
# #     carry = 0
#
# #     while m > 0 or n > 0 or carry > 0:
# #         print(m, n, carry)
# #         if m >= 0:
# #             print(a[m])
# #             carry += int(a[m])
# #             m -= 1
# #         if n >= 0:
# #             print(b[n])
# #             carry += int(b[n])
# #             n -= 1
# #         res += str(carry%10)
# #         carry = carry//10
#
# #     return res
#
# # print(add_two_number("199", "9")[::-1])  #. 208
# # print(add_two_number("999", "9")[::-1]) #. 1008
#
# # Swap 2 string without create new variable
# # String a = "abcdef"  // Expected result : a = "ghij"
# # String b = "ghij"    // Expected result : b = "abcdef"
#
# def swap_two_string(str1, str2):
#     return str2, str1
#
#
# # a, b = b, a
# # print(a, b)
#
#
# a = "abcdef"
# b = "ghij"
# a = a + b  # abcdefghij
# b = a[0:len(a) - len(b)]
# a = a[len(b)::]
# print(a, b)
#
# News
# website
#
# DB < - Web
# Server < - Customer
# Website load very slow at night