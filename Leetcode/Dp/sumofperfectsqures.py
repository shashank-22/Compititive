import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp =[0]*(n+1)
        kn=math.sqrt(n)
        dp[1] = 1
        if(n==1 or kn-int(kn)==0):
            return 1
        
        for i in range(2,n+1):
            temp=dp[1]+dp[i-1]
            k=math.sqrt(i)
            if(k-int(k) !=0):
                for j in range(2,int(math.sqrt(i))+1):
                    if(temp>dp[j*j]+dp[i-j*j]):
                        temp=dp[j*j]+dp[i-j*j]
                    if(temp==2):
                        break
                dp[i]=temp
            elif(dp[i-1]==1):
                dp[i]=2
            else:
                dp[i]=1
        # print(dp)
        return dp[n]
        