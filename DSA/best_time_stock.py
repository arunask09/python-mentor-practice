# Brute force: ______ → O(n2) time, O(n) space
# Running min: ______ → O(n) time, O(n) space

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1

        return max_profit



# Input: prices = [10,1,5,6,7,1]
# Output: 6