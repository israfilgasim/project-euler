#include <stdio.h>

int main(){
    int sum_of_squares = 0;
    int square_of_sum = 0;
    int difference;

    for(int i = 1; i <= 100; i++){
        sum_of_squares += i * i;
        square_of_sum += i;
    }

    square_of_sum *= square_of_sum;
    difference = square_of_sum - sum_of_squares;

    printf("%d\n", difference);
    return 0;

}

// answer: 25164150