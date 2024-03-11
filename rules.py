def diagnose(symptoms):
    heart_disease_symptoms = ["chest pain", "shortness of breath", "fatigue"]
    diabetes_symptoms = ["increased thirst", "frequent urination", "fatigue"]

    if any(symptom in symptoms for symptom in heart_disease_symptoms):
        return "Heart Disease"
    elif any(symptom in symptoms for symptom in diabetes_symptoms):
        return "Diabetes"
    else:
        return "No specific diagnosis found"
