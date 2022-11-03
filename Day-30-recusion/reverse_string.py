def reverse_string(string):
    if len(string) == 0:
        return ""
    return string[-1] + reverse_string(string[0:-1])


if __name__ == '__main__':
    output = reverse_string("aman ranjan verma")
    print(output)