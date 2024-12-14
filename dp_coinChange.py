
from typing import List

class Solution:
    """
    Given coins of different denominations and a total amount, return the fewest number of coins
    needed to make up that amount. If it is not possible, return -1.

    Example 1:
        Input: coins = [1, 2, 5], amount = 11
        Output: 3

    Example 2:
        Input: coins = [2], amount = 3
        Output: -1

    Example 3:
        Input: coins = [1], amount = 0
        Output: 0

    Constraints:
        - 1 <= coins.length <= 12
        - 1 <= coins[i] <= 2^31 - 1
        - 0 <= amount <= 10^4
    """
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array where dp[i] represents the fewest coins to make up amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


# Pytest test cases
def test_example1():
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    assert solution.coinChange(coins, amount) == 3

def test_example2():
    solution = Solution()
    coins = [2]
    amount = 3
    assert solution.coinChange(coins, amount) == -1

def test_example3():
    solution = Solution()
    coins = [1]
    amount = 0
    assert solution.coinChange(coins, amount) == 0

def test_large_amount():
    solution = Solution()
    coins = [1, 2, 5]
    amount = 100
    assert solution.coinChange(coins, amount) == 20

def test_single_coin():
    solution = Solution()
    coins = [2]
    amount = 8
    assert solution.coinChange(coins, amount) == 4

def test_no_solution():
    solution = Solution()
    coins = [5, 10]
    amount = 3
    assert solution.coinChange(coins, amount) == -1

def test_multiple_coin_combinations():
    solution = Solution()
    coins = [3, 5, 7]
    amount = 12
    assert solution.coinChange(coins, amount) == 2  # 7 + 5 = 12
