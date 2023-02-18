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


# structure for a node in circular linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
 
def monkeyKing(n, m):
    head = Node(0)
    prev = head
    for i in range(1, n):
        prev.next = Node(i)
        prev = prev.next
    prev.next = head 
 
    ptr1 = head
    ptr2 = head.next
    while (ptr2.next != ptr2):
        count = 1
        while (count != m):
            ptr1 = ptr2
            ptr2 = ptr2.next
            count += 1
 
        ptr1.next = ptr2.next
        ptr2 = ptr1.next
    return ptr2.data
  
n = int(input("Please enter the total number of monkeys in the group: "))
m = int(input("Please enter the 'm' value: "))
print("The king will be: ", monkeyKing(n, m)) 