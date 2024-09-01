import streamlit as st
import pandas as pd
#widgets
st.title("Streamlit text input")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}")
else:
    st.write("Please enter your name")

age = st.slider("Select your age:",0,100,18)

options = ["python","java","c"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")

data = {
    "Name":["John","Jake","Jake","Jill"],
    "Age":[28,22,34,19],
    "City":["New York","Los Angeles","Chicago","Downtown"]
}
df = pd.DataFrame(data)
st.write(df)
st.selectbox("choose",df.iloc[1]) #for row
st.selectbox("choose",df.Age) #for column

#upload
uploaded_file = st.file_uploader("Choose a file",type = ["csv","pdf","txt"])

