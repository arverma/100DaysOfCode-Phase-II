__author__ = 'aman.rv'
# Codility AppleOrchardCoding

def solution(A, K, L):
    # write your code in Python 3.8.10
    def find_max_apple(a, k, l):
        if k + l > len(a):
            return -1
        sum_total = [a[0]]
        for i in range(1, len(a)):
            sum_total.append(sum_total[i-1]+a[i])

        max_num = -1
        x, y = 0, 0
        i = 0
        while i+k-1 < len(a):
            if i>0:
                x = sum_total[i+k-1] - sum_total[i-1]
            else:
                x = sum_total[i+k-1]

            j = i+k
            while j+l-1 < len(a):
                if j > 0:
                    y = sum_total[j+l-1] - sum_total[j-1]
                else:
                    y = sum_total[j+l-1]
            if x+y > max_num:
                max_num = x+y
                j += 1
            i += 1
        return max_num

    return max(find_max_apple(A, K, L), find_max_apple(A, L, K))