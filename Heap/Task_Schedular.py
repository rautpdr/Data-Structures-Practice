from collections import Counter
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        heap = []
        res = []
        msg = "idle"

        for t, f in counter.items():
            heapq.heappush(heap, (-f, t))

        while heap:
            temp = []
            extra = n + 1

            for i in range(extra):
                if heap:
                    freq, task = heapq.heappop(heap)
                    res.append(task)
                    if -freq > 1:
                        heapq.heappush(temp, (freq + 1, task))
                else:
                    res.append(msg)

            for item in temp:
                heapq.heappush(heap, item)

            while res and res[-1] == msg and not heap:
                res.pop()

        return len(res)

# Main function
if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    sol = Solution()
    result = sol.leastInterval(tasks, n)
    print("Minimum time units to finish all tasks:", result)
