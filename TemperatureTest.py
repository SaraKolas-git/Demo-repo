# Temperature Converter: Celsius <-> Fahrenheit

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Choose an option (1 or 2): ").strip())
        if choice not in (1, 2):
            print("Invalid choice. Please select 1 or 2.")
            return

        temp_input = input("Enter the temperature value: ").strip()
        temperature = float(temp_input)  # May raise ValueError if invalid

        if choice == 1:
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C = {result:.2f}°F")
        else:
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F = {result:.2f}°C")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()