# Expense Tracker

**Organization:** WeIntern Pvt Ltd  
**Task:** Week 1 - Task 2

---

## Objective
Console-based Expense Tracker to record and review daily expenses with file persistence.

---

## Features
- Add new expense
- View all expenses
- Filter by category
- Calculate total expenses
- Generate summary report
- Save data to CSV file

---

## Technologies
- Python 3.x
- CSV File Handling
- Exception Handling

---

## Folder Structure
```
expense_tracker/
├── main.py           # Menu & main logic
├── file_handler.py   # Save & load expenses
├── expenses.csv      # Data storage
└── README.md
```

---

## How to Run
```bash
cd expense_tracker
python main.py
```

---

## Sample Output
```
===== Expense Tracker =====
1. Add Expense
2. View All Expenses
3. Summary Report
4. Exit

Enter your choice: 3

===== Expense Summary =====
Total Entries: 12
Total Spent: 5400.00
Highest Expense: Travel - 1200.00
```

---

## Expense Fields
| Field | Example |
|---|---|
| Date | 2024-01-15 |
| Category | Food / Travel |
| Description | Lunch at cafe |
| Amount | 250.00 |

---

## Author
**Name:** Kunjal Dodiya
**Intern at:** WeIntern Pvt Ltd