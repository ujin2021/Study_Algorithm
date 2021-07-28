# 2021 KAKAO BLIND RECRUITMENT - 순위 검색

from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []
    db = defaultdict(list)
    for i in range(len(info)) :
        i = info[i].split()
        i_v = int(i[-1])
        i_k = i[:-1]
        for j in range(5) :
            for c in combinations(i_k, j) :
                db[''.join(c)].append(i_v)
    
    # print(db)

    # query 갯수 보다 info 갯수가 적기 때문에 여기서 for문으로 sort 해주는 것이 효율성이 더 높다
    for k in db.keys() :
        db[k] = sorted(db[k])

    for q in query :
        q = q.replace(' and ', '').split()
        q_v = int(q[1])
        q_k = q[0].replace('-', '')
        # score = sorted(db[q_k]) 여기서 sort 하면 안됨 (효율성 통과 x)
        score = db[q_k]
        
        if(len(score) == 0) :
            answer.append(0)
            continue

        # 효율성 통과를 위해 이진탐색 해야함
        start, end = 0, len(score)
        while end > start :
            mid = (start + end) // 2
            if (score[mid] >= q_v) :
                end = mid
            else :
                start = mid + 1       
            
        answer.append(len(score) - start)
        # print(answer)
    return answer

    

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query) == [1,1,1,1,2,4])