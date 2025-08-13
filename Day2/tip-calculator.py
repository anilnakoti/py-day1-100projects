# user greet message
print("Welcome to the tip calculator!")

# total bill input from the user
total_bill = input("What was the total bill?\n")

# add tip 10, 12, or 15
tip = input("How much tip would you like to give?\n")

# split the bill among people
number_of_split = input("How many people to split?\n")

# calculate the amount that each member should pay
each_person_should_pay = (int(total_bill) + int(tip)) / int(number_of_split)

print(f"Each person should pay: {round(each_person_should_pay, 2)}")
