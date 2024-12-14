
from typing import List

class Solution:
    """
    Given an m x n binary matrix grid, return the maximum area of an island in grid.
    An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical).
    If there is no island, return 0.

    Example 1:
        Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,1,1,0,1,0,0,0,0,0,0,0,0],
                       [0,1,0,0,1,1,0,0,1,0,1,0,0],
                       [0,1,0,0,1,1,0,0,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        Output: 6

    Example 2:
        Input: grid = [[0,0,0,0,0,0,0,0]]
        Output: 0

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 50
        - grid[i][j] is either 0 or 1
    """
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            # Check if (x, y) is out of bounds or water or already visited
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            grid[x][y] = 0  # Mark as visited
            area = 1  # Current cell
            # Explore neighbors
            area += dfs(x + 1, y)
            area += dfs(x - 1, y)
            area += dfs(x, y + 1)
            area += dfs(x, y - 1)
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area


# Pytest test cases
def test_example1():
    solution = Solution()
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    assert solution.maxAreaOfIsland(grid) == 6

def test_example2():
    solution = Solution()
    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert solution.maxAreaOfIsland(grid) == 0

def test_single_island():
    solution = Solution()
    grid = [[1]]
    assert solution.maxAreaOfIsland(grid) == 1

def test_disconnected_islands():
    solution = Solution()
    grid = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1]
    ]
    assert solution.maxAreaOfIsland(grid) == 2

def test_large_grid():
    solution = Solution()
    grid = [[1] * 50 for _ in range(50)]  # All land
    assert solution.maxAreaOfIsland(grid) == 2500

def test_no_land():
    solution = Solution()
    grid = [[0] * 10 for _ in range(10)]  # All water
    assert solution.maxAreaOfIsland(grid) == 0
