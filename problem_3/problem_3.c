#include <stdio.h>
#include <math.h> // for sqrt function

int greatestPrimeFactor(long long int number) // we use long long int because the number is too big for int
{
    int array[1000];

    if (number % 2 == 0)
    {
        array[0] = 2;
        while (number % 2 == 0)
        {
            number /= 2;
        }
    }

    long int i = 3;
    int index = 1;

    long long int sqrtNumber = (int)sqrt(number);
    // sqrt function returns double, so we cast it to int

    while (i <= sqrtNumber)
    {
        if (number % i == 0)
        {
            array[index] = i;
            index++;
            while (number % i == 0)
            {
                number /= i;
            }
        }
        i += 2;
    }

    int max = 0;

    for (int j = 0; j < index; j++)
    {
        if (array[j] > max)
        {
            max = array[j];
        }
    }

    return max;

}

// now, we can test our function

int main()
{
    printf("%d\n", greatestPrimeFactor(600851475143));
    return 0;
}

// answer: 6857