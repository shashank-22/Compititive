class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        finallenth = []
        low = 0 
        high = 0
        sumwin = 0
        while(high<len(arr)):
            if(sumwin==target):
                # print(low,high)
                finallenth.append([low,high-1])
                sumwin-=arr[low]
                low+=1
            elif(sumwin > target):
                sumwin-=arr[low]
                low+=1
            else:
                sumwin+=arr[high]
                high+=1
        
        while(sumwin>target):
            sumwin-=arr[low]
            low+=1
        if(sumwin==target):
            finallenth.append([low,high-1])
        # print(finallenth)       
        finallenth.sort(key=lambda x:(x[1]-x[0]))
        
        sum2=0
        count=0
        # print(finallenth)
        for i in range(len(finallenth)):
            for j in range(i+1, len(finallenth)):
                if(finallenth[i][1] < finallenth[j][0] or finallenth[i][0] > finallenth[j][1]):
                    return finallenth[i][1]-finallenth[i][0]+finallenth[j][1]-finallenth[j][0]+2
        return -1
        