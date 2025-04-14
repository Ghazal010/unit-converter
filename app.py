import streamlit as st
from pint import UnitRegistry

# Set page config - Sabse pehle!
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        /* Background color */
        .main {
            background-color:rgb(138, 213, 240);
        }
        /* Sidebar background */
        [data-testid="stSidebar"] {
            background-color: #2c3e50;
        }
        /* Sidebar text color */
        [data-testid="stSidebar"] * {
            color: white;
        }
        /* Button styling */
        div.stButton > button {
            background-color: #3498db;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
        }
        /* Button hover effect */
        div.stButton > button:hover {
            background-color: #2980b9;
        }
        /* Title styling */
        .stMarkdown h1 {
            color: #2c3e50;
        }
    </style>
    """,
    unsafe_allow_html=True
)

#Title
st.title("🌍 Unit Converter")
st.markdown("Convert units quickly and easily!")

#Sidebar 
st.sidebar.title("⚙ Sidebar Menu")

# Sidebar mein input fields
name = st.sidebar.text_input("Enter your Name:")

# Sidebar mein ek button
if st.sidebar.button("Submit"):
    st.sidebar.success(f"Hi👋, {name}!")

#Initialize unit registry
ureg = UnitRegistry()
ureg.define('square_micrometer = micrometer ** 2')
ureg.define('square_millimeter = millimeter ** 2')

#Categories of units
categories = {
    "Length": ["meter", "kilometer", "mile", "foot", "inch", "centimeter", "millimeter", "micrometer", "nanometer", "yard", "light_year"],
    "Weight": ["gram", "kilogram", "milligram", "metric_ton", "long_ton", "short_ton", "pound", "ounce", "carat", "atomic_mass_unit"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["L", "milliliter", "gallon", "cup", "meter ** 3", "kilometer ** 3", "cubic_centimeter", "cubic_millimeter"],
    "Time": ["second", "millisecond", "microsecond", "nanosecond", "minute", "hour", "day", "week", "month", "year"],
}

#Select category
category = st.selectbox("Select Category", list(categories.keys()))

#Select units
unit_options = categories[category]
from_unit = st.selectbox("From Unit", unit_options)
to_unit = st.selectbox("To Unit", unit_options)

#Input value
value = st.number_input("Enter Value", min_value=0.0, step=0.1, format="%.2f")

#Convert and display result
if st.button("Convert"):
    try:
        if category == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
        else:
            result = (value * ureg(from_unit)).to(to_unit).magnitude
        
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error! {str(e)}")

#Footer
st.markdown("---")
st.markdown("Made with 💡 and ☕ using Streamlit!")

