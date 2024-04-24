import streamlit as st

#Main Page

#Title
st.title('Municipality Codes')

#Displaybox for codes
initial_content = """a
a
a
a
a
a
a
a
a
a
a
a
aa
a
a
a
a

aa

a
aa

a
a
a
a
a
a
"""
display_box = st.text_area("Display Box", value=initial_content, height=600, disabled=True, label_visibility="collapsed")

#Sidebar
st.sidebar.header('Settings')

#Dropdown for county (fetch it dynamically through directory)
option = st.sidebar.selectbox(
    'Which number do you like best?',
     [1, 2, 3, 4, 5], key="dropdown1")

#Dropdown for Criteria
option1 = st.sidebar.selectbox(
    'Which number do you like best?',
     [1, 2, 3, 4, 5], key="dropdown2")

# Displaying a button in the sidebar
button_clicked = st.sidebar.button('Enter')


if button_clicked:
    st.sidebar.write("You clicked the button!")

