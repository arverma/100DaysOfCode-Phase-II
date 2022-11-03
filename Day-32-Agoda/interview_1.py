# import requests
# import mysql.connector
# import pandas as pd

# print('Hello')


#    Print out `line` `count` times

#    printMe(3, “Hello”)

#    Hello
#    Hello
#    Hello

#    public static void printMe(int count, String line) {

#   }

#  def printMe(n, line):
#      if n <= 0:
#          return
#      print(line)
#      printMe(n-1, line)

# printMe(3, "Hello")


# An anagram is a word  formed by rearranging the letters of a different word:

# evil = vile

# You are given a list of words, group the one which are anagrams to each other:

# Input:

# List(
# cat
# fresher
# freshre
# refresh
# rots
# sunders
# sort
# undress
# )


# Output:
# List(
# List(sunders, undress),
# List(fresher, refresh, freshre),
# List(rots, sort),
# )


def group_anagram():
    arr = httpClient.getWords

    anagram_dict = {}  # O(n)
    for string in arr:
        sorted_str = sorted(list(string))  # O(K)
        key = "".join(sorted_str)
        temp = anagram_dict.get(key, [])
        temp.append(string)
        anagram_dict[key] = temp

    remove_key = []  # O(n)
    for key, val in anagram_dict.items():
        if len(val) <= 1:
            remove_key.append(key)

    for key in remove_key:
        anagram_dict.pop(key)

    return [val for val in anagram_dict.values()]


input_list = ["cat", "fresher", "freshre", "refresh", "rots", "sunders", "sort", "undress"]
output = group_anagram(input_list)
print(output)

# Scaling:
# Given DB supporting 200 reads/sec
# Scale to support 600 reads/sec