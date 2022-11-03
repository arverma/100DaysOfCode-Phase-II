def generate_combinations(s, k):
    res = []
    for i in range(len(s)-k+1):
        res.append(s[i:i+k])
    return res


print(generate_combinations("abcd", 2))