# Leetcode 42. Trapping Rain Water
#
# Link: https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard
# Complexity:
#   O(N) time | where N represent the number of elements in the input array
#   O(1) space

class Solution:

    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        maxleft, maxright = height[left], height[right]
        result = 0

        while left < right:

            if maxleft <= maxright:
                left += 1
                trapped_water = maxleft - height[left]
                if trapped_water > 0:
                    result += trapped_water
                maxleft = max(maxleft, height[left])
            elif maxright < maxleft:
                right -= 1
                trapped_water = maxright - height[right]
                if trapped_water > 0:
                    result += trapped_water
                maxright = max(maxright, height[right])

        return result
