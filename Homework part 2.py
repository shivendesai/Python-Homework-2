#Written by Shiven Desai
#This program calculates the number of hot dogs and buns for people
# Constants for number of hot dogs per package and buns per package
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Get the number of people attending the cookout and the number of hot dogs each person will be given
num_people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Calculate the total number of hot dogs needed
total_hot_dogs = num_people * hot_dogs_per_person

# Calculate the number of packages of hot dogs needed
packages_of_hot_dogs = total_hot_dogs // HOT_DOGS_PER_PACKAGE
if total_hot_dogs % HOT_DOGS_PER_PACKAGE > 0:
    packages_of_hot_dogs += 1

# Calculate the number of hot dogs that will be left over
hot_dogs_left_over = (packages_of_hot_dogs * HOT_DOGS_PER_PACKAGE) - total_hot_dogs

# Calculate the total number of hot dog buns needed
total_buns = num_people * hot_dogs_per_person
packages_of_buns = total_buns // BUNS_PER_PACKAGE
if total_buns % BUNS_PER_PACKAGE > 0:
    packages_of_buns += 1

# Calculate the number of hot dog buns that will be left over
buns_left_over = (packages_of_buns * BUNS_PER_PACKAGE) - total_buns

# Print the results
print("Minimum number of packages of hot dogs required:", packages_of_hot_dogs)
print("Minimum number of packages of hot dog buns required:", packages_of_buns)
print("Number of hot dogs left over:", hot_dogs_left_over)
print("Number of hot dog buns left over:", buns_left_over)

