# 💳 PAYSRM ATM BANKING SYSTEM

> A fully functional GUI-based ATM Banking System built with **Python (Tkinter)** and integrated with **MySQL** for real-time banking operations like Withdraw, Deposit, Mini Statement, and Balance Inquiry. 🏦

---

## 📌 Project Features

* 🧑‍💼 **User Registration & Login** (with password security)
* 🏦 **Withdraw / Deposit** money with UI-based interaction
* 📄 **PDF Receipt Generation** for all transactions
* 📊 **Mini Statement Report** using **tkcalendar** + **FPDF**
* 🔐 **Change Password** option
* 🔀 **Database Integration** with **MySQL**
* 📦 Stores transactions in `.csv` files for audit

---

## 🛠️ Built With

| Category       | Tools Used                                                 |
| -------------- | ---------------------------------------------------------- |
| GUI            | `Tkinter`, `tkcalendar`                                    |
| Database       | `MySQL` (`mysql.connector`)                                |
| Data Handling  | `CSV`, `Pandas`                                            |
| PDF Export     | `FPDF`                                                     |
| Image Handling | `Pillow (PIL)`                                             |
| Language       | `Python`                                                   |
| OS             | `Windows` (with absolute file paths used for icons/images) |

---

## ⚙️ Modules & Structure

```bash
ATM GUI PROJECT FINAL.py
│
├── StartPage        → Welcome screen with login/logout options
├── MenuPage         → Main menu with action buttons
├── WithdrawPage     → Withdraw fixed/custom amounts
├── DepositPage      → Deposit screen
├── BalancePage      → Displays current account balance
├── MinistatementPage→ Date-range based mini-statement as PDF
├── InfoPage         → View account name & ID; change password
├── Auth System      → Register, Login, Password verification
├── Database         → MySQL (Table: paysrm, Fields: accid, name, password, balance)
└── CSV Transactions → Transactions saved as .csv per user
```

---

## 🎯 How It Works

1. **Register** with name and password (Account ID auto-generated)
2. **Login** using your credentials
3. Access:

   * 💸 Withdraw (pre-set or custom)
   * 💰 Deposit
   * 📊 Balance Inquiry
   * 📄 Mini-statement (with date picker)
4. PDFs are generated & opened after each transaction

---

## 📸 Screenshots

> *Images and screenshots are added to the mail root of this repository*
---

## ⚠️ Requirements

* Python 3.x
* MySQL Server
* Required packages:

  ```bash
  pip install mysql-connector-python tkcalendar fpdf pandas pillow
  ```

---

## 🔐 Database Setup

1. Run MySQL locally
2. Create a database called: `paysrm`
3. The script automatically creates:

   * Table `paysrm (accid INT, name VARCHAR, password CHAR, balance CHAR)`
4. No SQL file is needed — it self-generates tables if missing.

---

## 📂 File Storage

* All PDFs (`Withdraw`, `Deposit`, `Ministatement`) saved and auto-opened
* All transactions stored in CSV files named as: `{account_id}.csv`

---

## 🎓 Educational Scope

This project is ideal for:

* School level , Higher secondry students
* Learning **Tkinter GUI**
* Practicing **MySQL CRUD**
* PDF & CSV file operations
* Handling user sessions and multiple screens in a single file

---

## 👤 Author

**Rahul Krishna J**

* LinkedIn: [linkedin.com/in/rahulkrishna-j](https://linkedin.com/in/rahulkrishna-j)
* GitHub: [JRK-007](https://github.com/JRK-007)
* Mail: [rahulkrishnaofficial@gmail.com](mailto:rahulkrishnaofficial@gmail.com)

---
## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
---

## 🌟 Star This Repo

## 🤝 Contributing

Feel free to fork this repo and open a pull request if you'd like to:

- Improve GUI design
- Add password encryption
- Add SQL file generator script

All contributions are welcome!

---

## 🐞 Known Issues

- GUI may appear stretched on certain high-resolution displays.
- PDF files overwrite if same date is selected multiple times.
- Account registration does not validate duplicate usernames (yet).

---
## 🚧 Future Enhancements

- 🔐 Add OTP/email-based 2FA login system
- 📊 Visual dashboard for admin analytics
- 🌍 Web version using Flask or Django
- 📱 Mobile-friendly version using Kivy

---

If this project helped you or inspired you, please ⭐ star it on GitHub — it motivates me to build more such projects!

NOTE : For further details about this project verify pdf document named "User Instructions for Running the ATM System Code"

---
