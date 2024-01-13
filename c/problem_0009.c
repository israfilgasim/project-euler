#include <stdio.h>

int main(){

    int a = 1;
    int b = 2;
    int c = 997;

    while (a < c-1){
        b = a + 1;
        while (b < c){
            c = 1000 - a - b;
            if (a*a + b*b == c*c){
                printf("a = %d, b=%d, c=%d %d\n",a,b,c, a*b*c);
                return 0;
            }
            b++;
        }
        a++;
    }
    return 0;

}

// a = 200, b=375, c=425 31875000