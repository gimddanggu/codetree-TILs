product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class sol:
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code

a = sol()
b = sol(product_name, product_code)

print(f"product {a.code} is {a.name}")
print(f"product {b.code} is {b.name}")

    
