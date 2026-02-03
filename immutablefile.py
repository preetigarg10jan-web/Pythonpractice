
# 1️⃣ Integer (int)
a = 5
print("Original a:", a)
print("Original id(a):", id(a))

# Trying to "change" a
a = a + 1
print("New a:", a)
print("New id(a):", id(a))

# 2️⃣ Float (float)
f = 3.14
f = f + 1
print(f)



# 3️⃣ String (str)
s = "Hello"
print("Original:", s)

# Trying to change
# s[0] = "h"   # ❌ This gives an error

# Correct way: create a new string
s_new = "h" + s[1:]
print("New string:", s_new)



# 4️⃣ Tuple (tuple)
t = (1, 2, 3)
print("Original tuple:", t)

# Trying to change
# t[0] = 10    # ❌ Error

# Concatenate creates a new tuple
t_new = t + (4, 5)
print("New tuple:", t_new)



# ⃣Boolean (bool)
b = True
print(b)
b = not b
print(b)






