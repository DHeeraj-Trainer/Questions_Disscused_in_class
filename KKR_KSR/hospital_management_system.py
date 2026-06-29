
from abc import ABC, abstractmethod

# =========================
# Custom Exceptions
# =========================

class DoctorNotFoundException(Exception):
    pass

class PatientNotFoundException(Exception):
    pass

class AppointmentAlreadyExistsException(Exception):
    pass

class InvalidAgeException(Exception):
    pass

class InvalidFeeException(Exception):
    pass


# =========================
# Abstract Class
# =========================

class Person(ABC):
    def __init__(self, pid, name, age, phone):
        self.id = pid
        self.name = name
        self.age = age
        self.phone = phone

    @abstractmethod
    def display_details(self):
        pass


# =========================
# Doctor
# =========================

class Doctor(Person):

    def __init__(self, doctor_id, name, age, phone, specialization, fee):
        super().__init__(doctor_id, name, age, phone)

        if age <= 0:
            raise InvalidAgeException("Invalid age")

        if fee <= 0:
            raise InvalidFeeException("Invalid consultation fee")

        self.specialization = specialization
        self.__consultation_fee = fee

    def get_consultation_fee(self):
        return self.__consultation_fee

    def set_consultation_fee(self, fee):
        if fee <= 0:
            raise InvalidFeeException("Invalid fee")
        self.__consultation_fee = fee

    def display_details(self):
        print(f"Doctor ID       : {self.id}")
        print(f"Name            : {self.name}")
        print(f"Age             : {self.age}")
        print(f"Phone           : {self.phone}")
        print(f"Specialization  : {self.specialization}")
        print(f"Fee             : {self.__consultation_fee}")
        print("-" * 40)


# =========================
# Patient
# =========================

class Patient(Person):

    def __init__(self, patient_id, name, age, phone, disease):
        super().__init__(patient_id, name, age, phone)

        if age <= 0:
            raise InvalidAgeException("Invalid age")

        self.disease = disease
        self.admission_status = "Admitted"
        self.__medical_history = []

    def add_medical_history(self, treatment):
        self.__medical_history.append(treatment)

    def get_medical_history(self):
        return self.__medical_history

    def display_details(self):
        print(f"Patient ID      : {self.id}")
        print(f"Name            : {self.name}")
        print(f"Age             : {self.age}")
        print(f"Phone           : {self.phone}")
        print(f"Disease         : {self.disease}")
        print(f"Status          : {self.admission_status}")
        print("-" * 40)


# =========================
# Appointment
# =========================

class Appointment:

    def __init__(self, appointment_id, doctor_id, patient_id, date, time):
        self.appointment_id = appointment_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date = date
        self.time = time


# =========================
# Data Storage
# =========================

doctors = {}
patients = {}
appointments = []
diseases = set()
total_revenue = 0


# =========================
# Functions
# =========================

def add_doctor():
    try:
        doctor_id = input("Doctor ID: ")

        if doctor_id in doctors:
            print("Doctor already exists")
            return

        name = input("Name: ")
        age = int(input("Age: "))
        phone = input("Phone: ")
        specialization = input("Specialization: ")
        fee = float(input("Consultation Fee: "))

        doctor = Doctor(
            doctor_id,
            name,
            age,
            phone,
            specialization,
            fee
        )

        doctors[doctor_id] = doctor
        print("Doctor added successfully")

    except Exception as e:
        print("Error:", e)


def add_patient():
    try:
        patient_id = input("Patient ID: ")

        if patient_id in patients:
            print("Patient already exists")
            return

        name = input("Name: ")
        age = int(input("Age: "))
        phone = input("Phone: ")
        disease = input("Disease: ")

        patient = Patient(
            patient_id,
            name,
            age,
            phone,
            disease
        )

        patients[patient_id] = patient
        diseases.add(disease)

        print("Patient added successfully")

    except Exception as e:
        print("Error:", e)


def view_doctors():
    if not doctors:
        print("No doctors available")
        return

    for doctor in doctors.values():
        doctor.display_details()


def view_patients():
    if not patients:
        print("No patients available")
        return

    for patient in patients.values():
        patient.display_details()


def search_doctor():
    doctor_id = input("Enter Doctor ID: ")

    if doctor_id not in doctors:
        raise DoctorNotFoundException("Doctor not found")

    doctors[doctor_id].display_details()


