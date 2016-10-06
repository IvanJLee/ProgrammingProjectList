#! /usr/bin/env python
# coding=utf-8

# author: Ivan J. Lee
# date: 2016-10-06 23:43
# description: reverse a string----input a string, reverse it and print it

def reverse1(s):
    l = list(s)
    l.reverse()
    return "".join(l)

def reverse2(s):
    length = len(s)
    l = list(s)
    for x in range(length//2):
        t = l[x]
        l[x] = l[-x-1]
        l[-x-1] = t
    return "".join(l)

s = input("Enter a string:")
print('reverse 1:', reverse1(s))
print('reverse 2:', reverse2(s))
