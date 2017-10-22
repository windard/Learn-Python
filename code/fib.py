# coding=utf-8


def fib(n):
    if n < 2:
        return n        
    return fib(n-1) + fib(n-2)

for i in xrange(10):
    print fib(i),
