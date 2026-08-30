class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPtr = 0
        rightPtr = 1
        maxPrice = 0
        while(rightPtr < len(prices)):
            if(prices[leftPtr] < prices[rightPtr]):
                profit = prices[rightPtr] - prices[leftPtr]
                maxPrice = max(maxPrice, profit)
            else: 
                leftPtr = rightPtr
            rightPtr += 1
        return maxPrice