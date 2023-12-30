#include <stdio.h>

int main(){

    int max_chain = 0;
    int number = 0;

    for (int i = 1; i < 1000000; i++){
        int chain = 1;
        long long int n = i;
        while (n != 1){
            if (n % 2 == 0){
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            chain++;
        }
        if (chain > max_chain){
            max_chain = chain;
            number = i;
        }
    }

    printf("The number with the longest chain is %d with %d terms.\n", number, max_chain);
    return 0;


}