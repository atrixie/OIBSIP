import csv
from tkinter import messagebox
from database import get_records


def export_csv():

    data = get_records()

    with open("BMI_History.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Weight",
            "Height",
            "BMI",
            "Category",
            "Date"
        ])

        writer.writerows(data)

    messagebox.showinfo(
        "Export Successful",
        "BMI history has been exported to BMI_History.csv"
    )