# JadenCase 문자열 만들기

def solution(s):
    s = s.lower()
    l = len(s)
    for i in range(l - 1) :
        # print('i : ', i)
        if(i == 0 and s[i] != ' ') :
            s = s[:i] + s[i].upper() + s[i + 1:]
        elif(s[i] == ' ' and s[i + 1] != ' ') :
            s = s[:i + 1] + s[i + 1].upper() + s[i + 2:]
            # print('new s : ', s)
    return s

print(solution(" my  wOrld  ") == " My  World  ") # l = 12
print(solution("3people unFollowed me") == "3people Unfollowed Me")
print(solution("3people   unFollowed me") == "3people   Unfollowed Me")
print(solution("  3people   unFollowed me") == "  3people   Unfollowed Me")
print(solution("  3people   unFollowed me ") == "  3people   Unfollowed Me ")
print(solution("for the last week") == "For The Last Week")