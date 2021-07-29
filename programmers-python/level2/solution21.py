# 2018 KAKAO BLIND RECRUITMENT 압축

def solution(msg) :
    d = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    answer = []
    l = len(msg)
    now_i = new_i = 0
    while True :
        now = new = msg[now_i]
        for new_i in range(now_i + 1, l) :
            new += msg[new_i]
            if(new not in d) :
                d.append(new)
                now_i = new_i
                answer.append(d.index(now))
                break
            else :
                now = new

        # 마지막 처리 (마지막이 사전에 있는 단어에 포함되는가 / 아닌가)
        if(new_i ==  l - 1) :
            if(new == d[-1]) :
                answer.append(d.index(msg[-1]))
                break
            else :
                answer.append(d.index(now))
                break
            
    # print(answer)
    return answer

print(solution("KAKAO") == [11, 1, 27, 15])
print(solution("TOBEORNOTTOBEORTOBEORNOT") == [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution("ABABABABABABABAB") == [1, 2, 27, 29, 28, 31, 30])