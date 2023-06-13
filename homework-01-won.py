# Krystal Cheongeui Won
# June 6, 2023
# Homework 1


import datetime


# let the user input their birth year
birth_year = int(input("Please enter your birth year: "))
while birth_year > datetime.datetime.now().year:
    print("You can't be born in the future! Please try again.")
    birth_year = int(input("Please enter your birth year: "))


# another way to write this line
birth_year = input("what year were you born?")
birth_year = int(birth_year)
age = 2023 - birth_year
print(age)


# Calculate user's age
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"You are approximately {age} years old.")


# use 35,000,000 instead of 35000000

heartbeats = 10000 * 365 * age
print(f"your heart has beaten about {heartbeats:,.2} in your lifetime.")

# comment all the hyperlink
# I downloaded the animal heartbeats library
# Here's the URL where someone suggested how to use it


# Heart beats
human_heart_rate = 60
# A blue whale's heart can only beat roughly 33 times/min
blue_whale_heart_rate = 33
# A rabbit's resting heart rate ranges between 140 and 180 beats/min
rabbit_heart_rate = 140

human_heartbeats = round(age * 365 * 24 * 60 * human_heart_rate, 2)
blue_whale_heartbeats = round(age * 365 * 24 * 60 * blue_whale_heart_rate, 2)
rabbit_heartbeats = round(age * 365 * 24 * 60 * rabbit_heart_rate, 2)

print(f"Your heart has beaten approximately {human_heartbeats} times.")
print(f"A blue whale's heart has beaten approximately {blue_whale_heartbeats} times.")
if rabbit_heartbeats > 10**6:
    rabbit_heartbeats /= 10**6
    print(
        f"A rabbit's heart has beaten approximately {rabbit_heartbeats} million times."
    )
else:
    print(f"A rabbit's heart has beaten approximately {rabbit_heartbeats} times.")


# Age in Venus and Neptune years
venus_year_ratio = 0.615
neptune_year_ratio = 164.79
venus_years = round(age / venus_year_ratio, 2)
neptune_years = round(age / neptune_year_ratio, 2)
print(f"You are approximately {venus_years} Venus years old.")
print(f"You are approximately {neptune_years} Neptune years old.")


# Comparison with my age
my_age = 21
if age > my_age:
    print(f"You are older than me by {age - my_age} years.")
elif age < my_age:
    print(f"You are younger than me by {my_age - age} years.")
else:
    print("You are the same age as me.")


# Even or odd year (modulo)
if birth_year % 2 == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")


# Democratic Presidents since birth
democratic_presidents = [
    {"name": "John F. Kennedy", "term": [1961, 1963]},
    {"name": "Lyndon B. Johnson", "term": [1963, 1969]},
    {"name": "Jimmy Carter", "term": [1977, 1981]},
    {"name": "Bill Clinton", "term": [1993, 2001]},
    {"name": "Barack Obama", "term": [2009, 2017]},
    {
        "name": "Joe Biden",
        "term": [2021, 2023],
    },  # Adjust the term as per the current date
]

# Initialize a counter for Democratic presidents
count_dem_presidents = 0

# Loop through the list of Democratic presidents
for president in democratic_presidents:
    # Check if the user was born during the president's term
    if president["term"][0] <= birth_year < president["term"][1]:
        # if yes, increment the counter by 1
        count_dem_presidents = count_dem_presidents + 1

print(
    f"Since you were born, there have been {count_dem_presidents} Democratic presidents."
)


# don't do range(len(xxx))
# YES!!


# President during birth year (need to go to TA!)
president_during_birth_year = next(
    (
        president["name"]
        for president in democratic_presidents
        if president["term"][0] <= birth_year < president["term"][1]
    ),
    None,
)
if president_during_birth_year:
    print(f"The president when you were born was {president_during_birth_year}.")
else:
    print(
        "The president when you were born was not a Democrat (or data not available)."
    )
