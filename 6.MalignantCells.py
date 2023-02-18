# Given a CT scanning image file saved as 2-dementional array, each element in array denotes one cell with different value from 0 to 255. Assuming that malignant cell’s value is less 50 than around 4 cells (up, down, left, right), and the cell on the matrix edge will NOT be detected, write a program to calculate and print number of malignant cells. 

#      Output
# Enter size of row & column: 4 4
# Enter each element: 
# 70 70 70 70
# 70 10 70 70
# 70 70 20 70
# 70 70 70 70

# Result of malignant cell detection: 2 


# function to check if a cell is malignant
def is_malignant(image, row, col):
    # check that the cell is not on the edge of the image
    if row == 0 or col == 0 or row == len(image)-1 or col == len(image[0])-1:
        return False
    # check the neighboring cells for malignancy
    for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if image[row+i][col+j] < image[row][col]-50:
            return True
    return False

# get the size of the image from the user
rows, cols = map(int, input("Enter size of row & column: ").split())

# get the image from the user
image = []
print("Enter each element:")
for i in range(rows):
    row = list(map(int, input().split()))
    image.append(row)

# count the number of malignant cells
count = 0
for i in range(1, rows-1):
    for j in range(1, cols-1):
        if is_malignant(image, i, j):
            count += 1

# print the result
print("Result of malignant cell detection:", count)
