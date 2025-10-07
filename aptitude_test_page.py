# aptitude_test_page.py
import streamlit as st
import matplotlib.pyplot as plt
import random

# ✅ Full question bank with 50 questions
QUESTION_BANK = [
    {"question": "What is 25% of 200?", "options": ["25", "50", "75", "100"], "answer": "50"},
    {"question": "If 12 men can build a wall in 6 days, how many days will 6 men take?", "options": ["6", "12", "18", "24"], "answer": "12"},
    {"question": "The next term in the series 2, 6, 12, 20, ?", "options": ["28", "30", "32", "34"], "answer": "30"},
    {"question": "Simplify: 144 ÷ 12 + 6", "options": ["15", "16", "17", "18"], "answer": "18"},
    {"question": "A train 150m long crosses a pole in 15 sec. Its speed is:", "options": ["5 m/s", "10 m/s", "12 m/s", "15 m/s"], "answer": "10 m/s"},
    {"question": "The average of 5, 10, 15, 20, 25 is:", "options": ["10", "12", "15", "18"], "answer": "15"},
    {"question": "Solve: (3/4) of 200", "options": ["100", "120", "140", "150"], "answer": "150"},
    {"question": "The square root of 784 is:", "options": ["26", "28", "30", "32"], "answer": "28"},
    {"question": "The LCM of 12 and 18 is:", "options": ["24", "36", "48", "60"], "answer": "36"},
    {"question": "If selling price is Rs. 120 and gain is 20%, cost price is:", "options": ["Rs. 90", "Rs. 95", "Rs. 100", "Rs. 110"], "answer": "Rs. 100"},
    {"question": "What is the simple interest on Rs. 1000 at 5% for 2 years?", "options": ["Rs. 50", "Rs. 75", "Rs. 100", "Rs. 120"], "answer": "Rs. 100"},
    {"question": "Which number is divisible by 9?", "options": ["1458", "2345", "4567", "8752"], "answer": "1458"},
    {"question": "If x + 5 = 12, then x = ?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Speed = Distance/Time. If distance = 120 km and time = 2 hrs, speed = ?", "options": ["50 km/hr", "60 km/hr", "70 km/hr", "80 km/hr"], "answer": "60 km/hr"},
    {"question": "The perimeter of a square of side 7 cm is:", "options": ["21 cm", "28 cm", "35 cm", "49 cm"], "answer": "28 cm"},
    {"question": "The probability of getting a head when a coin is tossed:", "options": ["0", "1/2", "1/3", "1"], "answer": "1/2"},
    {"question": "The ratio of 2 hours to 30 minutes is:", "options": ["1:4", "2:1", "4:1", "1:2"], "answer": "4:1"},
    {"question": "Which is the largest prime number below 20?", "options": ["17", "19", "13", "11"], "answer": "19"},
    {"question": "The area of a circle of radius 7 cm is (π=22/7):", "options": ["132 cm²", "144 cm²", "154 cm²", "160 cm²"], "answer": "154 cm²"},
    {"question": "Solve: 15 × 12 ÷ 6", "options": ["25", "30", "35", "40"], "answer": "30"},
    {"question": "The next number in 5, 10, 20, 40, ?", "options": ["50", "60", "80", "100"], "answer": "80"},
    {"question": "The sum of angles in a triangle is:", "options": ["180°", "90°", "360°", "270°"], "answer": "180°"},
    {"question": "If a=b=2, find a² + b²", "options": ["2", "4", "8", "6"], "answer": "8"},
    {"question": "Which is an odd prime number?", "options": ["2", "4", "9", "5"], "answer": "5"},
    {"question": "Cube root of 512 is:", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "If 3x = 12, x =", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "50% of 60 + 25% of 80 =", "options": ["55", "60", "65", "70"], "answer": "55"},
    {"question": "The next term in 1, 4, 9, 16, ?", "options": ["20", "25", "36", "30"], "answer": "25"},
    {"question": "5 × 5 + 5 =", "options": ["25", "30", "35", "40"], "answer": "30"},
    {"question": "The simple interest on Rs. 500 at 10% for 3 years is:", "options": ["50", "100", "150", "200"], "answer": "150"},
    {"question": "If a train moves at 60 km/hr, distance in 2 hrs =", "options": ["100", "120", "130", "150"], "answer": "120"},
    {"question": "Next in series 3, 6, 9, 12, ?", "options": ["14", "15", "16", "18"], "answer": "15"},
    {"question": "LCM of 8 and 12 is:", "options": ["24", "36", "48", "60"], "answer": "24"},
    {"question": "HCF of 12 and 18 is:", "options": ["2", "3", "6", "12"], "answer": "6"},
    {"question": "Solve: 2x + 3 = 11", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "The next term in 2, 4, 8, 16, ?", "options": ["18", "20", "24", "32"], "answer": "32"},
    {"question": "Area of a rectangle with length 5 and breadth 4:", "options": ["9", "10", "20", "25"], "answer": "20"},
    {"question": "7² - 3² =", "options": ["10", "28", "40", "49"], "answer": "40"},
    {"question": "50 ÷ 5 + 10 =", "options": ["15", "20", "25", "30"], "answer": "20"},
    {"question": "25% of 80 =", "options": ["15", "20", "25", "30"], "answer": "20"},
    {"question": "Simplify: 6 × (2 + 3)", "options": ["20", "25", "30", "36"], "answer": "30"},
    {"question": "If x/2 = 5, x =", "options": ["5", "8", "10", "12"], "answer": "10"},
    {"question": "Next in series: 10, 20, 30, ?", "options": ["40", "50", "60", "70"], "answer": "40"},
    {"question": "Sum of first 5 natural numbers:", "options": ["10", "15", "20", "25"], "answer": "15"},
    {"question": "6 × 7 =", "options": ["42", "36", "40", "48"], "answer": "42"},
    {"question": "Square of 9 is:", "options": ["18", "72", "81", "90"], "answer": "81"},
    {"question": "Simplify: 8 ÷ 2 × 4", "options": ["12", "16", "24", "32"], "answer": "16"},
    {"question": "Next prime number after 17:", "options": ["18", "19", "20", "21"], "answer": "19"},
    {"question": "Cube of 3 is:", "options": ["6", "9", "27", "81"], "answer": "27"},
    {"question": "12 × 12 =", "options": ["124", "144", "154", "164"], "answer": "144"},
]

