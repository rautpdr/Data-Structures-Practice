import heapq
from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = Counter(arr)
        n = len(arr) // 2
        Store_f = 0
        i = 0
        heap = []

        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))

        while Store_f < n:
            if heap:
                freq, num = heapq.heappop(heap)
                i += 1
                Store_f -= freq  # -freq gives positive

        return i

# Main function
if __name__ == "__main__":
    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    sol = Solution()
    result = sol.minSetSize(arr)
    print("Minimum size of set to remove at least half of the array:", result)
