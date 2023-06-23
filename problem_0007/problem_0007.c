#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(int n){
    bool status = true;
    int a = sqrt(n) + 1;
    for(int i = 3; i < a; i+=2){
        if(n % i == 0){
            status = false;
            break;
        }
    }
    return status;

}

int main (){

    int count = 1;
    int i = 3;
    int number = 0;

    while(count <= 10000){
        if(is_prime(i)){
            count++;
            number = i;
        }
        i+=2;
    }

    printf("%d\n", number);

}

// answer: 104743