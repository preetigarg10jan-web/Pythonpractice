branch_a_products={"bread","milk","butter","jam"}
branch_b_products={"bread","cheese","butter","ketchup"}

print(f"{branch_a_products},{branch_b_products}")


All_product = branch_a_products | branch_b_products
print(f"union:->{All_product}")

common_product = branch_a_products & branch_b_products
print(f"common:->{common_product}")

Essential_product = branch_a_products - branch_b_products
print(f"Essential:->{branch_a_products}")

print(f"is ketchup is available:{'ketchup' in branch_a_products }")

products = ["bread", "milk", "butter","milk"]
frozen_products = frozenset(products)

print(frozen_products)


# 🔑 Key takeaway
# set is mutable
# frozenset is an immutable set—values cannot change, but set operations still work.