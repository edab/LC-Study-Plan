# Leetcode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
#
# Link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# Difficulty: Medium

# Solution using string search
# Complexity:
#   O(N) time | where N represent the number of chars in the give string
#   O(1) space
class Solution:
    def minPartitions(self, n: str) -> int:

        max_value = 0

        for data in range(9, -1, -1):
            if str(data) in n:
                return data
