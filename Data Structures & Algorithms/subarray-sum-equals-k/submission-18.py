class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        memory = {0:1} #pref sum:freq
        curr_sum=0

        for n in nums:
            curr_sum+=n
            diff = curr_sum-k

            if diff in memory:
                count+=memory[diff]
            memory[curr_sum] = 1+memory.get(curr_sum,0)
        
        return count

        