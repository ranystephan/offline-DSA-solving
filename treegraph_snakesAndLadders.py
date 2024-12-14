
from typing import List
from collections import deque

class Solution:
    """
    Simulates the Snakes and Ladders game on an n x n board. The goal is to reach the last square
    with the minimum number of dice rolls. If it's not possible to reach the last square, return -1.

    Example 1:
        Input: board = [[-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1],
                        [-1,35,-1,-1,13,-1],
                        [-1,-1,-1,-1,-1,-1],
                        [-1,15,-1,-1,-1,-1]]
        Output: 4

    Example 2:
        Input: board = [[-1,-1],
                        [-1,3]]
        Output: 1

    Constraints:
        - 2 <= n <= 20
        - board[i][j] is either -1 or in the range [1, n^2].
        - The squares labeled 1 and n^2 are not the starting points of any snake or ladder.
    """
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Convert 1D position to (row, col) in the matrix
        def get_coordinates(pos):
            row = (pos - 1) // n
            col = (pos - 1) % n
            if row % 2 == 0:  # Even rows move left to right
                return n - 1 - row, col
            else:  # Odd rows move right to left
                return n - 1 - row, n - 1 - col

        # BFS initialization
        visited = set()
        queue = deque([(1, 0)])  # (current square, steps)
        visited.add(1)
        
        while queue:
            current, steps = queue.popleft()
            if current == n * n:  # If we reach the final square
                return steps
            
            # Roll the dice (1 to 6)
            for dice_roll in range(1, 7):
                next_square = current + dice_roll
                if next_square > n * n:
                    break
                
                # Get the coordinates of the next square
                row, col = get_coordinates(next_square)
                
                # Check if the square has a snake or ladder
                if board[row][col] != -1:
                    next_square = board[row][col]
                
                # If the square has not been visited yet, enqueue it
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, steps + 1))
        
        return -1  # If there's no way to reach the final square


# Pytest test cases
def test_example1():
    solution = Solution()
    board = [[-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 15, -1, -1, -1, -1]]
    assert solution.snakesAndLadders(board) == 4

def test_example2():
    solution = Solution()
    board = [[-1, -1],
             [-1, 3]]
    assert solution.snakesAndLadders(board) == 1

def test_no_snakes_or_ladders():
    solution = Solution()
    board = [[-1, -1, -1],
             [-1, -1, -1],
             [-1, -1, -1]]
    assert solution.snakesAndLadders(board) == 4

def test_large_board():
    solution = Solution()
    board = [[-1] * 20 for _ in range(20)]
    assert solution.snakesAndLadders(board) == 19

def test_snake_and_ladder_chain():
    solution = Solution()
    board = [[-1, -1, -1],
             [-1, -1, 9],
             [-1, 8, -1]]
    assert solution.snakesAndLadders(board) == 1

def test_impossible_to_finish():
    solution = Solution()
    board = [[-1, -1, -1],
             [-1, -1, -1],
             [-1, -1, -1]]
    board[2][2] = 1  # Snake back to the start
    assert solution.snakesAndLadders(board) == -1
