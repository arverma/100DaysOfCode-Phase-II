def balanced_parenthesis(string):
    s2 = []
    bracket_dict = {"}": "{", ")": "(", "]": "["}
    for s in string[::-1]:
        print(s, s2)
        if bracket_dict.get(s):
            s2.append(bracket_dict.get(s))
        else:
            if s != s2.pop():
                return False
    return not s2


if __name__ == '__main__':
    string = "{()(]){}}"
    print("is balanced parenthesis? -", balanced_parenthesis(string))