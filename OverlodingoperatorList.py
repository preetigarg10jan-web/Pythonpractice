my_cart=["apple","bananas","milk"]
print(f"output:{my_cart}")

my_cart.append("bread")
print(f"output:{my_cart}")

my_cart.insert(0,"ketchup")
print(f"output:{my_cart}")

my_cart.remove("bananas")
print(f"output:{my_cart}")



removed_item=my_cart.pop()
print(f"removed_item output:{removed_item}")
add_ingredient=["rice","butter"]
my_cart.extend(add_ingredient)
print(f"updated grocery:{my_cart}")

my_cart.sort()
print(f"output:{my_cart}")


my_cart.reverse()
print(f"output:{my_cart}")

drinks=["juice","jam"]
full_list=my_cart+drinks
print(f" full list ->{full_list}")

new_cart=[my_cart]*2
print(f"newcart->{new_cart}")