
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
    (i.e., from left to right, then right to left for the next level and alternate between).

    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[20,9],[15,7]]

    Example 2:
        Input: root = [1]
        Output: [[1]]

    Example 3:
        Input: root = []
        Output: []

    Constraints:
        - The number of nodes in the tree is in the range [0, 2000].
        - -100 <= Node.val <= 100
    """
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        results = []
        queue = deque([root])
        left_to_right = True  # Toggle direction
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            results.append(level)
            left_to_right = not left_to_right  # Toggle the direction
        
        return results


# Helper function to build a binary tree from a list
def build_tree(values):
    """Builds a binary tree from a list of values (level-order traversal) and returns the root."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# Pytest test cases
def test_example1():
    solution = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    assert solution.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]

def test_example2():
    solution = Solution()
    root = build_tree([1])
    assert solution.zigzagLevelOrder(root) == [[1]]

def test_example3():
    solution = Solution()
    root = build_tree([])
    assert solution.zigzagLevelOrder(root) == []

def test_balanced_tree():
    solution = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert solution.zigzagLevelOrder(root) == [[1], [3, 2], [4, 5, 6, 7]]

def test_left_skewed_tree():
    solution = Solution()
    root = build_tree([1, 2, None, 3, None, 4, None])
    assert solution.zigzagLevelOrder(root) == [[1], [2], [3], [4]]

def test_right_skewed_tree():
    solution = Solution()
    root = build_tree([1, None, 2, None, 3, None, 4])
    assert solution.zigzagLevelOrder(root) == [[1], [2], [3], [4]]

def test_large_tree():
    solution = Solution()
    root = build_tree(list(range(1, 16)))
    assert solution.zigzagLevelOrder(root) == [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]]
