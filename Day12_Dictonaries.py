
# Imports
from replit import clear


dict_1 = {
    "Pushparghya": "9836014180",
    "Suparna": "8335047722",
    "Baba": "900785248",
    }

print(dict_1["Pushparghya"])

# Adding item
dict_1["Supu"] = "wifey"
dict_1["Maa"] = 900785625
print(dict_1)
print(type(dict_1["Maa"]))

# creating an empty dictionary
empty_dict = {}

# clear any dictionary
dict_2 = {
    "Pushparghya": "9836014180",
    "Suparna": "8335047722",
    "Baba": "900785248",
}

dict_2 = {}
print(dict_2)

# Edit the value of a key
dict_1["Supu"] = "babai"
print(dict_1)

# Loop through the dictionary, it by default returns the keys only
for dict_key in dict_1:
    print(f"Key :{dict_key}")
    print(f"Value :{dict_1[dict_key]}")

"""

# Exercise:1
student_scores = {
    "Ram": 81,
    "Sham": 78,
    "Tom": 99,
    "Dick": 74,
    "Harry": 62
}

student_grades = {}

for student in student_scores:
    # get the marks
    student_marks = student_scores[student]
    # evaluate the grade
    final_student_grade = ""
    if student_marks > 90:
        final_student_grade = "Outstanding"
    elif student_marks > 80:
        final_student_grade = "Exceeds Expectation"
    elif student_marks > 70:
        final_student_grade = "Acceptable"
    else:
        final_student_grade = "Fail"
    # update the student_grades dictionary
    student_grades[student] = final_student_grade

# print(f"Student Grades :{student_grades}")

# Exercise:2 (Nested dictionaries)
travel_log = [
    {
      "country": "France",
      "visits": 12,
      "cities": ["Paris", "Lille", "Dijon"]
    },
    {
      "country": "Germany",
      "visits": 5,
      "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# adding 3rd country travel log to the above list
# get input from the user
country = input("Country visited? :")
visits = int(input("Number of visits made? :"))
cities = input("Provide cities name separated by space? :")


def update_travel_log(country_visited, num_visits, cities_went):
    country_dict = {}
    country_dict["country"] = country_visited
    country_dict["visits"] = num_visits
    country_dict["cities"] = cities_went.split(" ")

    travel_log.insert(len(travel_log), country_dict)


update_travel_log(country, visits, cities)

print(travel_log)

"""

# Exercise :3 (Silent Bidder)
print("**** Welcome to Silent Bidder ****")

# method that will derive the highest bidder
dict_bid_records = {}


def add_bidder(bidder_name, bid_value):
    dict_bid_records[bid_value] = bidder_name


def get_final_bidder():
    if len(dict_bid_records) == 1:
        print("Only 1 bidder, need more bidders! Bye")
    else:
        list_bid_amounts = []
        for bid_val in dict_bid_records:
            list_bid_amounts.append(bid_val)

        # get max value from the list
        max_bid = max(list_bid_amounts)

        # get the max bidder name by key
        max_bidder = dict_bid_records[max_bid]

        # final print
        print(f"Highest Bidder :[{max_bidder}] with bid value [Rs:{max_bid}]")


should_continue = True
while should_continue:
    bidder = input("What's your name? :")
    bid_amount = int(input("What's your bid? Rs:"))
    add_bidder(bidder, bid_amount)
    yes_no = input("Any other bidder? Type 'yes' or 'no':").lower()
    if yes_no == "no":
        should_continue = False
        get_final_bidder()
    else:
        clear()






