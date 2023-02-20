#There is a kind of bacterium with two sub-species A and B. They are very similar and difficult to differentiate, but the major difference between them is capability of reproduction. And reproduction in A is much stronger than that of B. Assuming that in a research center, researcher massed up Petri dishes with A and B bacterium, write a program to find which one is A, and which one is B in terms of each reproduction rate, given that reproduction rate is the ratio of new number of bacteria to original number after one hour (PR = new bacterial number / original bacterial numbers). Because of the huge different reproduction rate, it means that the difference of PR in any two Petri dishes belonging to the same sub-species is extremely smaller than that in any two Petri dishes belonging to the different sub-species. 

# 		Output
# 	Enter total number of Petri dishes: 5
# Enter Petri dish label, original bacterial number, new bacterial number after one hour reproduction: 

# 1	10 	3456
# 2 	10 	5644
# 3 	10 	4566
# 4 	20 	234
# 5 	20 	232


# 	Running results: 
# 	3 in A sub-species and Petri dish labels from smaller PR to bigger PR are 1 3 2
# 	2 in B sub-species and Petri dish labels from smaller PR to bigger PR are 5 4


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// define a new data type (petri_dish) that consists of three members (label, original, and new)
typedef struct {
    char label[100];
    int original;
    int new;
} petri_dish;

// function used by qsort to compare the reproduction rates of two petri dishes
int compare(const void *a, const void *b) {
    petri_dish *dishA = (petri_dish *)a;
    petri_dish *dishB = (petri_dish *)b;
    double rateA = (double)(dishA->new) / dishA->original;
    double rateB = (double)(dishB->new) / dishB->original;
    if (rateA < rateB) {
        return -1;
    } else if (rateA > rateB) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int number_petri_dishes;
    printf("Please enter total number of Petri dishes: ");
    scanf("%d", &number_petri_dishes);

    petri_dish petri_dishes[number_petri_dishes];
    for (int i = 0; i < number_petri_dishes; i++) {
        printf("Enter Petri dish label: ");
        scanf("%s", petri_dishes[i].label);
        printf("Enter original bacterial number: ");
        scanf("%d", &petri_dishes[i].original);
        printf("Enter new bacterial number after one hour reproduction: ");
        scanf("%d", &petri_dishes[i].new);
    }

    // sort the petri dishes by their reproduction rates
    qsort(petri_dishes, number_petri_dishes, sizeof(petri_dish), compare);

    // determine A and B sub-species
    int numA = 1;
    for (int i = 1; i < number_petri_dishes; i++) {
        if (abs((double)(petri_dishes[i].new) / petri_dishes[i].original - (double)(petri_dishes[i-1].new) / petri_dishes[i-1].original) > abs((double)(petri_dishes[0].new) / petri_dishes[0].original - (double)(petri_dishes[1].new) / petri_dishes[1].original)) {
            numA = i;
            break;
        }
    }

    // output results
    printf("%d in A sub-species and Petri dish labels from smaller PR to bigger PR are ", numA);
    for (int i = 0; i < numA; i++) {
        printf("%s ", petri_dishes[i].label);
    }
    printf("\n");
    printf("%d in B sub-species and Petri dish labels from smaller PR to bigger PR are ", number_petri_dishes - numA);
    for (int i = numA; i < number_petri_dishes; i++) {
        printf("%s ", petri_dishes[i].label);
    }
    printf("\n");

    return 0;
}
