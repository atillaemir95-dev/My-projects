choice = input("Hello choose one of these to generate ((C->F or F->C) ")

if choice.upper() == "C->F":
    celcius = float(input("choose the celcius degree : "))
    fahrenhiet = (celcius * 9/5) + 32
    print(f"{celcius}°C = {fahrenhiet}°F")
elif choice.upper() == "F->C":
    fahrenheit = float(input("Choose the Fahrenheit degree: "))
    celcius = (fahrenheit -32) * 5/9
    print(f"{fahrenheit}°F = {celcius}°C ")

else:
    print("Invalid choice please choose 'F->C' or 'C->F'")