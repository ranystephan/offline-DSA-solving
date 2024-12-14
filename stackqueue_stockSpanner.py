
class StockSpanner:
    """
    Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

    The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) 
    for which the stock price was less than or equal to the price of that day.

    Implement the StockSpanner class:
        - StockSpanner() Initializes the object of the class.
        - int next(int price): Returns the span of the stock's price given that today's price is price.

    Example:
        Input:
            ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
            [[], [100], [80], [60], [70], [60], [75], [85]]
        Output:
            [null, 1, 1, 1, 2, 1, 4, 6]

        Explanation:
            StockSpanner stockSpanner = new StockSpanner();
            stockSpanner.next(100); // return 1
            stockSpanner.next(80);  // return 1
            stockSpanner.next(60);  // return 1
            stockSpanner.next(70);  // return 2
            stockSpanner.next(60);  // return 1
            stockSpanner.next(75);  // return 4
            stockSpanner.next(85);  // return 6

    Constraints:
        - 1 <= price <= 10^5
        - At most 10^4 calls will be made to next.
    """

    def __init__(self):
        self.stack = []  # Stack to store pairs of (price, span)

    def next(self, price: int) -> int:
        span = 1
        # Pop elements from the stack while the price at the top of the stack is less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Pytest test cases
def test_example():
    spanner = StockSpanner()
    assert spanner.next(100) == 1
    assert spanner.next(80) == 1
    assert spanner.next(60) == 1
    assert spanner.next(70) == 2
    assert spanner.next(60) == 1
    assert spanner.next(75) == 4
    assert spanner.next(85) == 6

def test_increasing_prices():
    spanner = StockSpanner()
    assert spanner.next(10) == 1
    assert spanner.next(20) == 2
    assert spanner.next(30) == 3
    assert spanner.next(40) == 4

def test_decreasing_prices():
    spanner = StockSpanner()
    assert spanner.next(50) == 1
    assert spanner.next(40) == 1
    assert spanner.next(30) == 1
    assert spanner.next(20) == 1

def test_same_prices():
    spanner = StockSpanner()
    assert spanner.next(100) == 1
    assert spanner.next(100) == 2
    assert spanner.next(100) == 3
    assert spanner.next(100) == 4

def test_large_input():
    spanner = StockSpanner()
    for i in range(1, 10001):
        assert spanner.next(i) == i  # Increasing prices, span equals index
