# streamlit run app.py --server.port 9993

import streamlit as st
import pandas as pd
import numpy as np


st.title("Age Predictor")

number = st.selectbox("Please Select Any Number", (2, 3, 4, 5, 6, 7, 8, 9, 10, ))
st.write("You Have Selected", number)

new_number = number * 2
new_number1 = new_number + 5
new_number2 = new_number1 * 50
# st.write(new_number)
# st.write(new_number1)
# st.write(new_number2)

birthday_celebration = st.radio("Have You Already Celebrated Your Birthday ?", ("Yes", "No"))

if birthday_celebration == "Yes":
    new_number3 = new_number2 + 1770
    # st.write(new_number3)
    born_age1 = st.number_input("When Did You Born")   
    # st.write(born_age1) 
    final_step = new_number3 - born_age1
    st.write(final_step)


if birthday_celebration == "No":
    new_number4 = new_number2 + 1769
    # st.write(new_number4)
    born_age2 = st.number_input("When Did You Born")   
    # st.write(born_age2) 
    final_step1 = str(new_number4 - born_age2)
    st.write("Your Age is ", final_step1[1:3])


    






















    














































































