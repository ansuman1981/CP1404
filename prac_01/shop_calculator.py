total_price = 0
items = int(input("Number of items: "))
for i in range(1, items + 1):
    price = float(input("price of items: "))
    while price <= 0:
        print("invalid number of items")
        price = float(input("price of items: "))
    total_price += price
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {items}: ${total_price:.2f}")

