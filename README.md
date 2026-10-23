# Shared Trip Expense Settler 💸

A simple Python web application that helps friends manage shared trip expenses, calculate individual balances, and settle debts with fewer transactions.

## 📌 Project Overview

When friends travel together, keeping track of who paid for what can become confusing. The Shared Trip Expense Settler makes expense sharing easier by recording payments, splitting costs among participants, and calculating who owes money to whom.

## ✨ Features

- **Participant Management** — Add participants to a trip.
- **Expense Tracking** — Record expenses, including the payer, amount, and participants sharing the cost.
- **Equal Expense Splitting** — Divide shared expenses among selected participants.
- **Balance Calculation** — Calculate how much each participant owes or should receive.
- **Suggested Settlements** — Generate suggested transfers to simplify repayment.
- **Local Data Storage** — Save application data using JSON files.
- **Web Interface** — Interact with the application through a browser.

## 🛠️ Technologies Used

- Python
- HTML
- JSON
- Python HTTP Server

## 📂 Project Structure

```text
daa_project_assignment/
├── common.py
├── 04_expense_settler/
│   └── app.py
└── README.md
```

*The structure above shows the main files; include any additional files your actual project uses.*

## 🚀 How to Run Locally

### Prerequisites

- Python 3 installed
- A web browser

### Steps

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd daa_project_assignment
   ```

3. Run the application:

   ```bash
   python3 04_expense_settler/app.py
   ```

4. Open the local URL printed in the terminal in your browser.

Keep the terminal open while using the application.

## 🧮 Example

Suppose three friends share expenses:

- Asha pays ₹900 for a taxi shared by all three.
- Balu pays ₹300 for lunch shared by Balu and Chitra.

The application calculates each participant's net balance and suggests transfers to settle the expenses.

## 🎯 Project Objectives

- Practice Python programming.
- Apply basic data handling and expense calculations.
- Understand client-server communication.
- Use JSON for local data persistence.
- Build a practical application for managing shared expenses.

## 🔮 Future Improvements

- Edit and delete recorded expenses.
- Add persistent cloud storage for deployed use.
- Improve the user interface for mobile devices.
- Add secure user accounts and separate trips.
- Support configurable expense-splitting methods.

## 👩‍💻 Project Information

**Project Name:** Shared Trip Expense Settler  
**Category:** Python Web Application  
**Purpose:** Educational project for expense management.

---

*Built as a learning project to make sharing trip expenses simpler.*
