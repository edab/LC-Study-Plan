# Leetcode 841. Keys and Rooms
#
# Link: https://leetcode.com/problems/keys-and-rooms/
# Difficulty: Medium

# Solution using DFS.
# Complexity:
#   O(N) time | where N represent the number of elements in the input matrix
#   O(N) space | where N represent the number of elements in the input matrix
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        stack = [*rooms[0]]

        visited.add(0)

        while stack:

            room = stack.pop()
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)

        return len(visited) == len(rooms)
