'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
# We are given N numbers. We have to select K of them. We also have a number M . Suppose the numbers we selected were . (note that we write these numbers in order in which they appeared in the original array). Define .
# We have to maximize . sum(from i=0 to k) A[i]* (i%m)

# Constraints : 

 
 
 
 
# Input Format : 

#  In the first line, three space separated integers  are given. In the next line,  space separated integers  are given.

# Output Format :

# Print a single integer corresponding to the answer. 

 

# SAMPLE INPUT 
# 7 4 3
# 4 9 8 2 6 7 4
# SAMPLE OUTPUT 
# 32




n,k,m = map(int,input().split(" "))

nums = list(map(int,input().split(" ")))
def DP(arr,k,m):
    dp = [[0 for i in range(len(arr)+1)] for j in range(k+1)]

    for i in range(1,k+1):
        for j in range(i,len(arr)+1):
            if(i==j):
                dp[i][j] = arr[j-1]*(i%m) + dp[i-1][j-1]
            else:
                temp = arr[j-1]*(i%m)
                mx = dp[i-1][j-1]
                dp[i][j] = max(dp[i][j-1] , mx+temp)
    # print(dp)
    return dp[-1][-1]
if(n!=0):
    print(DP(nums,k,m))
else:
    print("0")