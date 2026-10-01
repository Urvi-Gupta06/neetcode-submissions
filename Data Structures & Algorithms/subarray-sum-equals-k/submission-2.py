class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        curr=0
        prefixSums = {0:1}
        
        for n in nums:
            curr+=n
            diff = curr - k

            count+=prefixSums.get(diff,0)
            prefixSums[curr] = 1 + prefixSums.get(curr,0)

        return count
     
            
            