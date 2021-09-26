# n진수 -> 10진수
def exchange(n, num):
  return int(n, num )

exchange(46, 3) # 3진수 -> 10진수


# 10진수 -> 2, 8, 16진수
print(bin(11)) # 2진수
print(oct(11)) # 8진수
print(hex(11)) # 16진수


# 10진수 -> n진수 - 1
def exchange(n, num):
  tmp = ''

  while n:
    tmp += str(n % num)
    n //= num
  return tmp[::-1]

# 10진수 -> n진수 - 2
def exchange(n, num):
  tmp = ''

  while n:
    n, mod = divmod(n, num)
    tmp += str(mod)

  return tmp[::-1]


# n진수 -> n진수
print(exchange(int('45', 3), 7)) # 3진수인 45를 7진수로 변환, exchange함수 활용