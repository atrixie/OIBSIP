from tkinter import *
from database import get_statistics


def show_statistics():

    stats = get_statistics()

    total = stats[0]

    avg = stats[1]
    highest = stats[2]
    lowest = stats[3]

    window = Tk()

    window.title("BMI Statistics")
    window.geometry("350x300")

    Label(
        window,
        text="BMI Statistics",
        font=("Arial",18,"bold")
    ).pack(pady=20)

    Label(
        window,
        text=f"Total Records : {total}",
        font=("Arial",12)
    ).pack(pady=8)

    Label(
        window,
        text=f"Average BMI : {round(avg,2) if avg else 0}",
        font=("Arial",12)
    ).pack(pady=8)

    Label(
        window,
        text=f"Highest BMI : {highest if highest else 0}",
        font=("Arial",12)
    ).pack(pady=8)

    Label(
        window,
        text=f"Lowest BMI : {lowest if lowest else 0}",
        font=("Arial",12)
    ).pack(pady=8)

    window.mainloop()