"""
Backspacing:

i/p -> "abc#def##"
o/p -> "abd"


You can also do it using stack
"""


def implement_backspacing(s):
    ans = ""
    for i, c in enumerate(s):
        if c == "#":
            ans = ans[0:-1]
        else:
            ans += c
    return ans


if __name__ == '__main__':
    s = "abc#def##"
    output = implement_backspacing(s)
    print(output)