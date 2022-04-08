# Leetcode 11. Container With Most Water
#
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium

# Solution using TwoPointers
# Complexity:
#   O(N) time | where N represent the number of elements in the array
#   O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1

        water = 0

        max_height = max(height)

        while l < r and (r - l) * max_height > water:

            water = max(water, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:

                l += 1

            else:

                r -= 1

        return water
