"""
문자열은 인덱스로 값 문자에 접근이 가능하다
인덱스값 i를 비교해 word[i]에 존재하는 문자열의 상태를 변경할 수 있다
word[i]의 문자열 상태는 변경 될 수 있지만 실제로 word에 담겨있는 문자열이 바뀌지는 않는다
"""

def solution(s):
    answer = ''
    s = s.split(' ')
    for word in s:
        for i in range(len(word)):
            result = word[i].upper() if i % 2 == 0 else word[i].lower() 
            print(word[i], '->', result)
        print()
                      
    return answer

s = "try hello world"
solution(s)

"""
t -> T
r -> r
y -> Y

h -> H
e -> e
l -> L
l -> l
o -> O

w -> W
o -> o
r -> R
l -> l
d -> D
"""