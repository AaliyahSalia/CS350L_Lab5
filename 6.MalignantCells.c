# Given a CT scanning image file saved as 2-dementional array, each element in array denotes one cell with different value from 0 to 255. Assuming that malignant cell’s value is less 50 than around 4 cells (up, down, left, right), and the cell on the matrix edge will NOT be detected, write a program to calculate and print number of malignant cells. 

#      Output
# Enter size of row & column: 4 4
# Enter each element: 
# 70 70 70 70
# 70 10 70 70
# 70 70 20 70
# 70 70 70 70

# Result of malignant cell detection: 2 

#include <stdio.h>

// function to check if a cell is malignant
int is_malignant(int image[][100], int row, int col, int rows, int cols) {
    // check that the cell is not on the edge of the image
    if (row == 0 || col == 0 || row == rows-1 || col == cols-1) {
        return 0;
    }
    // check the neighboring cells for malignancy
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if ((i == 0 || j == 0) && image[row+i][col+j] < image[row][col]-50) {
                return 1;
            }
        }
    }
    return 0;
}

int main() {
    int rows, cols;
    int image[100][100];

    // get the size of the image from the user
    printf("Enter size of row & column: ");
    scanf("%d %d", &rows, &cols);

    // get the image from the user
    printf("Enter each element:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &image[i][j]);
        }
    }

    // count the number of malignant cells
    int count = 0;
    for (int i = 1; i < rows-1; i++) {
        for (int j = 1; j < cols-1; j++) {
            if (is_malignant(image, i, j, rows, cols)) {
                count++;
            }
        }
    }

    // print the result
    printf("Result of malignant cell detection: %d\n", count);

    return 0;
}

