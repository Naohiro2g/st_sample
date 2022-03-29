import streamlit as st

st.title("Hello World!")
st.write("Welcome to my first app!")
st.markdown("#### This is a markdown section")
age = st.slider("How old are you?", 0, 100)
st.write("So, you're %d years old." % age)
# fruit1 = st.selectbox("What's your favorite fruit?", ["Apples", "Bananas", "Cherries"])
# fruit2 = st.multiselect("What's your favorite fruit?", ["Apples", "Bananas", "Cherries"])
# fruit1
# fruit2

st.balloons()