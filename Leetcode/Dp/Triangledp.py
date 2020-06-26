class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        dp = []
        dp.append(t[-1])
        l = len(t)
        for i in range(1,l):
            temp = []
            for j in range(0,len(t[l-i-1])):
                temp.append(min(dp[i-1][j],dp[i-1][j+1])+t[l-i-1][j])
            dp.append(temp)
        return dp[-1][-1]