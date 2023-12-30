#include <stdio.h>
#include <stdbool.h>

bool isArriveOne(long long int n) {
    long long int sum = 0;
    while (n > 0) {
        sum += (n % 10) * (n % 10);
        n /= 10;
    }

    if (sum == 1) {
        return true;
    } else if (sum == 89) {
        return false;
    } else {
        return isArriveOne(sum);
    }
}

int main() {
    int count = 0; // unlike python, in c we use int instead of array to count
    for (int i = 1; i < 10000000; i++) {
        if (isArriveOne(i) == false) {
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}

// answer: 8581146