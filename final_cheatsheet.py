import streamlit as st
import pandas as pd

st.title("Streamlit Widgets Reference")

st.header("Header Example")
st.subheader("Subheader Example")

# File Uploader
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.write("Uploaded file preview:")
    st.dataframe(df.head())

# Tabs
tab1, tab2, tab3 = st.tabs(["Chart", "Data", "About"])
with tab1:
    st.write("This is the chart tab")
with tab2:
    st.write("This is the data tab")
with tab3:
    st.write("About this app")

# Columns
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")

# Selectbox
option = st.selectbox("Choose one", ["Python", "R", "Julia"])
st.write("You selected:", option)

# Text Input
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

# Number Input
age = st.number_input("Your age", min_value=0, max_value=120, step=1)
st.write(f"Age: {age}")

# Success Message
st.success("This is a success message!")

# Button
if st.button("Click me!"):
    st.balloons()

# Form
with st.form("my_form"):
    email = st.text_input("Email")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success(f"Submitted email: {email}")

# Expander
with st.expander("Click to see hidden details"):
    st.write("Secret info inside!")
