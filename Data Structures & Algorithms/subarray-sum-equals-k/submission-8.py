class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr = 0
        prefSum = {0:1} #initial sum = 0

        for n in nums:
            curr+=n
            diff = curr-k

            if diff in prefSum:
                count+= prefSum[diff]
            
            prefSum[curr]=1+prefSum.get(curr,0) 
        
        return count
            