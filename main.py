import streamlit as st

def celsius_to_silverheit(celsius):
    return celsius * 2.7

def silverheit_to_celsius(silverheit):
    return silverheit / 2.7

def fahrenheit_to_silverheit(fahrenheit):
    return (fahrenheit - 32) * 1.5

def silverheit_to_fahrenheit(silverheit):
    return (silverheit / 1.5) + 32

def silverheit_to_kelvin(silverheit):
    return (silverheit / 2.7) + 273.15

def kelvin_to_silverheit(kelvin):
    return (kelvin - 273.15) * 2.7

st.title("Temperature Conversion: Silverheit System")

conversion_options = {
    "Celsius to Silverheit": celsius_to_silverheit,
    "Silverheit to Celsius": silverheit_to_celsius,
    "Fahrenheit to Silverheit": fahrenheit_to_silverheit,
    "Silverheit to Fahrenheit": silverheit_to_fahrenheit,
    "Silverheit to Kelvin": silverheit_to_kelvin,
    "Kelvin to Silverheit": kelvin_to_silverheit
}

tab = st.selectbox("Select conversion option:", options=list(conversion_options.keys()))

value = st.number_input("Enter temperature value:", format="%f")

if st.button("Convert"):
    conversion_function = conversion_options[tab]
    try:
        result = conversion_function(value)
        st.write(f"{value} in selected unit is equal to {result:.2f} in the target unit.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please select a conversion option and enter a temperature value.")
