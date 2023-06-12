#include <stdio.h>

int main(void)
{
    int first = 1;
    int second = 1;
    int sum = 0;
    int next;

    while (second < 4000000){
        next = first + second;
        first = second;
        second = next;
        if (second % 2 == 0){
            sum += next;
        }
    }

    printf("%i\n", sum);
    return 0;
}

// answer: 4613732