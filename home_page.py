import streamlit as st

def home():
    st.title("🎓 Campus Placement Prediction Using Machine Learning")
    st.write("""
    Welcome to the **Campus Placement Prediction System**!  
    Check your placement chances based on academic details and performance.  
    You can also **try an aptitude test** to know your readiness or 
    proceed to the **placement prediction** page.
    """)

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📝 Try Aptitude Test", key="home_apt"):
            st.session_state["page"] = "Aptitude Test"

    with col2:
        if st.button("📊 Placement Prediction", key="home_data"):
            st.session_state["page"] = "Data Entry"
