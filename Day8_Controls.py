# If Else

# ******************************************* #

# Exercise :
print("****** Welcome to RollerCoaster! ******")
user_height = float(input("What is your height in cm?"))
user_age = int(input("What is your age?"))

if user_height >= 120.00:
    print("Sorry! can't ride! over height")
else:
    print("Yes, you can ride! nJoy!")
    if user_age < 12:
        print("You need to pay Rs 5")
    elif user_age <= 18:
        print("You need to pay Rs 7")
    else:
        print("You need to pay Rs 12")

# ******************************************* #

# Exercise : Check odd/even number

number = int(input("Enter a number:"))

if number % 2 == 0:
    print(f"Number {number} is Even")
else:
    print(f"Number {number} is Odd")

# Exercise to calculate BMI

print("****** Welcome to BMI Calculator *******")

user_height = input("Enter your height in meters:")
user_height = float(user_height)

user_weight = input("Enter your weight in Kgs:")
user_weight = float(user_weight)

user_bmi = user_weight/(user_height ** 2)
user_bmi = round(user_bmi, 2)

if user_bmi < 18.5:
    print(f"Your BMI : {user_bmi} - Underweight!!")
elif user_bmi <= 25.0:
    print(f"Your BMI : {user_bmi} - Normal")
elif user_bmi <= 30.0:
    print(f"Your BMI : {user_bmi} - Overweight!!")
elif user_bmi <= 35:
    print(f"Your BMI : {user_bmi} - Obese!!!")
else:
    print(f"Your BMI : {user_bmi} - Clinically Obese!!!!")

# ******************************************* #

# Exercise to calculate Leap Year

current_year = int(input("Enter the current year:"))

if current_year % 4 == 0:
    if current_year % 100 == 0:
        if current_year % 400 == 0:
            print(f"Year [{current_year}] is a Leap year")
        else:
            print(f"Year [{current_year}] is not Leap year")
    else:
        print(f"Year [{current_year}] is a Leap year")
else:
    print(f"Year [{current_year}] is not Leap year")

# ******************************************* #

# Exercise : Roller Coaster V2
print("****** Welcome to RollerCoaster! ******")
user_height = float(input("What is your height in cm?"))


if user_height > 120.00:
    print("Sorry! can't ride! over height")
else:
    print("Yes, you can ride! nJoy!")

    user_age = int(input("What is your age?"))
    bill = 0.00

    if user_age < 12:
        bill = 5.00
        print("You need to pay Rs 5")
    elif user_age <= 18:
        bill = 7.00
        print("You need to pay Rs 7")
    else:
        bill = 12.00
        print("You need to pay Rs 12")

    user_wants_photo = input("Do you want a photo taken? Y or N?")

    if user_wants_photo == "Y":
        bill = bill + 3.00

    print(f"Your final bill : Rs {bill}")

# ******************************************* #

# Exercise for Pizza Deliveries

print("***** WELCOME to PYTHON PIZZA Deliveries *****")

pizza_size = input("What size pizza do you want? (S / M / L)")

bill = 0.00
if pizza_size == "S":
    bill = 15.00
elif pizza_size == "M":
    bill = 20.00
elif pizza_size == "L":
    bill = 25.00

    add_pepperoni = input("Do you want pepperoni? (Y / N)")
    add_cheese = input("Do you want extra cheese? (Y / N)")

    # if pepperoni needed
    if add_pepperoni == "Y":
        if pizza_size == "S":
            bill += 2.00
        else:
            bill += 3.00

    # if cheese needed
    if add_cheese == "Y":
        bill = bill + 1.00
        print(f"Your final bill : Rs {bill}")
else:
    print("We don't have any size of Pizza you ordered!")

# ******************************************* #

# Exercise : Roller Coaster V3
print("****** Welcome to RollerCoaster! ******")
user_height = float(input("What is your height in cm?"))


if user_height > 120.00:
    print("Sorry! can't ride! over height")
else:
    print("Yes, you can ride! nJoy!")

    user_age = int(input("What is your age?"))
    bill = 0.00

    if user_age < 12:
        bill += 5.00
        print("You need to pay Rs 5")
    elif user_age <= 18:
        bill += 7.00
        print("You need to pay Rs 7")
    elif 45 <= user_age <= 55:
        print("Free Ride!")
        bill += 0.00
    else:
        bill += 12.00
        print("You need to pay Rs 12")

    user_wants_photo = input("Do you want a photo taken? Y or N?")

    if user_wants_photo == "Y" and user_age >= 45 or user_age <= 55:
        bill += 0.00
    else:
        bill += 3.00

    print(f"Your final bill : Rs {bill}")

# ******************************************* #

# Exercise : Love Calculator

print("****** Welcome to Love Calculator! ******")

boy_friend = input("Enter boy friend name:")
girl_friend = input("Enter girl friend name:")

# make the names in lower case
boy_friend = boy_friend.lower()
girl_friend = girl_friend.lower()

# Check (t,r,u,e) characters in both the names
count_t = 0
count_t += boy_friend.count("t")
count_t += girl_friend.count("t")

count_r = 0
count_r += boy_friend.count("r")
count_r += girl_friend.count("r")

count_u = 0
count_u += boy_friend.count("u")
count_u += girl_friend.count("u")

count_e = 0
count_e += boy_friend.count("e")
count_e += girl_friend.count("e")

count_true = count_t + count_r + count_u + count_e
# print("count_true :", count_true)

# Check (l,o,v,e) characters in both the names
count_l = 0
count_l += boy_friend.count("l")
count_l += girl_friend.count("l")

count_o = 0
count_o += boy_friend.count("o")
count_o += girl_friend.count("o")

count_v = 0
count_v += boy_friend.count("v")
count_v += girl_friend.count("v")

count_love = count_l + count_o + count_v + count_e
# print("count_love :", count_love)

true_love_percentage = int(str(count_true) + str(count_love))
# print("true_love_percentage :", true_love_percentage)

if (true_love_percentage < 10) or (true_love_percentage > 90):
    print(f"Your score : {true_love_percentage}, you go together like coke & mentos")
elif (true_love_percentage >= 40) and (true_love_percentage <= 50):
    print(f"Your score : {true_love_percentage} %, you are alright together")
else:
    print(f"Your score : {true_love_percentage} %, you two need adjustment")

# ******************************************* #
