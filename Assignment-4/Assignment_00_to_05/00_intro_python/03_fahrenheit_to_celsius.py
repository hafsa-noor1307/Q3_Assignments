def main():
    print("Let's convert Fahrenheit temperature to Celsius.")
    inp = input("Enter temperature in Fahrenheit: ")
    fahrenheit = float(inp)
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is {celsius:.2f}°C.")

if __name__ == "__main__":  
    main()