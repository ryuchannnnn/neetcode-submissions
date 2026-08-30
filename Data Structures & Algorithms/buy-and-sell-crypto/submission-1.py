class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPtr = 0 # buying
        rightPtr = 1 # selling
        maxGain = 0
        while(rightPtr < len(prices)):
            # check if profitable transaction
            if(prices[leftPtr] < prices[rightPtr]):
                profit = prices[rightPtr] - prices[leftPtr]
                maxGain = max(maxGain, profit)
            else: 
                leftPtr = rightPtr
            rightPtr += 1
        return maxGain
        