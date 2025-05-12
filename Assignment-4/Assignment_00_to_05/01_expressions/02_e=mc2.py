
def main():
    c = 299792458  
    input_mass = float(input("Enter mass in kg: "))
    energy_in_mass = input_mass *(c**2)

    print(f"The mass you entered is: {input_mass} kg")
    print(f"The speed of light is: {c} m/s")
    print(f"So while using formula: E = m * c^2, the output is...")
    print(f"Energy in mass is = {energy_in_mass} Joules.")

if __name__ == "__main__":
    main()