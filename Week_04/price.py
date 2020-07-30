# 买卖股票最佳时机
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_p = 0
        for i in range(N-1):
            if prices[i+1]>prices[i]:
                max_p += prices[i+1]-prices[i]
        return max_p