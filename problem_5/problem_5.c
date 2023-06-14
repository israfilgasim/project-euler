#include <stdio.h>

/*
it is very easy we need only 2**4, 3**2, 5, 7, 11, 13, 17, 19
all powers of 2 is 2, 4, 8, 16 and 2 ** 4 evenly divsible by 2, 4, 8, 16
all powers of 3 is 3, 9 and 3 ** 2 evenly divsible by 3, 9
we have 3 and 2 these divisible by 6
5, 7, 11, 13, 17, 19 are prime numbers
*/

int main()
{
    int result = 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19;
    printf("%d\n", result);
    return 0;
}

// answer: 232792560