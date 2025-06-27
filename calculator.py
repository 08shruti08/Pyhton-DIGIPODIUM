#streamlit run calculator.py
import streamlit as st

st.title("Simple Calculator")
st.markdown("This is a simple calculator app built with Streamlit.")  # st.write("This is a simple calculator app built with Streamlit.") : work same as st.markdown          

c1,c2 = st.columns(2)

fnum = c1.number_input("Enter First number", value = 0)      
snum = c2.number_input("Enter second number", value = 0)             

options = ["Add","Substract", "Multiply", "DIVIDE" ]
choice = st.radio("Select Operation", options)  

button = st.button("Calculator")
result = 0
  
if button:
    if choice == "Add":
        result = fnum +snum
    if choice =="Subtract":
        result = fnum - snum
    if choice =="Multiply":
        result = fnum * snum
    if choice =="Divide":
        result = fnum / snum

st.success(f"Result: {result}") 


 