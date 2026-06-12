import streamlit as st

st.title("MedicalMind")

question = st.text_input("Ask a nursing question")

if question:
    st.write("Question:", question)

    if "cpr" in question.lower():
        st.write("CPR: Check responsiveness, call for help, start chest compressions.")
    elif "iv" in question.lower():
        st.write("IV Cannulation: Verify patient, prepare equipment, maintain aseptic technique.")
    else:
        st.write("Knowledge base is under development.")


