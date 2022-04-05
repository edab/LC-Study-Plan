# Leetcode 55. Jump Game
#
# Link: https://leetcode.com/problems/jump-game/
# Difficulty: Medium

# Solution using Greedy.
# Complexity:
#   O(N) time | where N represent the length of the input array
#   O(1) space
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal_index = len(nums) - 1

        for index in range(len(nums)-2, -1, -1):
            if index + nums[index] >= goal_index:
                goal_index = index

        return goal_index == 0
            
