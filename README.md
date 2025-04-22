# Hashmap allows to search in O(1), LinkedList and arrays O(n)

# Collision occurs when hash function tries to assign data to same index,
# e.g Franch (key) = index[0] (data)
#      USA (key) = index[0] (data) ... Collision

# Keys are immutable once they are assigned by value, can't change the keys.
# So must assign immutable data type to keys.

# Initialisation of hashmap/dict
# City_map = {} or City_map = dict()

# Adding values to hashmap
# Adding country as a key and list of cities as value
cities = ["Mumbai", "Pune", "Nagpur"]

# City_map["Maharashtra"] = []  # Initialising key because at start it doesn't exist
# City_map["Maharashtra"] += cities

# Result: {"Maharashtra" : ["Mumbai", "Pune", "Nagpur"]}

# Use defaultdict = all keys are already initialised.
from collections import defaultdict

City_map = defaultdict(list)
cities = ["Mumbai", "Pune", "Nagpur"]
City_map["Maharashtra"] += cities

# Result: {"Maharashtra" : ["Mumbai", "Pune", "Nagpur"]}

# 3 methods to retrieve data from dict

# hashmap.keys() = returns list of all of the keys in dict/hashmap
# hashmap.values() = returns list of all of the values in dict/hashmap
# hashmap.items() = returns tuple of all of the key-value pairs in dict/hashmap
