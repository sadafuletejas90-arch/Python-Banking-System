# =====================================
# Project Name: Banking Management System
# Author: Tejas Sadafule
# Language: Python
# Description: A simple banking application
# Version: 1.0
# =====================================

# Initial account balance
balance = 0

print("===== Welcome to Python Banking System ===== - Python-Banking-System.py:12")

while True:
    print("\n1. Check Balance - Python-Banking-System.py:15")
    print("2. Deposit Money - Python-Banking-System.py:16")
    print("3. Withdraw Money - Python-Banking-System.py:17")
    print("4. Exit - Python-Banking-System.py:18")

    choice = input("Enter your choice: ")

    # Check balance
    if choice == "1":
        print(f"Your current balance is: ₹{balance} - Python-Banking-System.py:24")

    # Deposit money
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))

        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully. - Python-Banking-System.py:32")
        else:
            print("Please enter a valid amount. - Python-Banking-System.py:34")

    # Withdraw money
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully. - Python-Banking-System.py:42")
        else:
            print("Insufficient balance. - Python-Banking-System.py:44")

    # Exit application
    elif choice == "4":
        print("Thank you for using the Banking System. - Python-Banking-System.py:48")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again. - Python-Banking-System.py:53")