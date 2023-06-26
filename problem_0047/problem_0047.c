#include <stdio.h>

int main(){

    int count = 0;

    int i, j;

    for (i = 1; i<1000000; i++){
        int temp = i;
        int divs = 0;

        if (temp % 2 == 0){
            divs++;
            while (temp % 2 == 0){
                temp /= 2;
            }
        }

        for (j = 3; j<1000; j+=2){
            if (temp % j == 0){
                divs++;
                while (temp % j == 0){
                    temp /= j;
                }
            }
        }

        if (divs == 4){
            count++;
        }
        else{
            count = 0;
        }

        if (count == 4){
            printf("%d\n", i-3);
            break;
        }
    }

    return 0;

}

// answer: 134043