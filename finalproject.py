import tkinter as tk
from datetime import date

def calculate_age():
   dob = entry_date.get()
   try:
       dob_date = date.fromisoformat(dob)
       today = date.today()

       years = today.year - dob_date.year
       months = today.month - dob_date.month
       days = today.day - dob_date.day

       if days < 0:
           months -= 1
           days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days
       if months < 0:
           years -= 1
           months += 12

       quotes = [
           "Every day is a fresh start.",
           "Dream big and stay curious.",
           "Learn, play, and grow every day.",
           "Your potential is limitless.",
           "Build habits that shape your future.",
           "Consistency creates success.",
           "Your best years are being built now.",
           "Stay strong, stay focused.",
           "Wisdom grows with experience.",
           "Your journey inspires others.",
           "Age is proof of a life well lived.",
           "Kill Yourself"
       ]

       index = min(years // 10, 10)
       quote = quotes[index]

       label_result.config(
           text=f"You are {years} years, {months} months, and {days} days old.\n\n{quote}"
       )
   except ValueError:
       label_result.config(text="Please enter a valid date in YYYY-MM-DD format.")

app = tk.Tk()
app.title("Age Calculator")
app.geometry("450x360")
app.configure(bg="#1e1e2e")

title = tk.Label(
    app,
    text="Age Calculator",
    font=("Segoe UI", 20, "bold"),
    fg="#ffffff",
    bg="#1e1e2e"
)
title.pack(pady=20)

label_date = tk.Label(
    app,
    text="Date of Birth (YYYY-MM-DD)",
    font=("Segoe UI", 11),
    fg="#cdd6f4",
    bg="#1e1e2e"
)
label_date.pack(pady=5)

entry_date = tk.Entry(
    app,
    font=("Segoe UI", 12),
    width=22,
    justify="center",
    bd=0
)
entry_date.pack(pady=10, ipady=6)

button_calculate = tk.Button(
    app,
    text="Calculate Age",
    font=("Segoe UI", 12, "bold"),
    bg="#89b4fa",
    fg="#1e1e2e",
    activebackground="#74c7ec",
    bd=0,
    width=18,
    command=calculate_age
)
button_calculate.pack(pady=15)

label_result = tk.Label(
    app,
    text="",
    font=("Segoe UI", 12),
    fg="#a6e3a1",
    bg="#1e1e2e",
    wraplength=380,
    justify="center"
)
label_result.pack(pady=10)

app.mainloop()
