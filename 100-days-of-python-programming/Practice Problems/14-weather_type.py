# Write a program that will determine whether the value of temperature and humidity is provided by the user.

# | TEMPERATURE(C) | HUMIDITY(%) |     WEATHER    |
# |----------------|-------------|----------------|
# |      >= 30     |    >= 90    | Hot and Humid  |
# |      >= 30     |    <  90    |      Hot       |
# |      <  30     |    >= 90    | Cold and Humid |
# |      <  30     |    <  90    |      Cold      |

temperature = int(input("Enter the Temperature in celcius: "))
humidity = int(input("Enter the Humidity percentage: "))

if temperature >= 30 and humidity >= 90:
    print("Temperature is Hot and Humid")

elif temperature >= 30 and humidity < 90:
    print("Temperature is Hot")

elif temperature < 30 and humidity >= 90:
    print("Temperature is Cool and Humid")
    
else:
    print("Temperature is Cool")