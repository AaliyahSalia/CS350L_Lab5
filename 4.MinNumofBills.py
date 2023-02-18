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


def calculate_bills(payment):
    bills = [100, 50, 20, 10, 5, 1]
    num_bills = [0] * len(bills)
    for i, bill in enumerate(bills):
        num_bills[i] = payment // bill
        payment = payment % bill
    return num_bills

def main():
    payment = int(input("Please enter the payment amount: "))
    num_bills = calculate_bills(payment)
    print("The number of bills are: ", num_bills)
    total_bills = sum(num_bills)
    print("The total number of bills are: ", total_bills)
    print("$100 bill: ", num_bills[0])
    print("$50 bill: ", num_bills[1])
    print("$20 bill: ", num_bills[2])
    print("$10 bill: ", num_bills[3])
    print("$5 bill: ", num_bills[4])
    print("$1 bill: ", num_bills[5])

print(main())