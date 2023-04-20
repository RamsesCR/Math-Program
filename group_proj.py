import math

def calculator():
    operation = input("Do you want to add, subtract, multiply, or divide? ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    else:
        print("operation not available")

    print("Result:", result)


def temperature_converter():
    temperature = float(input("Enter temperature in Celsius: "))
    fahrenheit = temperature * 9/5 + 32
    print("Temperature in Fahrenheit:", fahrenheit)


def measurement_converter():
    inches = float(input("Enter measurement in inches: "))
    feet = inches / 12
    print("length in feet:", feet)


def circle_area():
    radius = float(input("Enter radius of circle: "))
    area = math.pi * radius ** 2
    print("Area of circle:", area)


def sphere_volume():
    radius = float(input("Enter radius of sphere: "))
    volume = 4/3 * math.pi * radius ** 3
    print("Volume of sphere:", volume)


# menu
while True:
    print("\nSelect an option:")
    print("1. Calculator")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Convert Inches to Feet")
    print("4. Circle Area Calculator")
    print("5. Sphere Volume Calculator")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        temperature_converter()
    elif choice == "3":
        measurement_converter()
    elif choice == "4":
        circle_area()
    elif choice == "5":
        sphere_volume()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
