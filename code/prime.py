# coding=utf-8

import math


def is_prime(n):
    for i in xrange(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def prime(n):
    while 1:
        if is_prime(n):
            return n
        n += 1


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print gcd(12, 15)
print prime(100)


class Father(object):
    def __init__(self):
        print 'father'


class Son(Father):
    def __init__(self):
        # super(Son, self).__init__()
        Father.__init__(self)
        print 'son'

s = Son()
