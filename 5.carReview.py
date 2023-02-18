#There are 4 types of racing sport cars with number from 1 to 4. And 4 car-design experts will review them and give 4 answers as follows. 

# a.	expert A said:  #2 is the best.
# b.	expert B said:  #4 is the best.
# c.	expert C said:  #3 is NOT the best.
# d.	expert D said:  expert B is wrong.

# Actually, only car is the best, and one & only one expert review is correct, the others are wrong. Write a program to calculate and print on the monitor which car is the best and which expert review is correct.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

# create a linked list to store the expert reviews
expert_reviews = LinkedList()
expert_reviews.insert("Expert D said: expert B is wrong.")
expert_reviews.insert("Expert C said: #3 is NOT the best.")
expert_reviews.insert("Expert B said: #4 is the best.")
expert_reviews.insert("Expert A said: #2 is the best.")

# create a dictionary to map car numbers to their rankings
car_rankings = {1: 0, 2: 0, 3: 0, 4: 0}

# iterate through the expert reviews and update the car rankings accordingly
curr_node = expert_reviews.head
while curr_node:
    review = curr_node.data
    if "Expert A said: #2 is the best." in review:
        car_rankings[2] += 1
    elif "Expert B said: #4 is the best." in review:
        car_rankings[4] += 1
    elif "Expert C said: #3 is NOT the best." in review:
        car_rankings[1] += 1
        car_rankings[2] += 1
        car_rankings[4] += 1
    elif "Expert D said: expert B is wrong." in review:
        car_rankings[1] += 1
        car_rankings[2] += 1
        car_rankings[3] += 1
    curr_node = curr_node.next

# find the car with the highest ranking
best_car = max(car_rankings, key=car_rankings.get)

# find the expert who gave the correct review
correct_expert = ""
if expert_reviews.head.data == "Expert A said: #2 is the best." and best_car == 2:
    correct_expert = "Expert A"
elif expert_reviews.head.data == "Expert B said: #4 is the best." and best_car == 4:
    correct_expert = "Expert B"
elif expert_reviews.head.data == "Expert C said: #3 is NOT the best." and best_car != 3:
    correct_expert = "Expert C"
elif expert_reviews.head.data == "Expert D said: expert B is wrong." and best_car != 4:
    correct_expert = "Expert D"

# print the results
print("The best car is #{}.".format(best_car))
print("The correct expert review is from {}.".format(correct_expert))
