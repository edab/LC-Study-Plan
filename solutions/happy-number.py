# Leetcode 202. Happy Number
#
# Link: https://leetcode.com/problems/happy-number/
# Difficulty: Easy

# Solution using HashSet.
# Complexity:
#   O(?) time
#   O(?) space
class Solution:

    def isHappy(self, n: int) -> bool:
        visited = set()

        if n == 1:
            return True

        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

    def sumOfSquares(self, n: int):
        result = 0

        while n:
            digit = n % 10
            result += digit ** 2
            n = n // 10

        return result
