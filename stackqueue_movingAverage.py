
from collections import deque

class MovingAverage:
    """
    Given a stream of integers and a window size, calculate the moving average of all integers 
    in the sliding window.

    Implement the MovingAverage class:
        - MovingAverage(int size): Initializes the object with the size of the window size.
        - double next(int val): Returns the moving average of the last size values of the stream.

    Example:
        Input:
            ["MovingAverage", "next", "next", "next", "next"]
            [[3], [1], [10], [3], [5]]
        Output:
            [null, 1.0, 5.5, 4.66667, 6.0]

        Explanation:
            MovingAverage movingAverage = new MovingAverage(3);
            movingAverage.next(1); // return 1.0 = 1 / 1
            movingAverage.next(10); // return 5.5 = (1 + 10) / 2
            movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
            movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

    Constraints:
        - 1 <= size <= 1000
        - -10^5 <= val <= 10^5
        - At most 10^4 calls will be made to next.
    """

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.current_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.current_sum += val
        if len(self.window) > self.size:
            self.current_sum -= self.window.popleft()
        return self.current_sum / len(self.window)


# Pytest test cases
def test_example():
    obj = MovingAverage(3)
    assert obj.next(1) == 1.0
    assert obj.next(10) == 5.5
    assert obj.next(3) == 4.666666666666667
    assert obj.next(5) == 6.0

def test_window_size_1():
    obj = MovingAverage(1)
    assert obj.next(5) == 5.0
    assert obj.next(10) == 10.0
    assert obj.next(-3) == -3.0

def test_window_size_greater_than_stream():
    obj = MovingAverage(5)
    assert obj.next(2) == 2.0
    assert obj.next(4) == 3.0
    assert obj.next(6) == 4.0

def test_large_input():
    obj = MovingAverage(3)
    assert obj.next(100000) == 100000.0
    assert obj.next(200000) == 150000.0
    assert obj.next(300000) == 200000.0
    assert obj.next(400000) == 300000.0

def test_large_window():
    obj = MovingAverage(1000)
    for i in range(1, 1001):
        assert obj.next(i) == sum(range(1, i + 1)) / i
