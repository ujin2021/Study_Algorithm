# 위클리 챌린지 - 2주차

def level(num) :
    if(num >= 90) :
        return 'A'
    elif(num >= 80) :
        return 'B'
    elif(num >= 70) :
        return 'C'
    elif(num >= 50) :
        return 'D'
    else :
        return 'F'

def solution(scores):
    scores = list(map(list, zip(*scores)))
    answer = ''
    l = len(scores)
    for i in range(l) :
        s = scores[i]
        a, b = max(s), min(s)
        if((s.count(a) == 1 and s.index(a) == i) or (s.count(b) == 1 and s.index(b) == i)) : # 가장 max/min이고 자기가 평가한거면 제외
            del s[i]
            avg = sum(s) / (l - 1)
        else :
            avg = sum(s) / l
        answer += level(avg)
        
    return answer

# print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]) == "FBABD")
# print(solution([[50,90],[50,87]]) == "DA")
# print(solution([[70,49,90],[68,50,38],[73,31,100]]) == "CFD")

a = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# print(list(zip(*a)))
print(*a) # [100, 90, 98, 88, 65] [50, 45, 99, 85, 77] [47, 88, 95, 80, 67] [61, 57, 100, 80, 65] [24, 90, 94, 75, 65]
# 각 list의 요소를 개별 요소로 보고 zip 하면 => 같은 인덱스 끼리 묶인다