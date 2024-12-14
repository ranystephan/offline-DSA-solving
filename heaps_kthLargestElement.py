
from typing import List
import heapq

class KthLargest:
    """
    Maintains a stream of test scores and dynamically returns the kth largest score after each insertion.

    Example:
        Input:
        ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
        Output: [null, 4, 5, 5, 8, 8]
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Maintain a min-heap of size k to store the k largest elements
        self.min_heap = []
        for num in nums:
            self.add(num)  # Add each number from nums to the heap

    def add(self, val: int) -> int:
        # Add the new value to the min-heap
        heapq.heappush(self.min_heap, val)
        # If the heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # Return the kth largest element, which is the smallest element in the heap
        return self.min_heap[0]


# Pytest test cases
def test_example1():
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
    assert obj.add(4) == 8

def test_example2():
    obj = KthLargest(4, [7, 7, 7, 7, 8, 3])
    assert obj.add(2) == 7
    assert obj.add(10) == 7
    assert obj.add(9) == 7
    assert obj.add(9) == 8

def test_empty_initial_stream():
    obj = KthLargest(1, [])
    assert obj.add(5) == 5
    assert obj.add(10) == 10

def test_all_same_elements():
    obj = KthLargest(2, [7, 7, 7])
    assert obj.add(7) == 7
    assert obj.add(7) == 7

def test_large_k():
    obj = KthLargest(5, [10, 20, 30, 40, 50])
    assert obj.add(5) == 5
    assert obj.add(35) == 10
    assert obj.add(60) == 20