def aptitude_test():
    st.title("📝 Aptitude Test")

    student_name = st.text_input("Enter Your Name", value=st.session_state.get("student_name", ""))

    # Randomly select 20 questions from bank
    QUESTIONS = random.sample(QUESTION_BANK, 20)

    # Save current questions in session state to prevent reshuffling on re-render
    if "current_questions" not in st.session_state:
        st.session_state["current_questions"] = QUESTIONS
    else:
        QUESTIONS = st.session_state["current_questions"]

    # Form for questions
    with st.form("aptitude_form"):
        for i, q in enumerate(QUESTIONS, start=1):
            st.radio(
                f"Q{i}. {q['question']}",
                q["options"],
                key=f"q{i}",
                index=None
            )
        submitted = st.form_submit_button("Submit Test")

    if submitted:
        if not student_name:
            st.error("⚠️ Please enter your name before submitting.")
            return

        score = 0
        wrong_questions = []
        unanswered_count = 0

        for i, q in enumerate(QUESTIONS, start=1):
            user_ans = st.session_state.get(f"q{i}", None)
            if user_ans is None:
                unanswered_count += 1
            elif user_ans == q["answer"]:
                score += 1
            else:
                wrong_questions.append((i, q["question"], user_ans, q["answer"]))

        total_questions = len(QUESTIONS)
        percentage = (score / total_questions) * 100
        unanswered = total_questions - score - len(wrong_questions)

        # Save in session state for Data Entry
        st.session_state["student_name"] = student_name
        st.session_state["etest_p"] = percentage

        # Display results
        st.subheader(f"📊 Test Result for {student_name}")
        st.write(f"✅ Correct Answers: {score}/{total_questions}")
        st.write(f"❌ Wrong Answers: {len(wrong_questions)}")
        st.write(f"🕒 Not Answered: {unanswered}")
        st.write(f"📈 Percentage: {percentage:.2f}%")

        # Pie chart
        labels = ['Correct', 'Wrong', 'Not Answered']
        sizes = [score, len(wrong_questions), unanswered]
        colors = ['#4CAF50', '#FF5252', '#FFC107']

        fig, ax = plt.subplots(figsize=(1.5, 1.5))
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 9})
        ax.axis('equal')
        ax.set_title("Test Result Overview", fontsize=10)
        st.pyplot(fig, use_container_width=False)

        # Wrongly answered questions
        if wrong_questions:
            st.subheader("❌ Wrongly Answered Questions")
            for q_no, ques, user_ans, correct_ans in wrong_questions:
                st.write(f"Q{q_no}: {ques}")
                st.write(f"   - Your Answer: {user_ans}")
                st.write(f"   - Correct Answer: ✅ {correct_ans}")
                st.write("---")

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Go Back to Home", key="apt_home"):
            st.session_state["page"] = "Home"
            st.session_state.pop("current_questions", None)
    with col2:
        if st.button("📊 Go to Placement Prediction", key="apt_data"):
            st.session_state["page"] = "Data Entry"
            st.session_state.pop("current_questions", None)
