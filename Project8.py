import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Input fields for weight and height
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (in cm):", min_value=0.0, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if height == 0:
        st.error("Height cannot be zero. Please enter a valid height.")
    else:
        # Convert height from cm to meters
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        st.success(f"Your BMI is: **{bmi:.2f}**")

        # Display BMI category
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")