class Solution:
    #bottom-up
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[0]=cost[0] #step 1 cost
        dp[1]=cost[1] #step 2 cost

        for i in range(2,len(cost)):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]

        return min(dp[len(cost)-1],dp[len(cost)-2])








        '''memo = {}

        def dfs(i): #min cost to reach the top from step i, including cost[i]
            if i>=len(cost):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = cost[i]+min(dfs(i+1),dfs(i+2))
            return memo[i]

        return min(dfs(0),dfs(1))'''

''' #top-down
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i): #min cost to reach step i from bottom, including cost[i]
            # We can start directly at either step.
            if i == 0 or i == 1:
                return cost[i]
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i - 1), dfs(i - 2))
            return memo[i]

        # Reach the top from either of the last two steps.
        n = len(cost)
        return min(dfs(n - 1), dfs(n - 2))'''
       
        
    

        


     
