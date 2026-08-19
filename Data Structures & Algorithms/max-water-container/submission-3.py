class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''result = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                result = max(result, min(heights[i], heights[j])*(j - i))
        return result'''

        result = 0
        l=0
        r=len(heights)-1

        while l<r:
            vol = min(heights[l],heights[r])*(r-l)
            result = max(result,vol)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return result 