def solution(n):
    answer = 0
    trit = ''
    num = 0

    while n > 0:
        trit += str(n % 3)
        n //= 3

    length = len(trit)-1
    trit = int(trit)
    
    for i in range(length, -1, -1):
        digit_10 = 10 ** i
        num = trit // digit_10
        trit %= digit_10
        
        answer += (num * (3 ** i))
    
    return answer
