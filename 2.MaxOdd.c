# Find the absolute value of maximum odd number minus minimum even number from standard input device by a program.

# 		Output
# 	Enter a series of integer numbers: 1 2 3 4 5 6

# 	Result is:	3			// |5 - 2| =3

# 	Enter a series of integer numbers: 1 6 3 8 5 10

# 	Result is:	1			// |5 – 6| =1



#include <stdio.h>
#include <stdlib.h>

int main() {
    int int_list[1000];
    int count = 0;

    while (1) {
        int input_num;
        printf("Please enter a series of integer numbers: ");
        int result = scanf("%d", &input_num);
        if (result == 1) {
            int_list[count] = input_num;
            count++;
        } else {
            break;
        }
    }

    printf("[");

    for (int i = 0; i < count; i++) {
        printf("%d", int_list[i]);
        if (i != count - 1) {
            printf(", ");
        }
    }

    printf("]\n");

    int odd_list[1000];
    int even_list[1000];
    int odd_count = 0;
    int even_count = 0;

    for (int i = 0; i < count; i++) {
        if (int_list[i] % 2 == 1) {
            odd_list[odd_count] = int_list[i];
            odd_count++;
        } else {
            even_list[even_count] = int_list[i];
            even_count++;
        }
    }

    int max_odd = -1000000;
    int min_even = 1000000;

    for (int i = 0; i < odd_count; i++) {
        if (odd_list[i] > max_odd) {
            max_odd = odd_list[i];
        }
    }

    for (int i = 0; i < even_count; i++) {
        if (even_list[i] < min_even) {
            min_even = even_list[i];
        }
    }

    if (max_odd != -1000000 && min_even != 1000000) {
        int result = abs(max_odd - min_even);
        printf("Max odd number is %d\n", max_odd);
        printf("Min even number is %d\n", min_even);
        printf("The result is: %d\n", result);
    } else {
        printf("Max odd number is None\n");
        printf("Min even number is None\n");
        printf("The result is: None\n");
    }

    return 0;
}

