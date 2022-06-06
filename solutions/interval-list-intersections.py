# Leetcode 986. Interval List Intersections
#
# Link: https://leetcode.com/problems/interval-list-intersections/
# Difficulty: Medium

# Solution using two pointers
# Complexity:
#   O(N+M) time | where N and M are the number of elemets in the first and second array
#   O(1) space
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ptrA, ptrB = 0, 0
        result = []

        while ptrA < len(firstList) and ptrB < len(secondList):

            if secondList[ptrB][0] <= firstList[ptrA][1] and firstList[ptrA][0] <= secondList[ptrB][1]:
                 result.append([max(firstList[ptrA][0], secondList[ptrB][0]), min(firstList[ptrA][1], secondList[ptrB][1])])

            if firstList[ptrA][1] > secondList[ptrB][1]:
                ptrB += 1
            else:
                ptrA += 1

        return result
