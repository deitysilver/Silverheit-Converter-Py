import streamlit as st

st.title("Temperature Conversion: Silverheit System")

st.write("""
1. Celsius to Silverheit
2. Silverheit to Celsius
3. Fahrenheit to Silverheit
4. Silverheit to Fahrenheit
5. Silverheit to Kelvin
6. Kelvin to Silverheit
""")

# Getting user input
choice = st.selectbox("Select conversion option (1-6):", options=["1", "2", "3", "4", "5", "6"])
value = st.number_input("Enter temperature value:")

# Perform conversion based on user choice
if st.button("Convert"):
    if choice == "1":
        result = value * 2.7
        st.write(f"{value} Celsius is equal to {result:.2f} Silverheit")
        
    elif choice == "2":
        result = value / 2.7
        st.write(f"{value} Silverheit is equal to {result:.2f} Celsius")
        
    elif choice == "3":
        result = (value - 32) * 1.5
        st.write(f"{value} Fahrenheit is equal to {result:.2f} Silverheit")
        
    elif choice == "4":
        result = (value / 1.5) + 32
        st.write(f"{value} Silverheit is equal to {result:.2f} Fahrenheit")
        
    elif choice == "5":
        result = (value / 2.7) + 273.15
        st.write(f"{value} Silverheit is equal to {result:.2f} Kelvin")
        
    elif choice == "6":
        result = (value - 273.15) * 2.7
        st.write(f"{value} Kelvin is equal to {result:.2f} Silverheit")
else:
    st.write("Please select a conversion option and enter a temperature value.")
