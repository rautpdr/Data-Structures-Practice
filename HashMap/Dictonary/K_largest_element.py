from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num , 0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Main function
def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    result = sol.topKFrequent(nums, k)
    print("Top", k, "frequent elements are:", result)

# Run main
if __name__ == "__main__":
    main()
