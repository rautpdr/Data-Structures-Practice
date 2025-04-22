#Hashmap allows to search in O(1) , LinkedList and arrays O(n)
#Collision occurs when hash function tries to assign data to same index,
#e.g Franch (key)= index[0](data)
#USA(key) = index[0](data) ... Collision
#keys are immutatble once they are assigned by value, cant change the keys.
#so must assign immutable data type to keys

#Initialisation of hashmap/dict
# City_map = {} or City_map = dict()

#adding values to hashmap
#adding country as a key and list of cities as value
#cities = ["Mumbai" , "Pune" , "Nagpur"]
#City_map["Maharashtra"] = [] Initialising key beacuse at start it does't exists
#City_map["Maharashtra"] += cities
#{"Maharashtra" : ["Mumbai" , "Pune" , "Nagpur"]}

#use defaultdict = all keys are already initialised.
#from collections import defaultdict
#City_map = defaultdict()
#cities = ["Mumbai" , "Pune" , "Nagpur"]
#City_map["Maharashtra"] += cities
#{"Maharashtra" : ["Mumbai" , "Pune" , "Nagpur"]}

#3 methods to retrive data from dict
#hashmap.keys() = returns list of all of the key in dict/hashmap
#hashmap.values() = returns list of all of the values in dict/hashmap
#hashmap.items() = returns tuple of all of the key-value pair in dict/hashmap


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






