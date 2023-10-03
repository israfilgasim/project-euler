#include <stdio.h>

// in c, we have try a different approach to the problem
// unlike python, we don't use array to store the value

int main(void){

    int max  = 9009; // 91 * 99

    for(int i = 100; i < 1000; i++){
        for(int j = 100; j < 1000; j++){
            int sum = i * j;
            int reverse_sum = 0; // we use this variable to store the reverse value of sum
            int temp = sum; // we use temporary variable to store the value of sum to avoid changing the value of sum

            while(temp != 0){
                reverse_sum = reverse_sum * 10; 
                // we multiply the value of reverse_sum by 10, 
                //because we want to add the value of temp % 10 to the end of reverse_sum
                reverse_sum = reverse_sum + temp % 10;
                temp = temp / 10;
            }

            if(sum == reverse_sum){
                if(sum > max){
                    max = reverse_sum;
                }
            }
        }
    }

    printf("%d\n", max);
    return 0;

}

// answer: 906609