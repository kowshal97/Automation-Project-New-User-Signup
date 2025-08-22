 🧪 AutomationExercise — New User Signup (Selenium + Python)

<!-- Replace YOUR-USERNAME/YOUR-REPO everywhere below -->
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](#)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?logo=selenium)](#)
[![webdriver--manager](https://img.shields.io/badge/webdriver--manager-Installed-informational)](#)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/YOUR-USERNAME/YOUR-REPO)](#)
[![Issues](https://img.shields.io/github/issues/YOUR-USERNAME/YOUR-REPO)](https://github.com/YOUR-USERNAME/YOUR-REPO/issues)
[![PRs](https://img.shields.io/github/issues-pr/YOUR-USERNAME/YOUR-REPO)](https://github.com/YOUR-USERNAME/YOUR-REPO/pulls)

Automates **new user registration** on [AutomationExercise.com](https://automationexercise.com) using Selenium WebDriver (Python).  
The flow validates homepage load, fills the signup form, completes detailed registration, and submits the account creation.

---

## ✨ Features

- ✅ **Homepage verification**
- 📝 **Signup form autofill** (name + email)
- 📋 **Full registration** (gender, password, DOB, address, preferences)
- ⏳ **Stable waits** via `WebDriverWait`
- 🧰 Uses `webdriver-manager` to auto-install ChromeDriver

---

## 🧱 Tech Stack

- Python 3.10+
- Selenium 4.x
- webdriver-manager
- Google Chrome (or Chromium)

---

## 📦 Setup

```bash
# 1) Create & activate a virtual env (optional but recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 2) Install dependencies
pip install selenium webdriver-manager
Heads-up: Make sure Google Chrome is installed. The script uses webdriver-manager to fetch the correct driver automatically.

🚀 Run
If your file name contains spaces, keep the quotes:

bash
Copy
Edit
python "New user signup with best practice.py"
Want headless mode? Add this small tweak inside setup_browser():

python
Copy
Edit
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
🔧 Customize Test Data
Open the script and update these inputs as you like (name, email, password, DOB, address, etc.).
Use a unique email each run to avoid “email already exists” errors.

Name / Email (signup page)

Password / DOB

Newsletter & offers checkboxes

Address (first/last name, company, street, country, state, city, zip, mobile)

🗂️ Project Structure
csharp
Copy
Edit
.
├─ New user signup with best practice.py   # Main automation script
├─ README.md                               # This file
└─ LICENSE                                 # (Optional) MIT or your chosen license
🧪 What It Does (Step-by-step)
Open site and verify homepage banner is visible

Navigate to Login/Signup

Fill name + email then continue

Complete registration form (gender, password, DOB, address, preferences)

Submit and print a success message in the console

🛠 Troubleshooting
Chrome/driver mismatch: Update Chrome to latest or reinstall webdriver-manager cache:

bash
Copy
Edit
pip install --upgrade webdriver-manager
Element not found / timing issues: Network delays happen—raise waits (e.g., WebDriverWait(..., 20)).

Email already exists: Use a fresh email each run (e.g., me+<timestamp>@example.com if your provider supports aliases).

🤝 Contributing
Fork the repo

Create a branch: git checkout -b feat/improvement

Commit changes: git commit -m "Add X"

Push: git push origin feat/improvement

Open a Pull Request

