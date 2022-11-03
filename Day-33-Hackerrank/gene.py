import collections

def is_present(string, str_map):
    for s in string:
        if str_map.get(s):
            str_map[s] -= 1
        else:
            return False
    return True


def steadyGene(gene):
    n = len(gene)
    char_count_map = collections.Counter(gene)

    extra_char = ""
    for key, val in char_count_map.items():
        if val > n // 4:
            extra_char += key * (val - n // 4)

    if extra_char == "":
        return 0

    m = len(extra_char)

    for i in range(m, n + 1):
        for j in range(n - i + 1):
            print(i, j, extra_char, gene[j:i + j])
            if is_present(extra_char, collections.Counter(gene[j:i + j])):
                return i