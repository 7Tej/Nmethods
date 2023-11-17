#include <stdio.h>

// Define a maximum length for the result array
#define MAX_LENGTH 10000

// Function to multiply two numbers represented as arrays
void multiply(int result[], int *resultSize, int x) {
    int carry = 0;

    // Multiply each digit of result by x
    for (int i = 0; i < *resultSize; i++) {
        int product = result[i] * x + carry;
        result[i] = product % 10; // Store the last digit
        carry = product / 10;     // Carry to the next iteration
    }

    // Multiply any remaining carry
    while (carry) {
        result[*resultSize] = carry % 10;
        carry /= 10;
        (*resultSize)++;
    }
}

// Function to calculate the factorial of a given number
void factorial(int n) {
    int result[MAX_LENGTH];
    int resultSize = 1;

    // Initialize the result with 1
    result[0] = 1;

    // Calculate factorial
    for (int i = 2; i <= n; i++) {
        multiply(result, &resultSize, i);
    }

    // Print the result in reverse order
    printf("Factorial of %d is:\n", n);
    for (int i = resultSize - 1; i >= 0; i--) {
        printf("%d", result[i]);
    }
    printf("\n");
}

int main() {
    int n;

    // Get user input for the number
    printf("Enter a non-negative integer: ");
    scanf("%d", &n);

    // Check if the input is valid
    if (n < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        // Calculate and print the factorial
        factorial(n);
    }

    return 0;
}
