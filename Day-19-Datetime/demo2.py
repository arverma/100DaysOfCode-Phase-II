# List of unique no. [2, 3, 4, 6, 7], k = 9

# [3, 3, 3], [3, 6], [2, 7], [2, 3, 4]


def comb_sum(arr, k, temp, i, result):
    if k < 0:
        return
    if k == 0:
        print(temp, result)
        result.append(temp[:])
        return
    if i < len(arr):
        temp.append(arr[i])
        comb_sum(arr, k - arr[i], temp, i, result)
        temp.pop()
        comb_sum(arr, k, temp, i + 1, result)
    return result


def dfs(nums, target, path, ret):
    print(nums, target, path, ret)
    if target < 0:
        return
    if target == 0:
        ret.append(path)
        return
    for i in range(len(nums)):
        dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
    return ret


a = [2, 3, 4]
k = 8
# print(comb_sum(a, k, [], 0, []))
print(dfs(a, k, [], []))