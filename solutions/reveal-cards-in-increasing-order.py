# Leetcode 950. Reveal Cards In Increasing Order
#
# Link: https://leetcode.com/problems/reveal-cards-in-increasing-order/
# Difficulty: Medium

# Solution using a deque
# Complexity:
#   O(N) time | where N represent the number of elements in the input list
#   O(N) space | where N represent the number of elements in the input list
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans
