# 🤖 Automation Project – New User Signup

![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Automation](https://img.shields.io/badge/Tool-Selenium-blue)
![Language](https://img.shields.io/badge/Language-Python-yellow)
![Testing](https://img.shields.io/badge/Type-UI%20Automation-red)

---

## 📌 Overview
This project automates the **new user registration** workflow on **AutomationExercise.com** using **Selenium WebDriver (Python)**.  
The script validates page loading, fills the signup form, completes the detailed registration page, and submits the account creation request.

---

## 🚀 Features
- 🌐 **Homepage Verification** — confirms the application loads successfully  
- 📝 **Signup Form Automation** — auto-fills name & email  
- 📋 **Detailed Registration** — gender, password, DOB, address, preferences  
- 🔐 **Form Submission** — creates a new account with basic validations  
- ⏳ **Explicit Waits** — stable execution using `WebDriverWait`

---

## 📂 Repository Contents
- `New user signup with best practice.py` — **main automation script**
- `README.md` — **documentation** (this file)

---

## 🛠️ Tech Stack
- 🐍 **Python 3**
- 🌐 **Selenium WebDriver**
- 💻 **ChromeDriver** (managed via `webdriver-manager`)

---

## ⚙️ How to Run

📦 **Install dependencies**
```bash
pip install selenium webdriver-manager

## ▶️ Run the script
```bash
python "New user signup with best practice.py"

👉 Chrome will launch and perform the signup automatically.
