## Python 常用函数

用规定的Python方法，在一行中对给定的任意整数数列，按照如下规则排序：

a) 非负数在前，负数在后；
b) 非负数部分按照从小到大排序；
c) 负数部分按从大到小排序。

如： 数列 foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
希望排序后为[0,2,4,8,8,9,-2,-4,-4,-5,-20]

```
# coding=utf-8

foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]

# print sorted(foo, key=lambda x: (x >= 0 and -abs(1/float(x+1)) or abs(x)))

print sorted(foo, key=lambda x: - 1.0 / (x + 1) if x >= 0 else -x)

```

给出用递归的方式求斐波那契数列的第n项的方法：

（斐波那契数列指的是这样一个数列0，1，1，2，3，5，8，13，21，34，55，89，144，233，377，…）

特别指出：第0项是0，第1项是第一个1。这个数列从第2项开始，每一项都等于前两项之和。

```
# coding=utf-8


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

for i in xrange(10):
    print fib(i),

def fib(n):
    a = 1
    b = 1
    c = []
    c.append(a)
    while b < n:
        c.append(b)
        a,b = b,b+a
    return c
    
```

求大于正整数n的最小质数

```
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

```

求素数

```
# coding=utf-8

import math


def checkPrime(a):
    for i in xrange(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True


def prime(a):
    yield 2
    start = 3
    while 1:
        if start > a:
            break
        if checkPrime(start):
            yield start
        start += 2

```

分解质因数

```
# coding=utf-8

import math


def decompose(n):
    i = 1
    res = []
    while i < math.sqrt(n):
        i += 1
        if n % i == 0:
            n = n / i
            res.append(i)
            i = 1
    res.append(int(n))
    return res


def decomposeall(n):
    res = []
    for x in xrange(1, n+1):
        if n % x == 0:
            res.append(x)

    return res

```

有列表如下 `["foo", 2, "bar", 4, "far", 6]` 希望对其按一个，两个，三个分别打包

```
>>> a = ["foo", 2, "bar", 4, "far", 6]
>>> group_adjacent = lambda x, k: zip(*([iter(x)] * k))
>>> group_adjacent(a, 1)
[('foo',), (2,), ('bar',), (4,), ('far',), (6,)]
>>> group_adjacent(a, 2)
[('foo', 2), ('bar', 4), ('far', 6)]
>>> group_adjacent(a, 3)
[('foo', 2, 'bar'), (4, 'far', 6)]
>>> group_adjacent(a, 4)
[('foo', 2, 'bar', 4)]
```

或者这样

```
>>> a = ["foo", 2, "bar", 4, "far", 6]
>>> splite_list = lambda splist, s: [splist[i:i + s] for i in range(len(splist)) if i % s == 0]
>>> splite_list(a, 2)
[['foo', 2], ['bar', 4], ['far', 6]]
>>> splite_list(a, 3)
[['foo', 2, 'bar'], [4, 'far', 6]]
>>> splite_list(a, 4)
[['foo', 2, 'bar', 4], ['far', 6]]
```

什么是lambda函数？它有什么好处?

解答：

lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数
lambda函数：首要用途是指短小的回调函数
