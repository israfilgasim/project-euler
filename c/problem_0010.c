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

    long long int i = 3;
    long long sum = 2;

    while(i < 2000000){
        if(is_prime(i)){
            sum += i;
        }
        i += 2;
    }

    printf("%lld\n", sum);

}

// answer: 142913828922