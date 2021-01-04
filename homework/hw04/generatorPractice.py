
def fibonacciSequence():
    x = 0
    y = 1
    while True:
        yield y
        x, y = y, x+y
