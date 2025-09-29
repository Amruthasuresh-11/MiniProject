import streamlit as st

def result_page():
    st.title("Placement Prediction Result 🎯")

    if 'student_name' in st.session_state and 'result' in st.session_state:
        student_name = st.session_state['student_name']
        result = st.session_state['result']

        if result == 1:
            # Placed student message
            st.success(f"🎉 Congratulations {student_name}! You are likely to be placed.")
            st.subheader("🌟 Keep Growing and Excelling!")
            st.write("""
            You are on the right track. Keep building your skills and stay motivated.
            Here are some suggestions to further improve your career prospects:
            """)
            st.markdown("""
            1. Take **advanced internships** or projects to sharpen technical and managerial skills.  
            2. **Prepare for technical interviews** using platforms like [GeeksforGeeks](https://www.geeksforgeeks.org/) and [PrepInsta](https://prepinsta.com).  
            3. Improve your **communication, soft skills, and aptitude** for faster career growth.  
            """)

        else:
            # Not placed student message
            st.warning(f"😞 Sorry {student_name}, you are not likely to be placed currently.")
            st.subheader("💪 Don’t Worry! Keep Improving.")
            st.write("""
            Every setback is a step towards success. Focus on the areas below to enhance your chances:
            """)
            st.markdown("""
            1. Take **free internships** at [Internshala](https://internshala.com) to gain experience.  
            2. Practice **e-tests and aptitude questions** at [IndiaBix](https://www.indiabix.com/) and other resources.  
            3. Enhance your **technical knowledge** through online courses and projects.  
            4. Work on **communication skills, teamwork, and interview preparation** for better employability.  
            """)

        # ✅ Go back to home button
        if st.button("🏠 Go Back to Home"):
            st.session_state["page"] = "Home"

    else:
        st.info("No prediction available. Please enter data in Data Entry Page first.")
