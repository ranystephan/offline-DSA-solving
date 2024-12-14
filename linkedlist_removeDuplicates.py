
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
    Return the linked list sorted as well.

    Example 1:
        Input: head = [1,1,2]
        Output: [1,2]

    Example 2:
        Input: head = [1,1,2,3,3]
        Output: [1,2,3]

    Constraints:
        - The number of nodes in the list is in the range [0, 300].
        - -100 <= Node.val <= 100
        - The list is guaranteed to be sorted in ascending order.
    """
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


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
    head = build_linked_list([1, 1, 2])
    result = solution.deleteDuplicates(head)
    assert linked_list_to_list(result) == [1, 2]

def test_example2():
    solution = Solution()
    head = build_linked_list([1, 1, 2, 3, 3])
    result = solution.deleteDuplicates(head)
    assert linked_list_to_list(result) == [1, 2, 3]

def test_no_duplicates():
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.deleteDuplicates(head)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5]

def test_all_duplicates():
    solution = Solution()
    head = build_linked_list([1, 1, 1, 1, 1])
    result = solution.deleteDuplicates(head)
    assert linked_list_to_list(result) == [1]

def test_empty_list():
    solution = Solution()
    head = build_linked_list([])
    result = solution.deleteDuplicates(head)
    assert linked_list_to_list(result) == []

def test_large_list():
    solution = Solution()
    head = build_linked_list([i for i in range(1, 101)] * 2)  # Duplicates from 1 to 100
    result = solution.deleteDuplicates(head)
    assert linked_list_to_list(result) == list(range(1, 101))
