def calculate_bmi(weight, height):
    return round(weight / (height * height), 2)


def get_category(bmi):

    if bmi < 18.5:
        return (
            "Underweight",
            "You are below the healthy weight range.\nIncrease nutritious food intake and consult a healthcare professional if needed.",
            "#3498db"
        )

    elif bmi < 25:
        return (
            "Normal Weight",
            "Excellent! Your BMI is within the healthy range.\nMaintain your balanced diet and regular exercise.",
            "#2ecc71"
        )

    elif bmi < 30:
        return (
            "Overweight",
            "You are above the healthy range.\nRegular exercise and a balanced diet are recommended.",
            "#f39c12"
        )

    else:
        return (
            "Obese",
            "Your BMI indicates obesity.\nConsult a healthcare professional and adopt a healthier lifestyle.",
            "#e74c3c"
        )