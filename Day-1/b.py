# https://stackoverflow.com/questions/32122022/split-a-string-into-pieces-of-max-length-x-split-only-at-spaces
import textwrap


def text_wrapper_break_words(string, n):
    counter = 0
    start = 0
    str_list = []
    for i in string:
        counter += 1
        if counter >= n:
            str_list.append(string[start:start+counter])
            start += counter
            counter = 0
    return str_list


def text_wrapper_no_words_break(text, n):
    words = iter(text.split())
    lines, current = [], next(words)
    for word in words:
        if len(current) + 1 + len(word) > n:
            lines.append(current)
            current = word
        else:
            current += " " + word
    lines.append(current)
    return lines

    # str_list = string.split()
    # res = []
    # temp = next(iter(str_list))
    # i = 1
    # while i < len(str_list):
    #     for j in range(i, len(str_list)):
    #         if len(temp + " " + str_list[j]) <= n:
    #             temp += " " + str_list[j]
    #             i += 1
    #         else:
    #             break
    #     res.append(temp)
    #     temp = next(iter(str_list[i::]))
    #     i += 1
    # res.append(temp)
    # return res


def text_wrapper_with_inbuilt_function(string, n):
    return textwrap.wrap(string, n, break_long_words=False)


text = "hello, this is some text to break up, with some reeeeeeeeeaaaaaaally long words. If you want to code it " \
       "yourself, this is how I would approach it: First, split the text into words. Start with the first word in a " \
       "line and iterate the remaining words. If the next word fits on the current line, add it, otherwise finish " \
       "the current line and use the word as the first word for the next line. Repeat until all the words are used up."

num = 8
print("\n".join(text_wrapper_no_words_break(text, num)), len(text_wrapper_no_words_break(text, num)))
print()
print("\n".join(text_wrapper_with_inbuilt_function(text, num)), len(text_wrapper_with_inbuilt_function(text, num)))
