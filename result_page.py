import streamlit as st

def result_page():
    st.title("Placement Prediction Result")

    if 'student_name' in st.session_state and 'result' in st.session_state:
        student_name = st.session_state['student_name']
        result = st.session_state['result']

        if result == 1:
            st.success(f"🎉 Congratulations {student_name}! You are likely to be placed.")
            st.subheader("Recommendations for further improvement:")
            st.write("- Take advanced internships to sharpen skills.")
            st.write("- Prepare for technical interviews using [GeeksforGeeks](https://www.geeksforgeeks.org/) and [PrepInsta](https://prepinsta.com).")
        else:
            st.warning(f"😞 Sorry {student_name}, you are not likely to be placed currently.")
            st.subheader("Recommendations to improve your chances:")
            st.write("- Take free internships at [Internshala](https://internshala.com).")
            st.write("- Focus on e-test preparation at [IndiaBix](https://www.indiabix.com/).")

    else:
        st.info("No prediction available. Please enter data in Data Entry Page first.")

if __name__ == '__main__':
    result_page()
