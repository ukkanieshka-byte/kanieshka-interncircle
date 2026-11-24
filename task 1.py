def calculator():
    print("\n--- Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Select operation (1-4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        return
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    if choice == "1":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == "4":
        if num2 == 0:
            print("Error: Division by zero.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    choice = input("Select conversion (1-4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        return
    try:
        val = float(input("Enter value to convert: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if choice == "1":
        print(f"Result: {val} km = {val * 0.621371:.2f} miles")
    elif choice == "2":
        print(f"Result: {val} miles = {val / 0.621371:.2f} km")
    elif choice == "3":
        print(f"Result: {val}°C = {(val * 9/5) + 32:.2f}°F")
    elif choice == "4":
        print(f"Result: {val}°F = {(val - 32) * 5/9:.2f}°C")
def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
if __name__ == "__main__":
    main()
