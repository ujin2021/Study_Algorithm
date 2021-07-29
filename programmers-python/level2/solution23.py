# 짝지어 제거하기

# substring 자체가 메모리를 할당해야 하기때문에 시간 초과 난다
# 스택으로 푸는게 효율적이다 - 참고 로직: https://programmers.co.kr/questions/19076

from collections import deque

def solution(s):
    if(len(s) % 2 == 1) :
        return 0
    l = len(s)
    q = deque([0])
    i = 1
    while True :
        if(q and s[i] == s[q[0]]) :
            q.popleft()
        else :
            q.appendleft(i)
        i += 1
        if(i == l) :
            if(len(q) == 0) :
                return 1
            return 0

print(solution("baabaa") == 1)
print(solution("cdcd") == 0)
print(solution("abccba") == 1)
print(solution("abcccba") == 0)
print(solution("abccccbaaa") == 1)
print(solution("abccaabaa") == 0)
print(solution("a") == 0)