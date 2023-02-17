#Written by Shiven Desai
#This program shows discounts for shipping packages
# Define the price of a single package
PACKAGE_PRICE = 99

# Get the number of packages purchased from the user
num_packages = int(input("Enter the number of packages purchased: "))

# Calculate the discount percentage based on the number of packages purchased
if num_packages >= 10 and num_packages <= 19:
    discount_percentage = 0.1
elif num_packages >= 20 and num_packages <= 49:
    discount_percentage = 0.2
elif num_packages >= 50 and num_packages <= 99:
    discount_percentage = 0.3
elif num_packages >= 100:
    discount_percentage = 0.4
else:
    discount_percentage = 0.0

# Calculate the total price after the discount
discount_amount = num_packages * PACKAGE_PRICE * discount_percentage
total_price = num_packages * PACKAGE_PRICE - discount_amount

# Print the results
print("Discount amount:", "${:.2f}".format(discount_amount))
print("Total amount after discount:", "${:.2f}".format(total_price))

