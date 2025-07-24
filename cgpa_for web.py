import streamlit as st

def grade(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    else:
        return 0

st.title("Student CGPA Calculator (VTU)")

name = st.text_input("Enter your name")
usn = st.text_input("Enter your USN")
sem = st.number_input("In which semester you are?", min_value=1, max_value=8, step=1)
cycle = st.radio("Enter the cycle name", ['P', 'C'])

if sem in [1, 2] and name and usn and cycle:
    st.subheader("Enter Internal and End-Sem Marks for Each Subject")

    subjects = [
        ("Maths", 4),
        ("Physics/Chemistry", 4),
        ("ESC Subject", 3),
        ("Waste Mgmt / CAED", 3),
        ("Programming", 3),
        ("English", 1),
        ("IDT/Indian Constitution", 1),
        ("Kannada/SFH", 1)
    ]

    grades = []
    total_credits = 0
    total_weighted_points = 0

    for subj, credit in subjects:
        internal = st.number_input(f"{subj} - Internal Marks", min_value=0, max_value=50)
        end_sem = st.number_input(f"{subj} - End Sem Marks", min_value=0, max_value=100)
        total = internal + (end_sem // 2)
        gp = grade(total)
        grades.append(gp)
        total_weighted_points += gp * credit
        total_credits += credit

    if st.button("Calculate CGPA"):
        cgpa = total_weighted_points / total_credits
        st.markdown("---")
        st.subheader("🎓 Student Exam Details")
        st.write(f"**Name:** {name}")
        st.write(f"**USN:** {usn}")
        st.write(f"**Cycle:** {cycle}")
        st.success(f"**CGPA:** {cgpa:.2f}")
