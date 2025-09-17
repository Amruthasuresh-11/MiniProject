import streamlit as st
from home_page import home
from data_entry_page import data_entry
from result_page import result_page

PAGES = {
    "Home": home,
    "Data Entry": data_entry,
    "Result": result_page
}

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Display the selected page
page = PAGES[st.session_state["page"]]
page()
