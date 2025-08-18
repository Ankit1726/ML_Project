import streamlit as st
import pandas as pd

# Title of the application
st.title(" Welcome Streamlit ✌️")

st.title('Streamlit Text Input')
name = st.text_input('enter your name')


age=st.slider('select your age ',0,100,21)
st.write(f'your age is {age}')

options = ['Python',"C++","JavaScript","Java","Java"]
choice = st.selectbox("choose your language ",options)

if name:
    st.write(f'Hello {name}')

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

upoaded_file = st.file_uploader('choose your csv file',type='csv')

if upoaded_file is not None:
    df = pd.read_csv(upoaded_file)
    st.write(df)