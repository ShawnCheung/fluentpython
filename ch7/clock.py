import time
import bisect
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        args_str = ', '.join(repr(arg) for arg in args)
        print("{}, {}({}) -> {}".format(elapsed, name, args_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    print('*'*40, 'Calling snooze(.123)')
    snooze(.123)
    print('*'*40, 'Calling factorial(6)')
    factorial(6)