#use hashmap
#sort the string in list
#sorted string returns list but for hashmap list wont work as they are mutable
#convert them to tuple
#if sorted tuple matches with the key then add value in the list of values for that particular key

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) #get back list of empty list for each value
        result = [] #to store result

        for s in strs:
            sorted_key = tuple(sorted(s))
            anagram_map[sorted_key].append(s)

        for ans in anagram_map.values():
            result.append(ans)

        return result



def main():
    solution = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(input_strs)

    print("Grouped Anagrams:")
    for group in result:
        print(group)

if __name__ == "__main__":
    main()






