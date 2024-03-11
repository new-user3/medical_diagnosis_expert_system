from rules import diagnose

def main():
    print("Welcome to the Medical Diagnosis Expert System")
    print("Please enter the symptoms you are experiencing:")
    symptoms = input("Symptoms (comma-separated): ").split(',')
    diagnosis = diagnose(symptoms)
    print("Based on the symptoms provided, the possible diagnosis is:", diagnosis)

if __name__ == "__main__":
    main()
