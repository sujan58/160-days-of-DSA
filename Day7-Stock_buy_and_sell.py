from typing import List
class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for i in range(1, n):
            # If today's price is higher than yesterday's, sell the stock
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends
