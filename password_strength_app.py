import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔴 At least 8 characters required.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("🔴 Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("🔴 Include at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("🔴 Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("🔴 Include at least one special character (!@#$%).")

    # Evaluate strength level
    if strength == 5:
        level = "🟢 Very Strong"
    elif strength == 4:
        level = "🟢 Strong"
    elif strength == 3:
        level = "🟡 Moderate"
    elif strength == 2:
        level = "🔴 Weak"
    else:
        level = "🔴 Very Weak"

    return level, feedback

# Streamlit UI
st.title("🔐 Password Strength Checker")
st.write("Enter a password below to check how strong it is.")

password = st.text_input("🔑 Enter your password", type="password")

if password:
    level, feedback = check_password_strength(password)
    st.markdown(f"### Strength: {level}")

    if feedback:
        st.markdown("#### 🔧 Suggestions to Improve:")
        for tip in feedback:
            st.markdown(f"- {tip}")
    else:
        st.success("✅ Great! Your password is very secure.")
