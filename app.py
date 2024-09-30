import streamlit as st

st.title("Housing Heritage Issues")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.write(f"Hello {name}!")

