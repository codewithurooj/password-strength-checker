import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain numbers.")

    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain special characters (!@#$%&*).")

    return score, feedback

st.set_page_config(page_title="🔒 Password Strength Checker", page_icon=":lock:" )
st.title("Password Strength Checker 🔒")
st.markdown("""
## Welcome to the best password strength evaluator🎉 !
Use this tool to check the strength of your password and get suggestions to make
 it more secure. We will give you helpful tips to create a **strong password**.
""")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)

    if score == 4:
        st.success("✅ Password is strong! 🎉")
    elif score == 3:
        st.warning("✅ Password is medium strong. It can be improved.")
    else:
        st.error("❌ Password is weak. It can be improved.")
    
    with st.expander("Improvement Suggestions"):
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to check its strength.")
