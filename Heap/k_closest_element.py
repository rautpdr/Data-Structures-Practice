import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) < k:
            return []

        heap = []

        for val in arr:
            dist = abs(val - x)

            if len(heap) < k:
                heapq.heappush(heap, (-1 * dist, val))
            else:
                if dist < -1 * heap[0][0] :
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-1 * dist, val))

        return sorted([val for _, val in heap])


def main():
    sol = Solution()
    arr = [1, 1, 2, 2, 2, 5, 7, 8]
    k = 4
    x = 5
    result = sol.findClosestElements(arr, k, x)
    print("The closest elements are:", result)

if __name__ == "__main__":
    main()
