product_code = int(input("Enter the product code (1 for Battery-based, 2 for Key-based, 3 for Electrical Charging): "))
order_amount = float(input("Enter the order amount: "))

if product_code == 1:
    if order_amount > 1000:
        discount = 0.10
    else:
        discount = 0
elif product_code == 2:
    if order_amount > 100:
        discount = 0.05
    else:
        discount = 0
elif product_code == 3:
    if order_amount > 500:
        discount = 0.10
    else:
        discount = 0
else:
    print("Invalid product code.")
    discount = 0

net_amount = order_amount - (order_amount * discount)

print("The net amount to pay is: Rs.", net_amount)