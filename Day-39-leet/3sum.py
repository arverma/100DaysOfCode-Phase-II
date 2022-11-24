__author__ = 'aman.rv'


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, a in enumerate(nums[0:-2]):
            j = i + 1
            k = len(nums) - 1
            while j < k and ((i == 0) or (i > 0 and nums[i] != nums[i - 1])):
                if nums[j] + nums[k] == -a:
                    triplet = [a, nums[j], nums[k]]
                    ans.append(triplet)

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > -a:
                    k -= 1
                else:
                    j += 1
        return ans
