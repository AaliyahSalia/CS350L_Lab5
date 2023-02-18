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


number_petri_dishes = int(input("Please enter total number of Petri dishes: "))

petri_dishes = []
for i in range(number_petri_dishes):
    label = input("Enter Petri dish label: ")
    original = input("Enter original bacterial number: ")
    new = input("Enter new bacterial number after one hour reproduction: ")
    petri_dishes.append((label, int(original), int(new)))

# calculate reproduction rates and sort the petri dishes by their rates
petri_dishes = sorted(petri_dishes, key=lambda x: x[2]/x[1])

# determine A and B sub-species
numA = 1
for i in range(1, len(petri_dishes)):
    if abs(petri_dishes[i][2]/petri_dishes[i][1] - petri_dishes[i-1][2]/petri_dishes[i-1][1]) > abs(petri_dishes[0][2]/petri_dishes[0][1] - petri_dishes[1][2]/petri_dishes[1][1]):
        numA = i
        break

# output results
print(f"{numA} in A sub-species and Petri dish labels from smaller PR to bigger PR are ", end="")
for i in range(numA):
    print(petri_dishes[i][0], end=" ")
print()
print(f"{len(petri_dishes) - numA} in B sub-species and Petri dish labels from smaller PR to bigger PR are ", end="")
for i in range(numA, len(petri_dishes)):
    print(petri_dishes[i][0], end=" ")
print()
