# leetcode_minimum_depth_binary_tree.py

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
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node 
    down to the nearest leaf node.

    Note: A leaf is a node with no children.

    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 2

    Example 2:
        Input: root = [2,null,3,null,4,null,5,null,6]
        Output: 5

    Constraints:
        - The number of nodes in the tree is in the range [0, 10^5].
        - -1000 <= Node.val <= 1000
    """
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Breadth-First Search (BFS) to find the first leaf node
        queue = deque([(root, 1)])  # Store node along with its depth
        while queue:
            node, depth = queue.popleft()
            # If it's a leaf node, return its depth
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


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
    assert solution.minDepth(root) == 2

def test_example2():
    solution = Solution()
    root = build_tree([2, None, 3, None, 4, None, 5, None, 6])
    assert solution.minDepth(root) == 5

def test_empty_tree():
    solution = Solution()
    root = build_tree([])
    assert solution.minDepth(root) == 0

def test_single_node():
    solution = Solution()
    root = build_tree([1])
    assert solution.minDepth(root) == 1

def test_full_tree():
    solution = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert solution.minDepth(root) == 2

def test_left_skewed_tree():
    solution = Solution()
    root = build_tree([1, 2, None, 3, None, 4])
    assert solution.minDepth(root) == 4

def test_right_skewed_tree():
    solution = Solution()
    root = build_tree([1, None, 2, None, 3, None, 4])
    assert solution.minDepth(root) == 4
