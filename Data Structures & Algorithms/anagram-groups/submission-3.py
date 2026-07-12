class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        for word in strs:
            count = [0]*26 #a....z
            for char in word:
                count[ord(char)-ord('a')]+=1 #key is anagram pattern, values are all words that follow that pattern
            result[tuple(count)].append(word)
        return list(result.values())
