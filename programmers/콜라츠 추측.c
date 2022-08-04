#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long long int num) {
    int answer = 0;

    for (; answer < 500; answer++) {
        if (num == 1)
            break;

        if (num % 2 == 0)
            num /= 2;
        else
            num = (num * 3) + 1;
    }

    if (num != 1)
        answer = -1;

    return answer;
}

void main(void) {
    printf("%d", solution(1));
}