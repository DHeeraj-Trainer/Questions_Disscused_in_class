from collections import deque
from datetime import datetime

class Patient:
    def __init__(self, name, age, patient_id, condition, priority, visit_time):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.condition = condition
        self.priority = priority
        self.visit_time = visit_time

    def __str__(self):
        return f"{self.name} (ID: {self.patient_id}) - Condition: {self.condition} - Priority: {self.priority}"

class Doctor:
    def __init__(self, name, doctor_id, specialty):
        self.name = name
        self.doctor_id = doctor_id
        self.specialty = specialty
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_appointments(self, date):
        return [patient for patient in self.patients if patient.visit_time.date() == date]

class Appointment:
    def __init__(self, patient_id, doctor_id, date, time):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}, Date: {self.date}, Time: {self.time}"

class PatientQueue:
    def __init__(self):
        self.queue = deque()

    def add_patient(self, patient):
        if patient.priority == 'emergency':
            self.queue.appendleft(patient)
        else:
            self.queue.append(patient)

    def attend_next_patient(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return None

    def display_queue(self):
        emergency = [str(p) for p in list(self.queue) if p.priority == 'emergency']
        regular = [str(p) for p in list(self.queue) if p.priority == 'normal']
        return {"emergency": emergency, "regular": regular}

class HospitalSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []
        self.patient_queue = PatientQueue()

    def add_patient(self, name, age, condition, priority, visit_time):
        patient_id = len(self.patients) + 1
        patient = Patient(name, age, patient_id, condition, priority, visit_time)
        self.patients[patient_id] = patient
        self.patient_queue.add_patient(patient)
        print(f"Patient {name} added successfully.")

    def add_doctor(self, name, specialty):
        doctor_id = len(self.doctors) + 1
        doctor = Doctor(name, doctor_id, specialty)
        self.doctors[doctor_id] = doctor
        print(f"Doctor {name} added successfully.")

    def schedule_appointment(self, patient_id, doctor_id, date, time):
        if patient_id not in self.patients or doctor_id not in self.doctors:
            print("Invalid patient or doctor ID.")
            return
        appointment = Appointment(patient_id, doctor_id, date, time)
        self.appointments.append(appointment)
        self.doctors[doctor_id].add_patient(self.patients[patient_id])
        print(f"Appointment scheduled for Patient ID: {patient_id} with Doctor ID: {doctor_id}.")

    def get_daily_appointments(self, doctor_id, date):
        doctor = self.doctors.get(doctor_id)
        if not doctor:
            return f"Doctor with ID {doctor_id} not found."
        appointments = doctor.get_appointments(date)
        return appointments

    def attend_next_patient(self):
        patient = self.patient_queue.attend_next_patient()
        if patient:
            print(f"Now attending: {patient.name} (ID: {patient.patient_id}) - {patient.condition}")
        else:
            print("No patients in the queue.")

    def display_waiting_queue(self):
        queue = self.patient_queue.display_queue()
        print("\n--- Emergency Patients ---")
        for patient in queue["emergency"]:
            print(patient)
        print("\n--- Regular Patients ---")
        for patient in queue["regular"]:
            print(patient)

def print_main_menu():
    print("\n--- Main Menu ---")
    print("1. Add a New Patient")
    print("2. Add a New Doctor")
    print("3. Schedule an Appointment")
    print("4. Attend Next Patient")
    print("5. Display Waiting Queue")
    print("6. View Daily Appointments for a Doctor")
    print("7. Exit")

def get_patient_data():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    condition = input("Enter patient condition: ")
    priority = input("Enter priority (emergency/normal): ").lower()
    visit_time = datetime.now()
    return name, age, condition, priority, visit_time

def get_doctor_data():
    name = input("Enter doctor name: ")
    specialty = input("Enter doctor's specialty: ")
    return name, specialty

def get_appointment_data():
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM): ")
    date_time = datetime.strptime(date + ' ' + time, "%Y-%m-%d %H:%M")
    return patient_id, doctor_id, date_time

def run_hospital_system():
    system = HospitalSystem()

    while True:
        print_main_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name, age, condition, priority, visit_time = get_patient_data()
            system.add_patient(name, age, condition, priority, visit_time)
        elif choice == "2":
            name, specialty = get_doctor_data()
            system.add_doctor(name, specialty)
        elif choice == "3":
            patient_id, doctor_id, date_time = get_appointment_data()
            system.schedule_appointment(patient_id, doctor_id, date_time.date(), date_time.time())
        elif choice == "4":
            system.attend_next_patient()
        elif choice == "5":
            system.display_waiting_queue()
        elif choice == "6":
            doctor_id = int(input("Enter doctor ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            date = datetime.strptime(date, "%Y-%m-%d").date()
            appointments = system.get_daily_appointments(doctor_id, date)
            if appointments:
                print(f"Appointments for Doctor ID {doctor_id} on {date}:")
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found.")
        elif choice == "7":
            print("Exiting system...")
            break
        else:
            print("Invalid option. Please try again.")

run_hospital_system()
