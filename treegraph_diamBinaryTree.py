
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
    Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
    This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.

    Example 1:
        Input: root = [1,2,3,4,5]
        Output: 3
        Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

    Example 2:
        Input: root = [1,2]
        Output: 1

    Constraints:
        - The number of nodes in the tree is in the range [1, 10^4].
        - -100 <= Node.val <= 100
    """
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # Update the diameter with the sum of left and right depths
            self.diameter = max(self.diameter, left_depth + right_depth)
            # Return the depth of the current node
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter


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
    root = build_tree([1, 2, 3, 4, 5])
    assert solution.diameterOfBinaryTree(root) == 3

def test_example2():
    solution = Solution()
    root = build_tree([1, 2])
    assert solution.diameterOfBinaryTree(root) == 1

def test_single_node():
    solution = Solution()
    root = build_tree([1])
    assert solution.diameterOfBinaryTree(root) == 0

def test_left_skewed_tree():
    solution = Solution()
    root = build_tree([1, 2, None, 3, None, 4, None])
    assert solution.diameterOfBinaryTree(root) == 3

def test_right_skewed_tree():
    solution = Solution()
    root = build_tree([1, None, 2, None, 3, None, 4])
    assert solution.diameterOfBinaryTree(root) == 3

def test_balanced_tree():
    solution = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert solution.diameterOfBinaryTree(root) == 4

def test_large_tree():
    solution = Solution()
    root = build_tree([1] + [i for i in range(2, 1002)])  # A large skewed tree
    assert solution.diameterOfBinaryTree(root) == 1000
