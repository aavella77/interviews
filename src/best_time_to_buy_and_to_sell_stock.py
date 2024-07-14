# 121. Best Time to Buy and Sell Stock
# Easy
# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
#
# Constraints:
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# Plan:
# The algorithm to solve this problem is quite simple. You need to keep track of the minimum price found so far and the maximum profit found so far while iterating through the list of prices. For each price, you calculate the profit that could be made by selling at that price (assuming you bought at the minimum price found so far), and update the maximum profit if this profit is higher.

# you should keep track of the minimum price found so far and the maximum profit found so far while iterating through the list. For each price, you calculate the profit that could be made by selling at that price (assuming you bought at the minimum price found so far), and update the maximum profit if this profit is higher.
#
# In this corrected code, we iterate through the list of prices only once. For each price, we update min_price if the current price is lower, and we calculate the profit that could be made by selling at the current price (assuming we bought at min_price). If this profit is higher than max_profit, we update max_profit. At the end of the loop, max_profit is the maximum profit that can be made.

# In the provided solution, the algorithm keeps track of the minimum price (min_price) and the maximum profit (max_profit) as it iterates through the list of prices.
#
# For each price in the list, the algorithm checks if it('s less than the current min_price. If it is, it updates min_price. This ensures that min_price always holds the lowest price encountered so far. '
#
# Then, it calculates the profit that could be made by selling at the current price (assuming the stock was bought at min_price). If this profit is greater than the current max_profit, it updates max_profit.
#
# This way, the algorithm ensures that it')s always considering the scenario of buying at the lowest price seen so far and selling at the current price. It doesn't matter if a higher price comes before a lower price, because the algorithm doesn't just look for the highest and lowest prices, it looks for the highest profit, which is the highest difference between a selling price and a lower buying price that came before it.
class Solution:
	def maxProfit(self, prices) -> int:
		min_price = float('inf')
		max_profit = 0

		for price in prices:
			min_price = min(min_price, price)
			profit = price - min_price
			max_profit = max(max_profit, profit)

		return max_profit


# Time complexity: O(n)
# Space complexity: O(1)
my_solution = Solution()
prices = [7,1,5,3,6,4]
print(my_solution.maxProfit(prices))
prices = [7,6,4,3,1]
print(my_solution.maxProfit(prices))
prices = [7,6,4,3,1, 10]
print(my_solution.maxProfit(prices))
prices = [7,6,4,3,1, 10, 2]
print(my_solution.maxProfit(prices))
