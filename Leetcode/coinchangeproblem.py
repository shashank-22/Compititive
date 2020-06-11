class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [0]*5001
        arr[0] = 1
        
        for coin in coins:
            for j in range(len(arr)):
                if(coin<=j):
                    arr[j]+=arr[j-coin]
        return arr[amount]