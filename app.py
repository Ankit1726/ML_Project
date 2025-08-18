# run command : streamlit run app.py 
# more info : visit// stramlit.io

import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title(" Welcome Streamlit ✌️")

# Display Simple Text
st.write("Simple Text")

# create a simple dataframe
df = pd.DataFrame({
    'First Col':[1,2,3,4],
    'Second':[10,20,30,40]
})

# Display Dataframe
st.write("Here your Dataframe")
st.write(df)

# Create line Chart
chart_data = pd.DataFrame(
    np.random.randn(20,4),columns = ['a','b','c','d']
)
st.line_chart(chart_data)