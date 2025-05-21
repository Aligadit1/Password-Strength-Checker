# 🔐 Password Strength Meter

A simple and interactive web application built with **Python** and **Streamlit** that checks the strength of a password and gives real-time feedback with helpful suggestions for improvement.

## 🚀 Features

- ✅ **Real-time password evaluation**
- 📛 **Blacklist detection** for common weak passwords like `123456`, `password`, `admin`, etc.
- 🔠 **Character validation**:
  - Minimum 8 characters
  - At least one uppercase and one lowercase letter
  - At least one digit
  - At least one special character (`!@#$%^&*`)
- 📊 **Scoring system**:
  - Scores password on a scale of 0–6
  - Categorizes as **Strong**, **Moderate**, or **Weak**
- 💬 **User feedback and suggestions** for improvement

## 🧰 Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Regular Expressions (re module)](https://docs.python.org/3/library/re.html)

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/password-strength-meter.git
   cd password-strength-meter
   
2. Install dependencies
   ```bash
   pip install streamlit
   
▶️ Usage
Run the app locally with the following command:
```bash
streamlit run app.py

Then open your browser and go to:
http://localhost:8501

🙌 Acknowledgments
Inspired by common password validation practices and designed for educational purposes.

