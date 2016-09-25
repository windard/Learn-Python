#coding=utf-8

from random import randint

print [n for n in [randint(1,99) for i in range(10)] if n%2]