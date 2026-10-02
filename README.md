# BancoPy

BancoPy is a simple banking system developed in Python as part of a final course project.

The application runs in the terminal and allows users to create bank accounts, make deposits and withdrawals, transfer money between accounts, and list registered accounts.

## Features

- Create clients and bank accounts
- Automatic client code generation
- Automatic account number generation
- Deposit money into an account
- Withdraw money from an account
- Transfer money between accounts
- Search accounts by account number
- List all registered accounts
- Validate deposits and withdrawals
- Account balance and credit limit management
- Currency and date formatting
- Interactive terminal menu

## Project Structure

```text
BancoPy/
├── models/
│   ├── __init__.py
│   ├── account.py
│   └── client.py
├── utils/
│   └── helper.py
├── bank.py
├── test.py
├── README.md
└── .gitignore
```

## Main Classes

### Client

The `Client` class represents a bank customer and stores:

- Client code
- Name
- Email
- CPF
- Birth date
- Registration date

Each client receives an automatically generated code.

### Account

The `Account` class represents a bank account and stores:

- Account number
- Client
- Balance
- Credit limit
- Total available balance

Each account receives an automatically generated account number.

The class also contains the main banking operations:

- `deposit()`
- `withdraw()`
- `transfer()`

## Banking Operations

### Deposit

Adds a positive value to the account balance.

### Withdraw

Withdraws money if the requested value is positive and does not exceed the total available balance.

### Transfer

Transfers money from one account to another.

The transfer is completed only if the withdrawal from the source account succeeds.

## Main Menu

The application provides the following options:

```text
=== BANCOPY ===
1 - Create account
2 - Deposit
3 - Withdraw
4 - Transfer
5 - List accounts
6 - Exit
```

## Helper Functions

The `helper.py` module contains functions used for:

- Converting strings to dates
- Converting dates to strings
- Formatting monetary values

## Concepts Practiced

This project was developed to practice:

- Python
- Object-Oriented Programming
- Classes and objects
- Encapsulation
- Properties
- Type Hinting
- Functions
- Lists
- Loops and conditional statements
- Modules and packages
- Date manipulation
- String formatting
- Input validation
- Code organization

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Enter the project directory:

```bash
cd BancoPy
```

Run the application:

```bash
python bank.py
```

## Project Status

Completed and functional.
