import matplotlib.pyplot as plt
from database import get_records


def show_graph():

    records = get_records()

    if len(records) == 0:
        return

    names = []
    bmi = []

    for row in reversed(records):
        names.append(row[0])
        bmi.append(row[3])

    plt.figure(figsize=(8,5))
    plt.plot(names, bmi, marker="o", linewidth=2)

    plt.title("BMI Trend")
    plt.xlabel("User")
    plt.ylabel("BMI")

    plt.grid(True)

    plt.show()