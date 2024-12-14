
from typing import List
from collections import deque

class Solution:
    """
    Given an m x n matrix maze with empty cells ('.') and walls ('+'), find the nearest exit
    from the given entrance [entrancerow, entrancecol]. Return the number of steps in the shortest
    path to the nearest exit, or -1 if no such path exists.

    Example 1:
        Input: maze = [["+", "+", ".", "+"],
                       [".", ".", ".", "+"],
                       ["+", "+", "+", "."]], entrance = [1, 2]
        Output: 1

    Example 2:
        Input: maze = [["+", "+", "+"],
                       [".", ".", "."],
                       ["+", "+", "+"]], entrance = [1, 0]
        Output: 2

    Example 3:
        Input: maze = [[".", "+"]], entrance = [0, 0]
        Output: -1

    Constraints:
        - 1 <= m, n <= 100
        - maze[i][j] is either '.' or '+'.
        - entrance will always be an empty cell.
    """
    
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        # Mark the entrance as visited
        maze[entrance[0]][entrance[1]] = '+'
        
        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check bounds and whether the cell is empty
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.':
                    # If it's an exit, return the steps
                    if nx == 0 or ny == 0 or nx == rows - 1 or ny == cols - 1:
                        return steps + 1
                    # Mark the cell as visited and add to the queue
                    maze[nx][ny] = '+'
                    queue.append((nx, ny, steps + 1))
        
        return -1  # No exit found


# Pytest test cases
def test_example1():
    solution = Solution()
    maze = [["+", "+", ".", "+"],
            [".", ".", ".", "+"],
            ["+", "+", "+", "."]]
    entrance = [1, 2]
    assert solution.nearestExit(maze, entrance) == 1

def test_example2():
    solution = Solution()
    maze = [["+", "+", "+"],
            [".", ".", "."],
            ["+", "+", "+"]]
    entrance = [1, 0]
    assert solution.nearestExit(maze, entrance) == 2

def test_example3():
    solution = Solution()
    maze = [[".", "+"]]
    entrance = [0, 0]
    assert solution.nearestExit(maze, entrance) == -1

def test_no_exit():
    solution = Solution()
    maze = [["+", "+", "+", "+"],
            ["+", ".", ".", "+"],
            ["+", "+", "+", "+"]]
    entrance = [1, 1]
    assert solution.nearestExit(maze, entrance) == -1

def test_single_cell():
    solution = Solution()
    maze = [["."]]
    entrance = [0, 0]
    assert solution.nearestExit(maze, entrance) == -1

def test_multiple_paths():
    solution = Solution()
    maze = [["+", ".", ".", "+", ".", "+"],
            [".", ".", "+", ".", ".", "."],
            ["+", ".", "+", ".", "+", "+"],
            [".", ".", ".", ".", ".", "+"],
            ["+", "+", ".", "+", "+", "+"]]
    entrance = [1, 0]
    assert solution.nearestExit(maze, entrance) == 2

def test_large_maze():
    solution = Solution()
    maze = [["."] * 100 for _ in range(100)]
    maze[99][99] = "+"
    entrance = [0, 0]
    assert solution.nearestExit(maze, entrance) == 198  # Exit at the bottom right corner
