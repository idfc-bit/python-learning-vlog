# ==============================
# MINI PYTHON CONSOLE APP
# ==============================

import time

users = {}

def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def create_user():
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))
    users[name] = age
    slow_print(f"✅ User {name} added successfully!")

def show_users():
    if not users:
        slow_print("❌ No users found.")
        return

    slow_print("📋 Registered Users:")
    for name, age in users.items():
        print(f" - {name} ({age} years old)")

def average_age():
    if not users:
        slow_print("❌ No users to calculate average.")
        retu