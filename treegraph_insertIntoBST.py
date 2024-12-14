
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
    Given the root node of a binary search tree (BST) and a value to insert into the tree, 
    return the root node of the BST after the insertion. It is guaranteed that the new value 
    does not exist in the original BST.

    Example 1:
        Input: root = [4,2,7,1,3], val = 5
        Output: [4,2,7,1,3,5]

    Example 2:
        Input: root = [40,20,60,10,30,50,70], val = 25
        Output: [40,20,60,10,30,50,70,null,null,25]

    Example 3:
        Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
        Output: [4,2,7,1,3,5]

    Constraints:
        - The number of nodes in the tree will be in the range [0, 10^4].
        - -10^8 <= Node.val <= 10^8
        - All the values Node.val are unique.
        - -10^8 <= val <= 10^8
        - It's guaranteed that val does not exist in the original BST.
    """
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


# Helper function to build a binary tree from a list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
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


# Helper function to convert a binary tree to a list (level-order traversal)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to a list (level-order traversal)."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


# Pytest test cases
def test_example1():
    solution = Solution()
    root = build_tree([4, 2, 7, 1, 3])
    result = solution.insertIntoBST(root, 5)
    assert tree_to_list(result) == [4, 2, 7, 1, 3, 5]

def test_example2():
    solution = Solution()
    root = build_tree([40, 20, 60, 10, 30, 50, 70])
    result = solution.insertIntoBST(root, 25)
    assert tree_to_list(result) == [40, 20, 60, 10, 30, 50, 70, None, None, 25]

def test_example3():
    solution = Solution()
    root = build_tree([4, 2, 7, 1, 3, None, None, None, None, None, None])
    result = solution.insertIntoBST(root, 5)
    assert tree_to_list(result) == [4, 2, 7, 1, 3, 5]

def test_empty_tree():
    solution = Solution()
    root = build_tree([])
    result = solution.insertIntoBST(root, 42)
    assert tree_to_list(result) == [42]

def test_insert_left():
    solution = Solution()
    root = build_tree([10])
    result = solution.insertIntoBST(root, 5)
    assert tree_to_list(result) == [10, 5]

def test_insert_right():
    solution = Solution()
    root = build_tree([10])
    result = solution.insertIntoBST(root, 15)
    assert tree_to_list(result) == [10, None, 15]

def test_large_tree():
    solution = Solution()
    root = build_tree([i for i in range(1, 16)])
    result = solution.insertIntoBST(root, 20)
    assert tree_to_list(result).count(20) == 1
