cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price - cost_price > 0:
    print("Profit")
elif selling_price == cost_price:
    print("Neither Profit not Loss")
else:
    print("Loss")

# Second Method

cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price > cost_price:
    amount = selling_price - cost_price
    print("Profit amount ", amount)

elif selling_price == cost_price:
    print("Neither Profit nor Loss")

else:
    amount = cost_price - selling_price
    print("Loss amount:", amount)