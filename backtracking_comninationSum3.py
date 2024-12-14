
from typing import List

class Solution:
    """
    Find all valid combinations of k numbers that sum up to n using numbers 1 through 9.

    Example 1:
        Input: k = 3, n = 7
        Output: [[1,2,4]]

    Example 2:
        Input: k = 3, n = 9
        Output: [[1,2,6],[1,3,5],[2,3,4]]

    Example 3:
        Input: k = 4, n = 1
        Output: []

    Constraints:
        - 2 <= k <= 9
        - 1 <= n <= 60
    """
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, k: int, target: int, path: List[int]) -> None:
            # Base case: if k == 0 and target == 0, we found a valid combination
            if k == 0 and target == 0:
                result.append(path[:])
                return
            # If k < 0 or target < 0, stop exploring
            if k < 0 or target < 0:
                return
            
            # Try each number from `start` to 9
            for i in range(start, 10):
                # Include `i` in the current combination and move to the next number
                path.append(i)
                backtrack(i + 1, k - 1, target - i, path)
                # Backtrack by removing the last number
                path.pop()
        
        # Start the backtracking
        backtrack(1, k, n, [])
        return result


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.combinationSum3(3, 7) == [[1, 2, 4]]

def test_example2():
    solution = Solution()
    result = solution.combinationSum3(3, 9)
    expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert sorted(result) == sorted(expected)

def test_example3():
    solution = Solution()
    assert solution.combinationSum3(4, 1) == []

def test_minimum_case():
    solution = Solution()
    assert solution.combinationSum3(2, 3) == [[1, 2]]

def test_maximum_case():
    solution = Solution()
    result = solution.combinationSum3(9, 45)
    expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert result == expected

def test_no_solution():
    solution = Solution()
    assert solution.combinationSum3(3, 2) == []

def test_large_target_with_small_k():
    solution = Solution()
    result = solution.combinationSum3(2, 17)
    expected = [[8, 9]]
    assert result == expected
