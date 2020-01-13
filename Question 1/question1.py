def calculate_age():
	name = input("Enter your name :")
	age = input("Enter your age :")
	Y = 2016
	# Current_year = Y

	for x in range(49,100,7):
		Y+=7
		print ( name + "," + " in " + str(Y) + " "+ "your age is " + str(x))


