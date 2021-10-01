# -*- coding: utf-8 -*-

"""
유클리드 호제법
c와 d에 대해서 (c < d) t = c % d일때, t = 0이 될때까지 d % t = k, r % k 를 했을때 k가 최대 공약수
"""

# 최대 공약수
def gcd(a, b):
  c, d = max(a, b), min(a, b)
  t = 1

  while t > 0:
    t = c % d
    c, d = d, t

  answer = c
  print(answer)

gcd(4, 8) # 4

  # 최소 공배수
"""
(a * b) / 최대공약수
"""

print(('a' * 'b') /'최대공약수')