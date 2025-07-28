class Solution:
    def maximumProfit(self, prices):
        # code here
        minPrice = float('inf')
        profit = 0 
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > profit:
                profit = price - minPrice
                
        return profit