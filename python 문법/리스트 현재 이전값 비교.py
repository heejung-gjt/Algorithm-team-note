# level2 - 문자열 압축하기 문제에서

def solution(s):
    for size in range(1, len(s)): # s의 문자열을 1 ~ 7개씩 잘라서 배열에 담기
        splited = []
        cnt = 1
        for i in range(0, len(s), size):
            splited.append(s[i:i + size])
        print(splited)  
        '''
        ['a', 'b', 'b', 'b', 'c', 'd', 'd', 'e']
        ['ab', 'bb', 'cd', 'de']
        ['abb', 'bcd', 'de']
        ['abbb', 'cdde']
        ['abbbc', 'dde']
        ['abbbcd', 'de']
        ['abbbcdd', 'e']
        '''

        for j in range(1, len(splited)):
            prev, curr = splited[j - 1], splited[j] # a vs b 비교...
            if prev == curr:
                cnt += 1
            else:
                print(f'{prev}의 값 연속해서 {cnt}개 같음') # 마지막 값만 결과값이 나올 수 없음
                cnt = 1
        print(f'{splited[-1]}의 값 연속해서 {cnt}개 같음') # 마지막 값은 for문이 끝난 후 출력할 수 있음

        '''
        a의 값 연속해서 1개 같음
        b의 값 연속해서 3개 같음
        c의 값 연속해서 1개 같음
        d의 값 연속해서 2개 같음
        e의 값 연속해서 1개 같음
        ['ab', 'bb', 'cd', 'de']
        ab의 값 연속해서 1개 같음
        bb의 값 연속해서 1개 같음
        cd의 값 연속해서 1개 같음
        de의 값 연속해서 1개 같음
        ['abb', 'bcd', 'de']
        abb의 값 연속해서 1개 같음
        bcd의 값 연속해서 1개 같음
        de의 값 연속해서 1개 같음
        ['abbb', 'cdde']
        abbb의 값 연속해서 1개 같음
        cdde의 값 연속해서 1개 같음
        ['abbbc', 'dde']
        abbbc의 값 연속해서 1개 같음
        dde의 값 연속해서 1개 같음
        ['abbbcd', 'de']
        abbbcd의 값 연속해서 1개 같음
        de의 값 연속해서 1개 같음
        ['abbbcdd', 'e']
        abbbcdd의 값 연속해서 1개 같음
        e의 값 연속해서 1개 같음
        '''

solution("abbbcdde")