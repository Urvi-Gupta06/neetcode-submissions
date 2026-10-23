class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i]>0:
                break
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l=i+1
            r=len(nums)-1

            while l<r:
                threeSum = nums[i]+nums[l]+nums[r]

                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:#avoid duplicates
                        l+=1
                    while nums[r]==nums[r+1] and l<r: #avoid duplicates
                        r-=1
        return res

        '''
        -1,-1,0,1,2

        i=0, l=1, r=5
        (1<5)
        threeSum= -1 + -1 + 2 = 0 = 0: res = [[-1,-1,2]]
        l->2, r->4
        
        -1==-1 and 1<5: l->2
        0!=-1 - we can continue with l=2

        i=0,l=2,r=4
        (2<5)
        threeSum = -4 + -1 + 2 = -3 < 0: l->3'''
