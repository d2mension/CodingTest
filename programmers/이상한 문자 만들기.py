def solution(s):
    answer = ''
    cnt = 1
    
    for i in s:        
        if i == ' ':
            answer += ' '
            cnt = 1
            continue
        
        if cnt % 2 == 1:
            answer += i.upper()
        else:
            answer += i.lower()

        cnt += 1
        
    return answer