def search_patient():
    patient_id = input("Enter Patient ID: ")

    if patient_id not in patients:
        raise PatientNotFoundException("Patient not found")

    patients[patient_id].display_details()


def book_appointment():
    appointment_id = input("Appointment ID: ")
    doctor_id = input("Doctor ID: ")
    patient_id = input("Patient ID: ")
    date = input("Date: ")
    time = input("Time: ")

    if doctor_id not in doctors:
        raise DoctorNotFoundException("Doctor not found")

    if patient_id not in patients:
        raise PatientNotFoundException("Patient not found")

    for appt in appointments:
        if (
            appt.doctor_id == doctor_id and
            appt.date == date and
            appt.time == time
        ):
            raise AppointmentAlreadyExistsException(
                "Slot already booked"
            )

    appointment = Appointment(
        appointment_id,
        doctor_id,
        patient_id,
        date,
        time
    )

    appointments.append(appointment)

    print("Appointment booked successfully")


def view_appointments():
    if not appointments:
        print("No appointments available")
        return

    for appt in appointments:
        doctor_name = doctors[appt.doctor_id].name
        patient_name = patients[appt.patient_id].name

        print("-" * 40)
        print("Appointment ID :", appt.appointment_id)
        print("Doctor         :", doctor_name)
        print("Patient        :", patient_name)
        print("Date           :", appt.date)
        print("Time           :", appt.time)


def add_treatment():
    patient_id = input("Patient ID: ")

    if patient_id not in patients:
        raise PatientNotFoundException("Patient not found")

    treatment = input("Treatment Description: ")

    patients[patient_id].add_medical_history(treatment)

    print("Treatment added successfully")


def view_treatment_history():
    patient_id = input("Patient ID: ")

    if patient_id not in patients:
        raise PatientNotFoundException("Patient not found")

    history = patients[patient_id].get_medical_history()

    print("Treatment History")

    if not history:
        print("No treatments found")
        return

    for item in history:
        print(item)


def generate_bill():
    global total_revenue

    patient_id = input("Patient ID: ")

    if patient_id not in patients:
        raise PatientNotFoundException("Patient not found")

    doctor_id = input("Consulting Doctor ID: ")

    if doctor_id not in doctors:
        raise DoctorNotFoundException("Doctor not found")

    medicine = float(input("Medicine Charges: "))
    lab = float(input("Lab Charges: "))

    consultation_fee = doctors[doctor_id].get_consultation_fee()

    total = consultation_fee + medicine + lab

    total_revenue += total

    print("\nBill Summary")
    print("Consultation Fee :", consultation_fee)
    print("Medicine Charges :", medicine)
    print("Lab Charges      :", lab)
    print("Total Bill       :", total)


def discharge_patient():
    patient_id = input("Patient ID: ")

    if patient_id not in patients:
        raise PatientNotFoundException("Patient not found")

    patients[patient_id].admission_status = "Discharged"

    print("Patient discharged successfully")


def reports():
    print("\nReports")
    print("Total Doctors      :", len(doctors))
    print("Total Patients     :", len(patients))
    print("Total Appointments :", len(appointments))
    print("Unique Diseases    :", len(diseases))
    print("Disease List       :", diseases)
    print("Total Revenue      :", total_revenue)


# =========================
# Main Menu
# =========================

def main():
    while True:

        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. View Doctors")
        print("4. View Patients")
        print("5. Search Doctor")
        print("6. Search Patient")
        print("7. Book Appointment")
        print("8. View Appointments")
        print("9. Add Treatment")
        print("10. View Treatment History")
        print("11. Generate Bill")
        print("12. Discharge Patient")
        print("13. Reports")
        print("14. Exit")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                add_doctor()

            elif choice == 2:
                add_patient()

            elif choice == 3:
                view_doctors()

            elif choice == 4:
                view_patients()

            elif choice == 5:
                search_doctor()

            elif choice == 6:
                search_patient()

            elif choice == 7:
                book_appointment()

            elif choice == 8:
                view_appointments()

            elif choice == 9:
                add_treatment()

            elif choice == 10:
                view_treatment_history()

            elif choice == 11:
                generate_bill()

            elif choice == 12:
                discharge_patient()

            elif choice == 13:
                reports()

            elif choice == 14:
                print("Thank you")
                break

            else:
                print("Invalid Choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
