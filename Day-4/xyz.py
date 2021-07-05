# Threading communication in Python

def get_most_repeating_words(string):
    """

    :param string:
    :type string:
    :return:
    :rtype:
    """
    words = string.split()
    word_occ = {}
    for w in words:
        word_occ[w] = word_occ.get(w, 0) + 1
    # print(word_occ)

    max_occ = 0
    answer = ""
    for key, value in word_occ.items():
        if value > max_occ:
            max_occ = value
            answer = key
    return answer


if __name__ == '__main__':
    with open("input.txt", 'r') as lines:
        for line in lines:
            print(get_most_repeating_words(line))
