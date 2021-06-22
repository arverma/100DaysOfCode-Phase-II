# Reverse a number

def reverse_1(num):
    return str(num)[::-1]


def reverse_2(num):
    temp = 0
    i = 0
    while num:
        temp = 10*temp + num % 10
        num = num//10
        i += 1
    return temp


a = [1234, 5678, 4324243]
for i in a:
    print(reverse_1(i), reverse_2(i))
