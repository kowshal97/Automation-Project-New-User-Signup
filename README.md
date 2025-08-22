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
- [New user signup with best practice.py](https://github.com/kowshal97/Automation-Project-New-User-Signup/raw/main/New%20user%20signup%20with%20best%20practice.py)


## 🔧 Customize Test Data

- Open the script and update these inputs as you like (name, email, password, DOB, address, etc.).
- Use a unique email each run to avoid “email already exists” errors.
- Name / Email (signup page)
- Password / DOB
- Newsletter & offers checkboxes
- Address (first/last name, company, street, country, state, city, zip, mobile)

---

## 🛠 Troubleshooting

- Chrome/driver mismatch: Update Chrome to latest or reinstall webdriver-manager cache:
- pip install --upgrade webdriver-manager
- Element not found / timing issues: Network delays happen—raise waits (e.g., WebDriverWait(..., 20)).
- Email already exists: Use a fresh email each run (e.g., me+<timestamp>@example.com if your provider supports aliases).

---

## 🛠️ Tech Stack
- 🐍 **Python 3**
- 🌐 **Selenium WebDriver**
- 💻 **ChromeDriver** (managed via `webdriver-manager`)

---

## 📸 Demo Flow

- Opens AutomationExercise.com
- Navigates to Signup/Login page
- Fills in user details, address, and preferences
- Submits the registration form
- Confirms account creation

---

## 🎯 Key Learnings

- ✅ Automated end-to-end signup flow with Selenium
- ✅ Applied best practices: waits, validations, reusable functions
- ✅ Enhanced Python scripting & testing skills

---

## 👤 Author  
**Kowshal Sugunarajah**  
🎓 Postgraduate Student – Cloud Computing @ Durham College  
💼 Ex-QA at Amazon | ☁️ Cloud Enthusiast | 🗄️ Database & Automation Tester  











