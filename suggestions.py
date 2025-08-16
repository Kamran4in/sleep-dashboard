def generate_suggestions(row):
    tips = []

    # Sleep duration
    if row["Sleep Duration"] < 6:
        tips.append("Increase your sleep time to at least 7–8 hours per night.")

    # Stress
    if row["Stress Level"] > 7:
        tips.append("High stress detected. Try meditation, relaxation, or exercise before bed.")

    # Physical Activity
    if row["Physical Activity Level"] < 30:
        tips.append("Increase daily physical activity for better sleep quality.")

    # Daily Steps
    if row["Daily Steps"] < 5000:
        tips.append("Try walking more during the day (aim for 8,000–10,000 steps).")

    # BMI
    if "BMI Category" in row and row["BMI Category"] == 2:  # 0=Normal,1=Overweight,2=Obese
        tips.append("Obesity can affect sleep. Consider diet & lifestyle changes.")

    # Heart Rate
    if row["Heart Rate"] > 85:
        tips.append("Elevated resting heart rate. Try light evening exercise & relaxation.")

    # Blood Pressure
    if row["Systolic_BP"] > 130 or row["Diastolic_BP"] > 85:
        tips.append("Monitor your blood pressure; consult a doctor if consistently high.")

    # Sleep Disorder
    if row["Sleep Disorder"] == 1:  # Example: 1 = Insomnia
        tips.append("Insomnia detected. Maintain a regular sleep schedule & avoid caffeine late.")
    elif row["Sleep Disorder"] == 2:  # Example: 2 = Sleep Apnea
        tips.append("Sleep apnea detected. Consult a specialist & avoid alcohol before sleep.")

    if not tips:
        tips.append("Your sleep habits look good! Maintain consistency.")

    return tips
