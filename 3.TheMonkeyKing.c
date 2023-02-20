# A group of monkeys want to elect a king based on the following rules. 

# 	a. everyone is sitting in a circle and get number in clockwise direction from 0 to n-1
# b. with a given number m that is set up before, count each one in clockwise direction     from 1 to m, and then m^th monkey will be out from the competition.
# c. after that, re-assign number right after m^th monkey for each from 0 to n-2
# 	d. repeat above step b and c until the last one is left. And it will be the king. 
# 	e. the program running result should be king’s number in step a

# 	 Output
# 		Enter total number of monkeys in a group: 5
# 		Enter m value: 3
# 		The king will be 3

# 		Enter total number of monkeys in a group: 8
# 		Enter m value: 5
# 		The king will be 2


#include <stdio.h>

int findKing(int n, int m) {
    int monkeys[n];
    for (int i = 0; i < n; i++) {
        monkeys[i] = i;
    }

    int eliminated = -1;
    while (n > 1) {
        eliminated = (eliminated + m) % n;
        for (int i = eliminated; i < n - 1; i++) {
            monkeys[i] = monkeys[i + 1];
        }
        n--;
    }

    return monkeys[0];
}

int main() {
    int n, m;
    printf("Enter total number of monkeys in a group: ");
    scanf("%d", &n);
    printf("Enter m value: ");
    scanf("%d", &m);
    int king = findKing(n, m);
    printf("The king will be: %d\n", king);
    return 0;
}
