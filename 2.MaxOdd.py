# Find the absolute value of maximum odd number minus minimum even number from standard input device by a program.

# 		Output
# 	Enter a series of integer numbers: 1 2 3 4 5 6

# 	Result is:	3			// |5 - 2| =3

# 	Enter a series of integer numbers: 1 6 3 8 5 10

# 	Result is:	1			// |5 – 6| =1



int_list = []

while True:
	try:
		int_list.append(int(input("Please enter a series of integer numbers: ")))
	except:
		break

print(int_list)

odd_list = [x for x in int_list if x % 2 == 1]
even_list = [x for x in int_list if x % 2 == 0]

max_odd = max(odd_list) if odd_list else None
min_even = min(even_list) if even_list else None

print(f"Max odd number is {max_odd}")
print(f"Min even number is {min_even}")


if max_odd  is not None and min_even is not None:
	result = abs(max_odd - min_even)
else:
	result = None

print("The result is: ", result)

