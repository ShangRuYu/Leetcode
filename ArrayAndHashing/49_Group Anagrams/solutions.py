# Sort and Map approach:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) 
        for s in strs:
            sortedS = ''.join(sorted(s)) # 'cool' --sorted--> ['c', 'l', 'o', 'o'] --join--> 'cloo'
            result[sortedS].append(s)
        return list(result.values()) # retrieves all the values from the map and turn them into a list
    

# Count and Map approach:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) 
        for s in strs:
            count = [0] * 26 # create a list of 26 zeros to represent the count of each character
            for char in s:
                count[ord(c) - ord('a')] += 1 # increment the count of the character
            result[tuple(count)].append(s) # use the count list as a key in the map
        return list(result.values())