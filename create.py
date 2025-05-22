# etl/generate_data.py
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_unorganized_patient_data(num_records=100, file_path='~/healthcare_etl_project/raw_patient_data.csv'):
    """
    Generates a CSV file simulating unorganized patient data.
    """
    fake = Faker()
    data = []

    for i in range(num_records):
        patient_id = f"PID{i+1:04d}"
        first_name = fake.first_name()
        last_name = fake.last_name()
        dob = fake.date_of_birth(minimum_age=1, maximum_age=90)
        gender = random.choice(['Male', 'Female', 'Other', None])
        admission_date = fake.date_this_year()
        diagnosis = random.choice(['Flu', 'Cold', 'Fever', 'Migraine', 'Broken Bone', 'Diabetes', 'Hypertension', None])
        blood_pressure = f"{random.randint(90, 140)}/{random.randint(60, 90)}" if random.random() > 0.1 else None # Simulate missing
        temperature = round(random.uniform(36.0, 40.0), 1) if random.random() > 0.05 else None # Simulate missing
        medication = random.choice(['Paracetamol', 'Ibuprofen', 'Amoxicillin', 'Insulin', 'Lisinopril', None])
        room_number = random.randint(101, 500) if random.random() > 0.03 else None # Simulate missing

        # Introduce some "unorganized" elements
        if random.random() < 0.2: # Inconsistent DOB format
            dob_str = dob.strftime(random.choice(['%m/%d/%Y', '%d-%m-%Y', '%Y%m%d']))
        else:
            dob_str = dob.strftime('%Y-%m-%d')

        if random.random() < 0.15: # Inconsistent Admission Date format
            admission_date_str = admission_date.strftime(random.choice(['%m/%d/%y', '%Y-%m-%d %H:%M:%S']))
        else:
            admission_date_str = admission_date.strftime('%Y-%m-%d')

        if random.random() < 0.1: # Mixed case names
            first_name = first_name.upper() if random.random() < 0.5 else first_name.lower()
            last_name = last_name.upper() if random.random() < 0.5 else last_name.lower()

        data.append({
            'Patient_ID': patient_id,
            'First_Name': first_name,
            'Last_Name': last_name,
            'Date_of_Birth': dob_str,
            'Gender': gender,
            'Admission_Date': admission_date_str,
            'Primary_Diagnosis': diagnosis,
            'Blood_Pressure': blood_pressure,
            'Body_Temperature': temperature,
            'Prescribed_Medication': medication,
            'Room_Number': room_number
        })

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Generated {num_records} records to {file_path}")
    return file_path

if __name__ == "__main__":
    # Example of how to run it directly
    generate_unorganized_patient_data(num_records=200, file_path='raw_patient_data.csv')
