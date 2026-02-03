sugar_amount=4
print(f"amount={sugar_amount}")
sugar_amount=12
print(f"amount={sugar_amount}")
print(f"id of 4={id(4)}")
print(f"id of 12={id(12)}")


# mutable
name="preeti"
print(f"name:{name}")
print(f"name:{id(name)}")
name = "h" + name[1:]
print("New string:", name)
print("New string:", id(name))
a = 5
print(id(a))  # Memory address
a = a + 1
print(id(a))


# immutable
spice_mix=set()
print(f"id:{id(spice_mix)}")
print(f"id:{spice_mix}")

spice_mix.add("ginger")
spice_mix.add("cardmom")
print(f"after id;{id(spice_mix)}")
print(f"after id;{spice_mix}")
b = [1, 2, 3]
print(id(b))  # Memory address
b.append(4)
print(id(b))

# using tuple

# Create a tuple
my_tuple = (10, 20, 30)

# Access elements
print("set", my_tuple)
print("First:", my_tuple[0])
print("Last:", my_tuple[2])
print("Last:", id(my_tuple[2]))


# Concatenate tuple
new_tuple = my_tuple + (40, 50)
print("After adding:", new_tuple)
print("After adding:",id( new_tuple))