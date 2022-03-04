# Leetcode 1344. Angle Between Hands of a Clock
#
# Link: https://leetcode.com/problems/angle-between-hands-of-a-clock/
# Difficulty: Medium
# Complexity:
#   O(1) time
#   O(1) space

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_hand_angle = (hour % 12 + minutes / 60) * 30
        minute_hand_angle = minutes * 6
        result = abs(hour_hand_angle - minute_hand_angle)
        if (result > 180):
            return 360 - result
        else:
            return result
