import re
import streamlit as st

# title
st.title("🔐 Password Strength Meter")
st.subheader("Check Your Password Strength")

#  function to check password strength
def check_password_strength(password):

    # score for giving results for the password 
    score = 0 

    # Blacklisted password
    blacklist = ["password", "password123", "123456", "12345678", "qwerty", "admin", "letmein", "welcome"]
    if password:
        # this if is ensuring that all the if else work if the password exist  
        if password not in blacklist:
            # length of the password
            if len(password) >= 8:
                score += 1
            else:
                st.write("❌ Password should be at least 8 characters long.")
            
            # Upper and lowercase checker 
            if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
                score += 2  
            else:
                st.write("�� Password should contain at least one uppercase and one lowercase letter.")   

            # digit checker 
            if re.search(r"\d", password):
                score += 1  
            else:
                st.write("�� Add atleast one digit")  

            # special character checker  
            if re.search(r"[!@#$%^&*]", password):
                score += 2
            else:
                st.write("�� Add atleast one special character (!@#$%^&*).") 

        # Strength Rating
            if score == 6:
                st.warning("✅ Strong Password!")
            elif score == 5:
                st.warning("⚠️ Moderate Password - Consider adding more security features.")
            else:
                st.warning("❌ Weak Password - Improve it using the suggestions above.")
        else:
            st.warning("❌ This password is too common! Choose a stronger one.")
# Getting user input    
password = st.text_input("Enter your password")
check_password_strength(password)