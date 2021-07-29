# 2018 KAKAO BLIND RECRUITMENT 압축
# 다른사람 풀이

def solution(msg) :
    dic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27))) # 이렇게 dictionary 만들 수 있다
    answer = []

    state = 1 # 1 : ok, 2 : add
    while (len(msg) > 0) :
        temp = -1
        for j in range(1, len(msg) + 1) :
            if list(dic.keys()).count(msg[0:j]) != 0 :
                temp = dic(msg[0:j])
                state = 1
            else :
                # add to dictionary
                dic[msg[0:j]] = len(dic)+1
                state = 2
                break
        answer += [temp]
        if state == 2 :
            msg = msg[j-1:]
        else :
            msg = ""
    return answer

print(solution("KAKAO") == [11, 1, 27, 15])
print(solution("TOBEORNOTTOBEORTOBEORNOT") == [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution("ABABABABABABABAB") == [1, 2, 27, 29, 28, 31, 30])