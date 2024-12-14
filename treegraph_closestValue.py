
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
    Given the root of a binary search tree and a target value, return the value in the BST
    that is closest to the target. If there are multiple answers, return the smallest.

    Example 1:
        Input: root = [4,2,5,1,3], target = 3.714286
        Output: 4

    Example 2:
        Input: root = [1], target = 4.428571
        Output: 1

    Constraints:
        - The number of nodes in the tree is in the range [1, 10^4].
        - 0 <= Node.val <= 10^9
        - -10^9 <= target <= 10^9
    """
    
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val  # Initialize the closest value to the root's value

        while root:
            # Update the closest value if the current node is closer to the target
            if abs(root.val - target) < abs(closest - target) or \
               (abs(root.val - target) == abs(closest - target) and root.val < closest):
                closest = root.val
            
            # Traverse the left or right subtree based on the target
            root = root.left if target < root.val else root.right
        
        return closest


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
        if i < len(values) and values[i] is not None:
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
    root = build_tree([4, 2, 5, 1, 3])
    assert solution.closestValue(root, 3.714286) == 4

def test_example2():
    solution = Solution()
    root = build_tree([1])
    assert solution.closestValue(root, 4.428571) == 1

def test_left_skewed_tree():
    solution = Solution()
    root = build_tree([5, 3, None, 2, None, 1])
    assert solution.closestValue(root, 2.5) == 3

def test_right_skewed_tree():
    solution = Solution()
    root = build_tree([1, None, 2, None, 3, None, 4])
    assert solution.closestValue(root, 2.8) == 3

def test_large_target():
    solution = Solution()
    root = build_tree([4, 2, 5, 1, 3])
    assert solution.closestValue(root, 1000) == 5

def test_small_target():
    solution = Solution()
    root = build_tree([4, 2, 5, 1, 3])
    assert solution.closestValue(root, -1000) == 1

def test_multiple_closest_values():
    solution = Solution()
    root = build_tree([8, 4, 10, 2, 6])
    assert solution.closestValue(root, 7) == 6  # Prefer the smallest when distances are the same
