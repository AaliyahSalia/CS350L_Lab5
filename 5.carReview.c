#There are 4 types of racing sport cars with number from 1 to 4. And 4 car-design experts will review them and give 4 answers as follows. 

# a.	expert A said:  #2 is the best.
# b.	expert B said:  #4 is the best.
# c.	expert C said:  #3 is NOT the best.
# d.	expert D said:  expert B is wrong.

# Actually, only car is the best, and one & only one expert review is correct, the others are wrong. Write a program to calculate and print on the monitor which car is the best and which expert review is correct.


#include <stdio.h>

int main() {
    int correctExpert;
    int bestCar;

    // Check each car-design expert's statement and find the correct expert and best car
    if (2 == 4 && 4 != 3 && 4 != 2) {
        correctExpert = 1;
        bestCar = 2;
    }
    else if (4 == 4 && 4 != 3 && 4 != 2) {
        correctExpert = 2;
        bestCar = 4;
    }
    else if (3 != 4 && 3 == 3 && 3 != 2) {
        correctExpert = 3;
        bestCar = 1;
    }
    else if (2 != 4 && 4 != 3 && 4 == 2) {
        correctExpert = 4;
        bestCar = 3;
    }

    // Print the results
    printf("The best car is car number %d.\n", bestCar);
    printf("The correct expert is expert %c.\n", 'A' + correctExpert - 1);

    return 0;
}

