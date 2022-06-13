class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        #min_price[i] is max price for (i+1) ~ (days-1)
        max_prices = [0] * days
        
        if days == 1:
            return 0
        max_prices[-1], max_prices[-2] = prices[-1], prices[-1]
        for i in range(days-3, -1, -1):
            if max_prices[i+1] < prices[i+1]:
                max_prices[i] = prices[i+1]
            else:
                max_prices[i] = max_prices[i+1]
        #print(max_prices)
        return max(0, max([max_prices[i] - prices[i] for i in range(days)]))
       
            
        