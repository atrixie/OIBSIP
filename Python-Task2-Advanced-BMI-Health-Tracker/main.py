from graph import show_graph
from stats import show_statistics
from export import export_csv
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from bmi import calculate_bmi, get_category
from database import create_table, insert_record, get_records

create_table()

root = tk.Tk()
root.title("Advanced BMI Health Tracker")
root.geometry("700x760")

root.configure(bg="#F4F6F8")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

title = tk.Label(
    root,
    text="Advanced BMI Health Tracker",
    font=("Segoe UI", 22, "bold"),
    bg="#F4F6F8",
    fg="#2C3E50"
)
title.pack(pady=20)

frame = ttk.Frame(root, padding=25)
frame.pack(fill="both", padx=20)

ttk.Label(frame, text="Name").pack(anchor="w")
name_entry = ttk.Entry(frame, width=40)
name_entry.pack(pady=5)

ttk.Label(frame, text="Weight (kg)").pack(anchor="w")
weight_entry = ttk.Entry(frame, width=40)
weight_entry.pack(pady=5)

ttk.Label(frame, text="Height (m)").pack(anchor="w")
height_entry = ttk.Entry(frame, width=40)
height_entry.pack(pady=5)

bmi_label = tk.Label(
    frame,
    text="BMI : --",
    font=("Segoe UI", 18, "bold"),
    bg="#F4F6F8"
)
bmi_label.pack(pady=15)

category_label = tk.Label(
    frame,
    text="Category : --",
    font=("Segoe UI", 16),
    bg="#F4F6F8"
)
category_label.pack()

tip_label = tk.Label(
    frame,
    text="",
    wraplength=500,
    justify="center",
    font=("Segoe UI", 11),
    bg="#F4F6F8"
)
tip_label.pack(pady=20)
scale_title = tk.Label(
    frame,
    text="BMI Classification",
    font=("Segoe UI", 13, "bold"),
    bg="#F4F6F8"
)

scale_title.pack(pady=(10, 5))

scale = tk.Label(
    frame,
    text=(
        "🔵 Underweight : < 18.5\n"
        "🟢 Normal : 18.5 - 24.9\n"
        "🟠 Overweight : 25 - 29.9\n"
        "🔴 Obese : 30+"
    ),
    justify="left",
    font=("Segoe UI", 10),
    bg="#F4F6F8"
)

scale.pack()


def clear_fields():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    bmi_label.config(text="BMI : --")
    category_label.config(text="Category : --", fg="black")
    tip_label.config(text="")


def calculate():

    name = name_entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

    except ValueError:
        messagebox.showerror("Error", "Weight and Height must be numbers.")
        return

    if weight <= 0 or height <= 0:
        messagebox.showerror("Error", "Values must be greater than zero.")
        return

    if weight < 10 or weight > 300:
        messagebox.showerror("Error", "Weight must be between 10 and 300 kg.")
        return

    if height < 0.5 or height > 2.5:
        messagebox.showerror("Error", "Height must be between 0.5 and 2.5 meters.")
        return

    bmi = calculate_bmi(weight, height)

    category, tip, color = get_category(bmi)

    bmi_label.config(text=f"BMI : {bmi}")

    category_label.config(
        text=f"Category : {category}",
        fg=color
    )

    tip_label.config(text=tip)

    insert_record(
        name,
        weight,
        height,
        bmi,
        category,
        datetime.now().strftime("%d-%m-%Y %H:%M")
    )

    messagebox.showinfo("Saved", "BMI record saved successfully.")


def show_history():

    history = tk.Toplevel(root)
    history.title("BMI History")
    history.geometry("900x450")

    tree = ttk.Treeview(
        history,
        columns=(
            "Name",
            "Weight",
            "Height",
            "BMI",
            "Category",
            "Date"
        ),
        show="headings"
    )

    headings = [
        "Name",
        "Weight",
        "Height",
        "BMI",
        "Category",
        "Date"
    ]

    for heading in headings:
        tree.heading(heading, text=heading)
        tree.column(heading, width=140)

    tree.pack(fill="both", expand=True)

    for row in get_records():
        tree.insert("", tk.END, values=row)


button_frame = ttk.Frame(frame)
button_frame.pack(pady=20)

ttk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate
).grid(row=0,column=0,padx=5,pady=5)

ttk.Button(
    button_frame,
    text="History",
    command=show_history
).grid(row=0,column=1,padx=5,pady=5)

ttk.Button(
    button_frame,
    text="Statistics",
    command=show_statistics
).grid(row=0,column=2,padx=5,pady=5)

ttk.Button(
    button_frame,
    text="Trend Graph",
    command=show_graph
).grid(row=1,column=0,padx=5,pady=5)

ttk.Button(
    button_frame,
    text="Export CSV",
    command=export_csv
).grid(row=1,column=1,padx=5,pady=5)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear_fields
).grid(row=1,column=2,padx=5,pady=5)

root.mainloop()