# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution:
    def isvalid(self,s):
        if(int(s)<=26 and int(s)>=1):
            return True
        return False
    
    def numDecodings(self, A):
        maps = {}
        maps['']=1
        for i in range(len(A)):
            st = len(A)-i-1
            s=A[st:]
            
            if(s[0]=='0'):
                maps[s]=0
            elif(len(s)==1 and int(s)<=9 and int(s)>=1):
                maps[s]=1
            else:
                if(self.isvalid(s[0]) and self.isvalid(s[0:2])):
                    maps[s] = maps[s[1:]]+maps[s[2:]]
                elif(self.isvalid(s[0])):
                    maps[s] = maps[s[1:]]
                elif(self.isvalid(s[0:2])):
                    maps[s] = maps[s[2:]]
        return maps[A]