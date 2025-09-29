import streamlit as st
import pandas as pd
import joblib

def data_entry():
    st.title("Enter Student Details")

    student_name = st.text_input("Student Name")

    gender = st.selectbox("Gender", ["Male", "Female"])
    ssc_p = st.number_input("Secondary Education Percentage (10th Grade)", 0.0, 100.0)
    ssc_b = st.selectbox("SSC Board", ["Central", "Others"])
    hsc_p = st.number_input("Higher Secondary Education Percentage (12th Grade)", 0.0, 100.0)
    hsc_b = st.selectbox("HSC Board", ["Central", "Others"])
    hsc_s = st.selectbox("HSC Stream", ["Commerce", "Science", "Arts"])
    degree_p = st.number_input("Degree Percentage", 0.0, 100.0)
    degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
    workex = st.selectbox("Work Experience", ["Yes", "No"])
    etest_p = st.number_input("E-Test Percentage", 0.0, 100.0)
    specialisation = st.selectbox("Specialisation", ["Mkt&HR", "Mkt&Fin"])
    mba_p = st.number_input("MBA Percentage", 0.0, 100.0)

    

    if st.button("Predict"):
        # Validation: Ensure all percentages are within 0 to 100
        invalid_inputs = []
        if not (0 <= ssc_p <= 100):
            invalid_inputs.append("Secondary Education Percentage (SSC %)")
        if not (0 <= hsc_p <= 100):
            invalid_inputs.append("Higher Secondary Education Percentage (HSC %)")
        if not (0 <= degree_p <= 100):
            invalid_inputs.append("Degree Percentage")
        if not (0 <= etest_p <= 100):
            invalid_inputs.append("E-Test Percentage")
        if not (0 <= mba_p <= 100):
            invalid_inputs.append("MBA Percentage")

        if invalid_inputs:
            st.error(f"⚠️ Please enter valid percentage values (0 to 100) for: {', '.join(invalid_inputs)}")
        else:
            new_data = pd.DataFrame({
                'gender': [0 if gender == "Male" else 1],
                'ssc_p': [ssc_p],
                'ssc_b': [1 if ssc_b == "Central" else 0],
                'hsc_p': [hsc_p],
                'hsc_b': [1 if hsc_b == "Central" else 0],
                'hsc_s': [1 if hsc_s == "Science" else (0 if hsc_s == "Commerce" else 2)],
                'degree_p': [degree_p],
                'degree_t': [1 if degree_t == "Sci&Tech" else (0 if degree_t == "Comm&Mgmt" else 2)],
                'workex': [1 if workex == "Yes" else 0],
                'etest_p': [etest_p],
                'specialisation': [1 if specialisation == "Mkt&Fin" else 0],
                'mba_p': [mba_p]
            })

            model = joblib.load('placement_prediction_model.pkl')
            result = model.predict(new_data)[0]
            proba = model.predict_proba(new_data)[0][1]

            st.session_state['student_name'] = student_name
            st.session_state['result'] = result
            st.session_state['prob'] = proba

            st.success("✅ Data submitted! Redirecting to Result Page...")

            st.session_state["page"] = "Result"
            st.rerun()

if __name__ == '__main__':
    data_entry()
