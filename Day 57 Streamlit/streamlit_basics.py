import streamlit as st

# Title
st.title("🚀 My First Streamlit App")

# Text
st.write(
    "Welcome to Day 57 of Python Library A Day!"
)

# User Input
name = st.text_input(
    "Enter your name:"
)

if name:
    st.success(
        f"Hello, {name}! 👋"
    )

# Button
if st.button("Click Me"):
    st.balloons()
    st.write("Button Clicked!")