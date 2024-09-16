print("""
1. Celsius to Revanite
2. Revanite to Celsius
3. Fahrenheit to Revanite
4. Revanite to Fahrenheit
5. Revanite to Kelvin
6. Kelvin to Revanite\n""")

choice = input("Enter choice (1-6): ")

value = float(input("\nEnter temperature value: "))

print()

if choice == "1":
    result = value * 2.7
    print(f"{value} Celsius is equal to {result:.2f} Revanite")
    
elif choice == "2":
    result = value / 2.7
    print(f"{value} Revanite is equal to {result:.2f} Celsius")
    
elif choice == "3":
    result = (value - 32) * 1.5
    print(f"{value} Fahrenheit is equal to {result:.2f} Revanite")
    
elif choice == "4":
    result = (value / 1.5) + 32
    print(f"{value} Revanite is equal to {result:.2f} Fahrenheit")
    
elif choice == "5":
    result = (value / 2.7) + 273.15
    print(f"{value} Revanite is equal to {result:.2f} Kelvin")
    
elif choice == "6":
    result = (value - 273.15) * 2.7
    print(f"{value} Kelvin is equal to {result:.2f} Revanite")

else:
    print("Invalid choice.")
