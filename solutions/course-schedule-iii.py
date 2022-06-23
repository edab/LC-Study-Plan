# Leetcode 630. Course Schedule III
#
# Link: https://leetcode.com/problems/course-schedule-iii/
# Difficulty: Hard

# Solution using heap
# Complexity:
#   O(N log N) time | where N represent the number of elements if the given array
#   O(N) time | where N represent the number of elements if the given array

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        heap = []

        courses.sort(key = lambda x: x[-1])

        current_time = 0

        for time, end in courses:

            current_time += time

            heapq.heappush(heap, -time)

            if current_time > end:
                current_time += heapq.heappop(heap)

        return len(heap)
