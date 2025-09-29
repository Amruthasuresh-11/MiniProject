import streamlit as st
from home_page import home
from data_entry_page import data_entry
from result_page import result_page
from aptitude_test_page import aptitude_test

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home"
if "student_name" not in st.session_state:
    st.session_state["student_name"] = ""
if "etest_p" not in st.session_state:
    st.session_state["etest_p"] = 0.0
if "result" not in st.session_state:
    st.session_state["result"] = None
if "prob" not in st.session_state:
    st.session_state["prob"] = None

# Pages dictionary
PAGES = {
    "Home": home,
    "Data Entry": data_entry,
    "Aptitude Test": aptitude_test,
    "Result": result_page
}

# Display current page
PAGES[st.session_state["page"]]()
