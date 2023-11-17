#include <stdio.h>
#include <time.h>

#define MAX_LENGTH 10000

void multiply(int result[], int *resultSize, int x) {
    int carry = 0;

    for (int i = 0; i < *resultSize; i++) {
        int product = result[i] * x + carry;
        result[i] = product % 10;
        carry = product / 10;
    }

    while (carry) {
        result[*resultSize] = carry % 10;
        carry /= 10;
        (*resultSize)++;
    }
}

void factorial(int n) {
    int result[MAX_LENGTH];
    int resultSize = 1;

    result[0] = 1;

    clock_t start = clock();

    for (int i = 2; i <= n; i++) {
        multiply(result, &resultSize, i);
    }

    clock_t end = clock();
    double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Factorial of %d is:\n", n);
    for (int i = resultSize - 1; i >= 0; i--) {
        printf("%d", result[i]);
    }
    printf("\n");

    printf("Time taken to calculate factorial: %f seconds\n", cpu_time_used);
}

int main() {
    int n;

    printf("Enter a non-negative integer: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        factorial(n);
    }

    return 0;
}
