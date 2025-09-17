import streamlit as st

def home():
    st.title("🏫 Campus Placement Prediction System")

    st.write("""
        Welcome to the Campus Placement Prediction System.  
        This system predicts whether a student will be placed based on academic and other personal details.
    """)

    if st.button("Get Started"):
      st.session_state["page"] = "Data Entry"  # use session_state instead of query params
      st.rerun()  # reload app to navigate
 
if __name__ == '__main__':
    home()
