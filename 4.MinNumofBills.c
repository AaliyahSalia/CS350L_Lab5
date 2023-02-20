# Write a program to calculate minimum number of bills for a given payment assuming existing bills, such as $100, $50, $20, $10, $5 and $1

# 	Output
# 	Enter total payment: 735

# 	Result of minimum number of bills: 10 
# 	$100 bill: 	7
# 	$50 bill: 	0
# $20 bill: 	1
# $10 bill: 	1
# $5 bill: 	1
# $1 bill: 	0


#include <stdio.h>

void calculate_bills(int payment, int* num_bills) {
    int bills[] = {100, 50, 20, 10, 5, 1};
    int num_bills_len = sizeof(bills)/sizeof(bills[0]);

    for (int i = 0; i < num_bills_len; i++) {
        num_bills[i] = payment / bills[i];
        payment = payment % bills[i];
    }
}

int main() {
    int payment, num_bills[6];
    printf("Please enter the payment amount: ");
    scanf("%d", &payment);

    calculate_bills(payment, num_bills);

    printf("The number of bills are: ");
    for (int i = 0; i < 6; i++) {
        printf("%d ", num_bills[i]);
    }
    printf("\n");

    int total_bills = 0;
    for (int i = 0; i < 6; i++) {
        total_bills += num_bills[i];
    }

    printf("The total number of bills are: %d\n", total_bills);
    printf("$100 bill: %d\n", num_bills[0]);
    printf("$50 bill: %d\n", num_bills[1]);
    printf("$20 bill: %d\n", num_bills[2]);
    printf("$10 bill: %d\n", num_bills[3]);
    printf("$5 bill: %d\n", num_bills[4]);
    printf("$1 bill: %d\n", num_bills[5]);

    return 0;
}
