# Leetcode 347. Top K Frequent Elements
#
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium

# Solution using bucket sort
# Complexity:
#   O(N) | where N represent the number of elements in the array
#   O(N) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Bucket sort using an array where:
        #   index = count value
        #   value = list of input number with the same count

        frequency = [[] for _ in range(len(nums) + 1)]
        counters = defaultdict(int)
        result = []

        # Count number occurrences
        for num in nums:
          counters[num] += 1

        # Update frequency list
        for num, count in counters.items():
          frequency[count].append(num)

        # Get top k values
        for i in range(len(frequency) - 1, 0, -1):
          for value in frequency[i]:
            result.append(value)
            if len(result) >= k:
              return result

# Solution using max heap
# Complexity:
#   O(KlogN) time | where N represent the number of elements in the array and
#                   K is the numbers of counts to get
#   O(N) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_counts = defaultdict(int)
        counts = []
        result = []

        # Count number occurrences
        for num in nums:
          num_counts[num] += 1

        # Creates an array of tuples (count value, number)
        for num, count in num_counts.items():
          counts.append((-count, num))

        # Use heap and get top k values
        heapq.heapify(counts)
        for _ in range(k):
          result.append(heapq.heappop(counts)[1])

        return result
