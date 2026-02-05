


# Step 1: Create a customer dictionary with name, age, and city
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}
print(customer)

# Step 2: Add email and phone

customer["email"] = "preeti@gmail.com"
customer["phone"] = 456789

print(f"added -> {customer}")

# Step 3: Print customer's name and city
print(f" name and city:-{customer['name']},{customer['city']}")

# Step 4: Check if "email" exists
print(f"email exits :-{'email' in customer}")

# Step 5: Delete the "age" field
del customer["age"]
print(f"customer after age->{customer}")

# Step 6: Print all keys, values, and items
print(f"customer keys->{customer.keys()}")
print(f"customer values->{customer.values()}")
print(f"customer items->{customer.items()}")


# Step 7: Remove and print the last inserted item
last_item=customer.popitem()
print(customer)

# Step 8: Use .get() to access "membership"
customer_note=customer.get("email")
print(customer_note)

# Step 9: Update dictionary with "address"

customer.update({"address":"flat b1/9"})
print(customer)

# Step 10: Print final dictionary
print(customer)