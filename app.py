
# import streamlit as st
# from streamlit_option_menu import option_menu

# st.title('Hello, Students!')
# st.write('This is your Python Programming course.')

# with st.sidebar:
#     selected=option_menu(
#         menu_title = "Menu",
#         options = ["Home", "About", "Contact"],
#         icons = ["house",
#                  "2-circle-fill",
#                  "3-circle-fill"],
#         menu_icon= "emoji-smile-fill",
#         default_index=0,
#     )

# if selected == "Home":
#     st.title(f"Welcome to the {selected} page.")

# if selected == "About":
#     st.title(f"Welcome to the {selected} page.")

# if selected == "Contact":
#     st.title(f"Welcome to the {selected} page.")

import streamlit as st
import pandas as pd
import os

# Get the current working directory
current_directory = os.getcwd()
# Define the file path
file_path = os.path.join(current_directory, 'winequality-red.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, delimiter=';')

# Display the DataFrame in an interactive table
st.write("Wine Quality Data")
st.dataframe(df)


data = {
    'Product': ['A', 'B', 'C'],
    'Sales': [1200, 850, 950],
    'Customers': [300, 400, 350]
}
df = pd.DataFrame(data)
