def fibonacii(n): #need help lol
    if n < 1:
        return None
    else:
        fib = (n - 1) + (n - 2)

        return fib

def interest(principle, rate):
    while principle > 1:
        total = principle(1 + rate)
        return total