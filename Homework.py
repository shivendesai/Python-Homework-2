#Written by Shiven Desai
#This code will tell the user what quarter of the year a specific month is in
#month creates an input where the user can enter a number for a month 
month = int(input("Enter a month as a number between 1 and 12: "))
#These if else statements will calculate what quarter of the year a month is in
if month >= 1 and month <= 12:
    if month >= 1 and month <= 3:
        print("The month is in the first quarter of the year.")
    elif month >= 4 and month <= 6:
        print("The month is in the second quarter of the year.")
    elif month >= 7 and month <= 9:
        print("The month is in the third quarter of the year.")
    else:
        print("The month is in the fourth quarter of the year.")
else:
    print("Error: Please enter a number between 1 and 12.")
