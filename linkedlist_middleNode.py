
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    Example 1:
        Input: head = [1,2,3,4,5]
        Output: [3,4,5]
        Explanation: The middle node of the list is node 3.

    Example 2:
        Input: head = [1,2,3,4,5,6]
        Output: [4,5,6]
        Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

    Constraints:
        - The number of nodes in the list is in the range [1, 100].
        - 1 <= Node.val <= 100
    """
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Helper functions for testing
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """Builds a linked list from a list of values and returns the head."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Converts a linked list to a list of values."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Pytest test cases
def test_example1():
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.middleNode(head)
    assert linked_list_to_list(result) == [3, 4, 5]

def test_example2():
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    result = solution.middleNode(head)
    assert linked_list_to_list(result) == [4, 5, 6]

def test_single_node():
    solution = Solution()
    head = build_linked_list([1])
    result = solution.middleNode(head)
    assert linked_list_to_list(result) == [1]

def test_two_nodes():
    solution = Solution()
    head = build_linked_list([1, 2])
    result = solution.middleNode(head)
    assert linked_list_to_list(result) == [2]

def test_long_list():
    solution = Solution()
    head = build_linked_list(list(range(1, 101)))  # 1 to 100
    result = solution.middleNode(head)
    assert linked_list_to_list(result) == list(range(51, 101))
