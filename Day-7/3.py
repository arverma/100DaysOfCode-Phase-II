# Check palindrome string

def check_palindrome(string):
    l = 0
    r = len(string)-1
    while r > l:
        if string[l] != string[r]:
            return False
        r -= 1
        l += 1
    return True


if __name__ == '__main__':
    print(check_palindrome('aman'))
    print(check_palindrome('amanama'))