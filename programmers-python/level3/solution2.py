# 위클리챌린지 3주차 - 퍼즐 조각 채우기

from collections import deque, defaultdict

# bfs 탐색 - 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 이어진 빈칸 or block 찾기
def bfs(board, x, y, check) :
    puzzle = []
    stack = deque([(x, y)])
    min_x, min_y = n, n

    while stack :
        now = stack.pop()
        puzzle.append(now)

        # block을 새로운 board에 그려주기 위해 min 좌표 찾기
        min_x, min_y = min(min_x, now[0]), min(min_y, now[1])
        
        board[now[0]][now[1]] = 2 # 탐색했음을 표시
        for i in range(4) :
            # 동서남북으로 탐색
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if(next_x < 0 or next_y < 0 or next_x >= n or next_y >= n) :
                continue
            elif(board[next_x][next_y] == check) :
                stack.append([next_x, next_y])
    return (board, puzzle, min_x, min_y)

# 새로운 정사각형 board에 좌표찍기
def make_new_board(b, x, y) :
    # 각 좌표에서 min_x, min_y 값 빼기
    new_position = [[i - x, j - y] for i, j in b]
    m = max(sum(new_position, [])) # x, y좌표 중 max값으로 정사각형 empty board생성
    new_board = [[0 for j in range(m + 1)] for i in range(m + 1)]
    for x, y in new_position :
        new_board[x][y] = 1
    return new_board

# 이어진 빈칸 or block 찾아서 새로운 board에 좌표찍기
def find_block(board, check) :
    d = defaultdict(list)
    for i in range(n) :
        for j in range(n) :
            if(board[i][j] == check) :
                # 이어진 빈칸 or block 찾기
                result = bfs(board, i, j, check)
                board = result[0]
                k = len(result[1])

                # 새로운 board에 좌표찍기
                new_board = make_new_board(result[1], result[2], result[3])

                # dict에 추가
                d[k].append(new_board)
    return d

def solution(game_board, table):
    answer = 0
    global n
    n = len(game_board)

    # game_board에서 이어진 빈칸 찾기
    game_board_d = find_block(game_board, 0)
    print(game_board_d)
                
    # table에서 이어진 블럭 찾기
    table_d = find_block(table, 0)
    print(table_d)

    # 빈칸에 블럭을 넣을 수 있는지 확인
    for k in table_d.keys() :
        puzzle = table_d[k]
        if(k not in game_board_d.keys()) :
            continue
        blank = game_board_d[k]
        for p in puzzle :
            for b in blank :
                if(isSame(p, b)) :
                    answer += k
                    blank.remove(b)
                    puzzle.remove(p)
                    break
                for i in range(3) :
                    p = rotate(p)
                    if(isSame(p, b)) :
                        answer += k
                        blank.remove(b)
                        puzzle.remove(p)
                        break
    return answer                   


# puzzle이 빈칸안에 들어갈 수 있는지
def isSame(a, b) :
    return 0
    # return set(a) == set(b)

# 시계방향으로 90도 회전
def rotate(board) :
    n = len(board)
    rot = [[0] * n for _ in range(n)]

    for r in range(n) :
        for c in range(n) :
            rot[c][n - 1 - r] = board[r][c]
    
    # rot = [[i - x, j - y] for i, j in rot]
    return rot

board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
# print(solution(board, table))
print(rotate([[0, 1, 0], [1, 1, 1], [0, 0, 0]]))