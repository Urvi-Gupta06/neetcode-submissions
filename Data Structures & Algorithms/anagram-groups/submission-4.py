class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''sorting
        res = defaultdict(list)
        for s in strs:
            sortedS: ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.valies())'''

        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c.lower())-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())