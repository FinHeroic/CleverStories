# Get user input
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

# Calculate the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# Display the subtotal
print(f"Subtotal: ${subtotal:.2f}")

# Calculate and display the sales tax
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate and display the total price
total_price = subtotal + sales_tax
print(f"Total: ${total_price:.2f}")

# Get the payment amount from the user
payment_amount = float(input("What is the payment amount? "))

# Calculate and display the change
change = payment_amount - total_price
print(f"Change: ${change:.2f}")
