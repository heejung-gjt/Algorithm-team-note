# -*- coding: utf-8 -*-
'''
date: 210809
description
  Q1. 1-n까지의 모든 자연수의 합
  Q2. n!
  Q3. fibonacci
'''

# Q1
def sum_number(num):
  print(num)
  if num <= 1:
    return num
  else:
    return num + sum_number(num - 1)
result = sum_number(10)


# Q2
def fac(num):
  if num <= 1:
    return num
  else:
    return num * fac(num - 1)
result = fac(10)


# Q3 fibonacci version
def fio(num):
  if num <= 1:
    return num
  else:
    return fio(num - 2) + fio(num - 1)



# 03-1 fibonacci version
def fio(num):
  if 0 < num <=2:
    return 1
  elif num == 0:
    return 0
  else:
    return fio(num - 2) + fio(num - 1)


# Q3-2 iterative version
def solution(num):
    result, a, b = 0, 0, 1
    if num == 1:
        return 1
    for _ in range(num - 1):
        result = a + b
        a = b
        b = result
    return result