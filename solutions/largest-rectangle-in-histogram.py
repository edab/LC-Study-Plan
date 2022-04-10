# Leetcode 84. Largest Rectangle in Histogram
#
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Difficulty: Hard

# Solution using stack and extend logic
# Complexity:
#   O(N) time | where N is the length of the input list
#   O(N) space | where N is the length of the input list
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # pair: index, height
        max_area = 0

        for i, h in enumerate(heights):

            start = i #

            while stack and stack[-1][1] > h:

                # we remove old heigher element since they cannot extend further
                higher_index, higher_height = stack.pop()
                max_area = max(max_area, higher_height * (i - higher_index))

                # we also extend our start index since was heigher
                start = higher_index

            # we add the current height with the new start, since we can extend on left side
            stack.append((start, h))


        # All remaining heights, can be extended left through all the graph
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
