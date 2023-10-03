#include <stdio.h>

// in python file, we found that the upper bound is 1000000

int main(){

    int sum_of_numbers = 0;

    for (int i = 2; i < 1000000; i++){

        int sum = 0;
        int number = i; // we need to keep the original number

        while (number > 0){
            int digit = number % 10;
            sum += digit * digit * digit * digit * digit;
            number /= 10;
        }

        if (sum == i){
            sum_of_numbers += i;
        }
    }

    printf("%d\n", sum_of_numbers);
    return 0;

}

//answer: 443839