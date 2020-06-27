# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?


class Solution:
    def uniquePathsWithObstacles(self, o: List[List[int]]) -> int:
        m=len(o)
        n=len(o[0])
        dp = [[1 for j in range(len(o[0]))] for i in range(len(o))]
        
        flag=0
        for i in range(m):
            if(o[i][0]==1):
                flag=1
            if(flag):
                dp[i][0]=0
        flag=0
        for i in range(n):
            if(o[0][i]==1):
                flag=1
            if(flag):
                dp[0][i]=0
            
        
        
        for i in range(m):
            for j in range(n):
                if(i==0 or j==0):
                    if(o[i][j]==1):
                        dp[i][j]=0
                        continue
                else:
                    if(o[i][j]==1):
                        dp[i][j]=0
                    else:
                        dp[i][j]=dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]