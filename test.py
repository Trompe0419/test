import streamlit as st

st.title("QCounter+")


seven_three = st.checkbox("7o3x")

if seven_three:
   
   if 'CC' not in st.session_state:
      st.session_state["CC"] = 0
   if st.button("o", key=0):
      st.session_state["CC"] += 1
   st.write("o", st.session_state["CC"])
   if 'inCC' not in st.session_state:
      st.session_state["inCC"] = 0
   if st.button("x", key=1):
      st.session_state["inCC"] += 1
   st.write("x", st.session_state["inCC"])
