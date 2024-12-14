
class Solution:
    """
    You are climbing a staircase. It takes n steps to reach the top. Each time you can either
    climb 1 or 2 steps. Return the number of distinct ways to climb to the top.

    Example 1:
        Input: n = 2
        Output: 2

    Example 2:
        Input: n = 3
        Output: 3

    Constraints:
        - 1 <= n <= 45
    """
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Initialize dp array
        dp = [0] * (n + 1)
        dp[1] = 1  # 1 way to climb 1 step
        dp[2] = 2  # 2 ways to climb 2 steps
        
        # Fill the dp array
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.climbStairs(2) == 2

def test_example2():
    solution = Solution()
    assert solution.climbStairs(3) == 3

def test_small_steps():
    solution = Solution()
    assert solution.climbStairs(1) == 1

def test_medium_steps():
    solution = Solution()
    assert solution.climbStairs(10) == 89

def test_large_steps():
    solution = Solution()
    assert solution.climbStairs(45) == 1836311903
