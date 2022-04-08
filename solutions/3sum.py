# Leetcode 15. 3Sum
#
# Link: https://leetcode.com/problems/3sum/
# Difficulty: Medium

# Solution using TwoPointers
# Complexity:
#   O(N) time | where N represent the number of elements in the array
#   O(1) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums.sort()

        for i, a in enumerate(nums):

            # Jump first number if already seen
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:

                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1

                    # Jump next number if already seen
                    while nums[l] == nums[l-1] and l<r:
                        l += 1

        return result
