# 1️⃣ List (list)

# Mutable: You can change, add, or remove elements.

my_list = [1, 2, 3]
print(my_list)
print(id(my_list))
my_list[0] = 10        # Change element
my_list.append(4)# Add element
my_list.remove(2)      # Remove element
print(my_list)         # [10, 3, 4]
print(id(my_list))         # [10, 3, 4]

# 2️⃣ Dictionary (dict)

# Mutable: Keys stay the same (if hashable), values can change.

my_dict = {"a": 1, "b": 2}
my_dict["a"] = 10      # Change value
my_dict["c"] = 30      # Add key-value pair
del my_dict["b"]       # Delete key
print(my_dict)         # {'a': 10, 'c': 30}

# 3️⃣ Set (set)

# Mutable: Add or remove elements, but no duplicates.

my_set = {1, 2, 3}
my_set.add(4)          # Add element
my_set.remove(2)       # Remove element
print(my_set)          # {1, 3, 4}

# 4️⃣ Bytearray (bytearray)

# Mutable: Like bytes but can be changed.
#
b = bytearray([1, 2, 3])
b[0] = 10
b.append(4)
print(list(b))              

# 5️⃣ Other mutable objects (less common)

# User-defined classes / objects – if their attributes can be changed.

class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
p.name = "Bob"        # Can change attribute
print(p.name)         # Bob