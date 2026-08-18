class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''n= len(nums)
        result = [0]*n
        pref = [0]*n
        suff = [0]*n

        pref[0]=suff[n-1]=1
        for i in range(1,n):
            pref[i]=nums[i-1]*pref[i-1]
        for i in range(n-2,-1,-1):
            suff[i]=nums[i+1]*suff[i+1]
        for i in range(n):
            result[i]=pref[i]*suff[i]
        return result'''

        n= len(nums)
        result = [0]*n

        prod = 1
        zero_cnt = 0 
        for i in range(n):
            if nums[i]!=0:
                prod = prod*nums[i]
            else:
                zero_cnt+=1
        
        if zero_cnt>1:
            return [0]*n

        if zero_cnt==0:
            for i in range(n):
                result[i]=prod//nums[i]

        if zero_cnt==1:
            for i in range(n):
                if nums[i]==0:
                    result[i]=prod
                else:
                    result[i]=0
        return result


        

        

            

