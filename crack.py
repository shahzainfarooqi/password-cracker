import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔒 Password Strength Checker")

st.markdown("""
### Welcome to the Ultimate Password Strength Checker! ✋

Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.  
We'll provide helpful tips to create a **Strong Password** 🔐.
""")

# Input
password = st.text_input("Enter your password", type="password")
feedback = []
score = 0

# Evaluate password
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*)")

    # Strength labels
    strength_label = ""
    if score == 4:
        strength_label = "💪 Very Strong"
    elif score == 3:
        strength_label = "🔐 Strong"
    elif score == 2:
        strength_label = "⚠️ Moderate"
    else:
        strength_label = "❌ Weak"

    # Display results
    st.subheader("🔒 Password Strength:")
    st.write(strength_label)

    # Show progress bar using Python only
    st.progress(score / 4)

    st.subheader("🔍 Password Feedback:")
    if feedback:
        for item in feedback:
            st.write(item)
    else:
        st.success("✅ Your password meets all recommended criteria!")