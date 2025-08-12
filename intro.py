import streamlit as st
click = st.sidebar.button("Abort App")
if click:
    st.stop()
st.title("Welcome to My Streamlit App")

st.header("Building Interactive :red[Web Apps] with Python :snake:")

st.write('Learning Streamlit is fun!')

agree = st.checkbox('I agree to the terms and conditions')

if agree:
    st.write("Thank you, you're welcome to proceed!")
else:
    st.write("Please agree to the terms and conditions to continue.")

st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate through the app.")
st.sidebar.selectbox(
    "Choose an option:",
    ['Option 1', 'Option 2', 'Option 3']
)

genre = st.radio(
    "Select your favorite genre:",
    ['Comedy','Action', 'Drama', 'Horror', 'Sci-Fi']
)

if genre == 'Action':
    st.write("You selected Action! Get ready for some thrilling adventures!")