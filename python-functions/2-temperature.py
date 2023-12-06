unit = input("is thi s temperatire in Celsius or in Fahrengeit (C/F)")
temp = float(input("Enter the temperature:: "))
if unit == "C":
    temp =round((9 * temp)/5+32, 2)
    print(f"temperatire in Fahrenheit is: {temp}°C")
elif unit =="F":
    temp = round((temp-32)* 5/9, 2)
    print(f"temperatire in Celsius is: {temp}°F")
else:
    print(f"{unit} is an invalid unit of measurement")