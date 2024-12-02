import streamlit as st
import pandas as pd

user = st.text_input("who is saving", "Larry")

number = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)
st.write("The current number is ", number)

st.write("Hello☺️! This is a helpful daily schedule to help you be more: Fabulously Encouraging, Lovely, Incredible, Careing, Incomprehendibly Trustworthy, Yummilicious!") 

# Part 1:
# This puts some starting values in the list of todos
if "TODO_LIST" not in st.session_state:
    st.session_state["TODO_LIST"] = ["Clean Room", "Check Mailbox"]

# Part 2:
# Gives you a box to write in
# And then there's a button
# If you push that button, it adds the thing you typed to the list
number = st.number_input(
    "set your gole boundrys", value=None, placeholder="Type a number..."
)
st.write("The current gole is ", number)

if st.button("add some money"):
    st.session_state["TODO_LIST"].append(title)


# Part 3:
# For each item in your list, it makes a checkbox
for checkbox in st.session_state["TODO_LIST"]:
    st.checkbox(checkbox)





