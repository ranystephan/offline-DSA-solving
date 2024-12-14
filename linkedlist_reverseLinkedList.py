
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given the head of a singly linked list and two integers left and right where left <= right,
    reverse the nodes of the list from position left to position right, and return the reversed list.

    Example 1:
        Input: head = [1,2,3,4,5], left = 2, right = 4
        Output: [1,4,3,2,5]

    Example 2:
        Input: head = [5], left = 1, right = 1
        Output: [5]

    Constraints:
        - The number of nodes in the list is n.
        - 1 <= n <= 500
        - -500 <= Node.val <= 500
        - 1 <= left <= right <= n

    Follow-up:
        - Could you do it in one pass?
    """
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: no need to reverse
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 1: Traverse to the node before `left`
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 2: Reverse the sublist from `left` to `right`
        current = prev.next
        next_node = None
        for _ in range(right - left + 1):
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp
        
        # Step 3: Reconnect the reversed sublist
        prev.next.next = current
        prev.next = next_node
        
        return dummy.next


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
    result = solution.reverseBetween(head, 2, 4)
    assert linked_list_to_list(result) == [1, 4, 3, 2, 5]

def test_example2():
    solution = Solution()
    head = build_linked_list([5])
    result = solution.reverseBetween(head, 1, 1)
    assert linked_list_to_list(result) == [5]

def test_full_reversal():
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseBetween(head, 1, 5)
    assert linked_list_to_list(result) == [5, 4, 3, 2, 1]

def test_partial_reversal_at_start():
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseBetween(head, 1, 3)
    assert linked_list_to_list(result) == [3, 2, 1, 4, 5]

def test_partial_reversal_at_end():
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseBetween(head, 3, 5)
    assert linked_list_to_list(result) == [1, 2, 5, 4, 3]

def test_no_reversal():
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseBetween(head, 3, 3)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5]

def test_large_list():
    solution = Solution()
    head = build_linked_list(list(range(1, 501)))
    result = solution.reverseBetween(head, 100, 200)
    expected = list(range(1, 100)) + list(range(200, 99, -1)) + list(range(201, 501))
    assert linked_list_to_list(result) == expected
