principal_amount = int(input("Enter the pricipal amount: "))
rate_of_interest = int(input("Enter the rate of interest: "))
time_period = int(input("Enter the time period: "))

interest = (principal_amount * rate_of_interest * time_period)/100

print("Simple interest is ",interest)

Total_amount = principal_amount + interest
print("Total Amount is ", Total_amount)