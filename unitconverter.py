import streamlit as st

def length_converter(value, from_unit, to_unit):
    length_units = {
        'meter': 1, 'kilometer': 0.001, 'centimeter': 100, 'millimeter': 1000,
        'mile': 0.000621371, 'yard': 1.09361, 'foot': 3.28084, 'inch': 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit]) if from_unit in length_units and to_unit in length_units else "Invalid unit"

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'gram': 1, 'kilogram': 0.001, 'milligram': 1000, 'pound': 0.00220462, 'ounce': 0.035274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit]) if from_unit in weight_units and to_unit in weight_units else "Invalid unit"

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    else:
        return "Invalid unit"

st.title("Unit Converter")

conversion_type = st.selectbox("Select conversion type:", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'mile', 'yard', 'foot', 'inch']
elif conversion_type == "Weight":
    units = ['gram', 'kilogram', 'milligram', 'pound', 'ounce']
else:
    units = ['celsius', 'fahrenheit', 'kelvin']

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From unit:", units)
to_unit = st.selectbox("To unit:", units)

if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    else:
        result = temperature_converter(value, from_unit, to_unit)
    
    
    st.success(f"Converted Value: {result}")
