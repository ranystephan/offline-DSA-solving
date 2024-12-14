
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
    Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b 
    where v = |a.val - b.val| and a is an ancestor of b.

    Example 1:
        Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
        Output: 7
        Explanation: 
            We have various ancestor-node differences, some of which are given below:
            |8 - 3| = 5
            |3 - 7| = 4
            |8 - 1| = 7
            |10 - 13| = 3
            Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

    Example 2:
        Input: root = [1,null,2,null,0,3]
        Output: 3

    Constraints:
        - The number of nodes in the tree is in the range [2, 5000].
        - 0 <= Node.val <= 10^5
    """
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_min, current_max):
            if not node:
                return current_max - current_min
            current_min = min(current_min, node.val)
            current_max = max(current_max, node.val)
            left_diff = dfs(node.left, current_min, current_max)
            right_diff = dfs(node.right, current_min, current_max)
            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)


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
    root = build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    assert solution.maxAncestorDiff(root) == 7

def test_example2():
    solution = Solution()
    root = build_tree([1, None, 2, None, 0, 3])
    assert solution.maxAncestorDiff(root) == 3

def test_single_branch_tree():
    solution = Solution()
    root = build_tree([1, 2, None, 3, None, 4, None, 5])
    assert solution.maxAncestorDiff(root) == 4

def test_balanced_tree():
    solution = Solution()
    root = build_tree([4, 2, 6, 1, 3, 5, 7])
    assert solution.maxAncestorDiff(root) == 6

def test_large_values():
    solution = Solution()
    root = build_tree([100000, 50000, 150000, 25000, 75000, 125000, 175000])
    assert solution.maxAncestorDiff(root) == 125000

def test_all_same_values():
    solution = Solution()
    root = build_tree([5, 5, 5, 5, 5, 5, 5])
    assert solution.maxAncestorDiff(root) == 0
