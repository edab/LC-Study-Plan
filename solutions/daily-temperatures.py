# Leetcode 739. Daily Temperatures
#
# Link: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Easy

# Solution using MinStack (monotonic decreasing stack)
# Complexity:
#   O(N) time | where N is the length of the input list
#   O(M) space | where M is the number of longest consecutive decreasing sequence
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # Save index and temperature of smaller temperature
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                last_index = stack.pop()
                result[last_index] = (index - last_index)
            stack.append(index)

        return result
