
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the root of a binary tree, return the sum of values of its deepest leaves.

    Example 1:
        Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
        Output: 15

    Example 2:
        Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
        Output: 19

    Constraints:
        - The number of nodes in the tree is in the range [1, 10^4].
        - 1 <= Node.val <= 100
    """
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # BFS to traverse the tree level by level
        queue = deque([root])
        while queue:
            level_sum = 0  # Sum of the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return level_sum


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
    root = build_tree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
    assert solution.deepestLeavesSum(root) == 15

def test_example2():
    solution = Solution()
    root = build_tree([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
    assert solution.deepestLeavesSum(root) == 19

def test_single_node():
    solution = Solution()
    root = build_tree([10])
    assert solution.deepestLeavesSum(root) == 10

def test_left_skewed_tree():
    solution = Solution()
    root = build_tree([1, 2, None, 3, None, 4, None])
    assert solution.deepestLeavesSum(root) == 4

def test_right_skewed_tree():
    solution = Solution()
    root = build_tree([1, None, 2, None, 3, None, 4])
    assert solution.deepestLeavesSum(root) == 4

def test_balanced_tree():
    solution = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert solution.deepestLeavesSum(root) == 22

def test_large_tree():
    solution = Solution()
    root = build_tree([1] + [2] * 1023)  # A complete binary tree with 1024 nodes
    assert solution.deepestLeavesSum(root) == 2048
