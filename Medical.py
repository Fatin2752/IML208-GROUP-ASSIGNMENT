# Medical Clinic Appointment Management System

# Booking
# Create, Read, Update, Delete (CRUD) Functions for Appointments
def appointment_booking():
    appointment_list = []

    def create_appointment():
        patient_id = input("Enter patient ID:")
        patient_name = input("Enter patient's name:")
        doctor_name = input("Enter doctor's name:")
        appointment_date = input("Enter appointment date (YYYY-MM-DD):")
        appointment_time = input("Enter appointment time (HH:MM):")

        appointment_details = {
            "Patient ID": patient_id,
            "Patient Name": patient_name,
            "Doctor Name": doctor_name,
            "Appointment Date": appointment_date,
            "Appointment Time": appointment_time
        }
        appointment_list.append(appointment_details)
        print("Appointment booked successfully!")

    def view_appointments():
        if not appointment_list:
            print("No appointments found!")
        else:
            for appointment in appointment_list:
                print(appointment)

    def update_appointment():
        patient_id = input("Enter the Patient ID of the appointment to update:")
        for appointment in appointment_list:
            if appointment["Patient ID"] == patient_id:
                print("Existing details:", appointment)
                appointment["Doctor Name"] = input("Enter new doctor's name:")
                appointment["Appointment Date"] = input("Enter new appointment date (YYYY-MM-DD):")
                appointment["Appointment Time"] = input("Enter new appointment time (HH:MM):")
                print("Appointment updated successfully!")
                return
        print("Appointment not found!")

    def delete_appointment():
        patient_id = input("Enter the Patient ID of the appointment to delete:")
        for appointment in appointment_list:
            if appointment["Patient ID"] == patient_id:
                appointment_list.remove(appointment)
                print("Appointment deleted successfully!")
                return
        print("Appointment not found!")

    while True:
        print("1. Create Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Delete Appointment")
        print("5. Exit")
        choice = input("Choose an option:")

        if choice == '1':
            create_appointment()
        elif choice == '2':
            view_appointments()
        elif choice == '3':
            update_appointment()
        elif choice == '4':
            delete_appointment()
        elif choice == '5':
            break
        else:
            print("Invalid option! Please try again.")

# Patient Record Management
# Create, Read, Update, Delete (CRUD) Functions for Patients
def patient_management():
    patient_list = []

    def create_patient():
        patient_name = input("Enter patient name:")
        patient_id = input("Enter patient ID:")
        patient_gender = input("Enter patient gender (Male / Female):")
        patient_age = input("Enter patient age:")
        patient_phone = input("Enter patient phone:")

        patient = {
            "Name": patient_name,
            "ID": patient_id,
            "Gender": patient_gender,
            "Age": patient_age,
            "Phone": patient_phone
        }
        patient_list.append(patient)
        print("Patient added successfully!")

    def view_patients():
        if not patient_list:
            print("No patients found!")
        else:
            for patient in patient_list:
                print(patient)

    def update_patient():
        patient_id = input("Enter the Patient ID to update:")
        for patient in patient_list:
            if patient["ID"] == patient_id:
                print("Existing details:", patient)
                patient["Name"] = input("Enter new patient name:")
                patient["Gender"] = input("Enter new gender (Male / Female):")
                patient["Age"] = input("Enter new age:")
                patient["Phone"] = input("Enter new phone:")
                print("Patient updated successfully!")
                return
        print("Patient not found!")

    def delete_patient():
        patient_id = input("Enter the Patient ID to delete:")
        for patient in patient_list:
            if patient["ID"] == patient_id:
                patient_list.remove(patient)
                print("Patient deleted successfully!")
                return
        print("Patient not found!")

    while True:
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")
        choice = input("Choose an option:")

        if choice == '1':
            create_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            break
        else:
            print("Invalid option! Please try again.")

# Nurse Record Management
# Create, Read, Update, Delete (CRUD) Functions for Nurses
def nurse_management():
    nurse_list = []

    def create_nurse():
        nurse_name = input("Enter nurse name:")
        nurse_id = input("Enter nurse ID:")
        nurse_gender = input("Enter nurse gender (Male / Female):")
        nurse_department = input("Enter nurse department:")
        nurse_phone = input("Enter nurse phone:")
        nurse_shift_time = input("Enter nurse shift time:")

        nurse = {
            "Name": nurse_name, 
            "ID": nurse_id,
            "Gender": nurse_gender,
            "Department": nurse_department,
            "Phone": nurse_phone,
            "Shift Time": nurse_shift_time
        }
        nurse_list.append(nurse)
        print("Nurse added successfully!")

    def view_nurses():
        if not nurse_list:
            print("No nurses found!")
        else:
            for nurse in nurse_list:
                print(nurse)

    def update_nurse():
        nurse_id = input("Enter the Nurse ID to update:")
        for nurse in nurse_list:
            if nurse["ID"] == nurse_id:
                print("Existing details:", nurse)
                nurse["Name"] = input("Enter new nurse name:")
                nurse["Gender"] = input("Enter new gender (Male / Female):")
                nurse["Department"] = input("Enter new department:")
                nurse["Phone"] = input("Enter new phone:")
                nurse["Shift Time"] = input("Enter new shift time:")
                print("Nurse updated successfully!")
                return
        print("Nurse not found!")

    def delete_nurse():
        nurse_id = input("Enter the Nurse ID to delete:")
        for nurse in nurse_list:
            if nurse["ID"] == nurse_id:
                nurse_list.remove(nurse)
                print("Nurse deleted successfully!")
                return
        print("Nurse not found!")

    while True:
        print("1. Add Nurse")
        print("2. View Nurses")
        print("3. Update Nurse")
        print("4. Delete Nurse")
        print("5. Exit")
        choice = input("Choose an option:")

        if choice == '1':
            create_nurse()
        elif choice == '2':
            view_nurses()
        elif choice == '3':
            update_nurse()
        elif choice == '4':
            delete_nurse()
        elif choice == '5':
            break
        else:
            print("Invalid option! Please try again.")

# Doctor Record Management
# Create, Read, Update, Delete (CRUD) Functions for Doctors
def doctor_management():
    doctor_list = []

    def create_doctor():
        doctor_name = input("Enter doctor name:")
        doctor_id = input("Enter doctor ID:")
        doctor_gender = input("Enter doctor gender (Male / Female):")
        doctor_specialty = input("Enter doctor specialty:")
        doctor_phone = input("Enter doctor phone:")
        doctor_working_hour = input("Enter doctor working hour:")

        doctor = {
            "Name": doctor_name,
            "ID": doctor_id,
            "Gender": doctor_gender,
            "Specialty": doctor_specialty,
            "Phone": doctor_phone,
            "Working Hour": doctor_working_hour
        }
        doctor_list.append(doctor)
        print("Doctor added successfully!")

    def view_doctors():
        if not doctor_list:
            print("No doctors found!")
        else:
            for doctor in doctor_list:
                print(doctor)

    def update_doctor():
        doctor_id = input("Enter the Doctor ID to update:")
        for doctor in doctor_list:
            if doctor["ID"] == doctor_id:
                print("Existing details:", doctor)
                doctor["Name"] = input("Enter new doctor name:")
                doctor["Gender"] = input("Enter new gender (Male / Female):")
                doctor["Specialty"] = input("Enter new specialty:")
                doctor["Phone"] = input("Enter new phone:")
                doctor["Working Hour"] = input("Enter new working hour:")
                print("Doctor updated successfully!")
                return
        print("Doctor not found!")

    def delete_doctor():
        doctor_id = input("Enter the Doctor ID to delete:")
        for doctor in doctor_list:
            if doctor["ID"] == doctor_id:
                doctor_list.remove(doctor)
                print("Doctor deleted successfully!")
                return
        print("Doctor not found!")

    while True:
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Exit")
        choice = input("Choose an option:")

        if choice == '1':
            create_doctor()
        elif choice == '2':
            view_doctors()
        elif choice == '3':
            update_doctor()
        elif choice == '4':
            delete_doctor()
        elif choice == '5':
            break
        else:
            print("Invalid option! Please try again.")

# Medicine Record Management
# Create, Read, Update, Delete (CRUD) Functions for Medicines
def medicine_management():
    medicine_list = []

    def create_medicine():
        medicine_name = input("Enter medicine name:")
        medicine_type = input("Enter medicine type (Tablet / Syrup / Ointment):")
        medicine_quantity = input("Enter medicine quantity:")
        medicine_expiry_date = input("Enter medicine expiry date:")
        medicine_price = input("Enter medicine price:")

        medicine = {
            "Name": medicine_name,
            "Type": medicine_type,
            "Quantity": medicine_quantity,
            "Expiry Date": medicine_expiry_date,
            "Price": medicine_price
        }
        medicine_list.append(medicine)
        print("Medicine added successfully!")

    def view_medicines():
        if not medicine_list:
            print("No medicines found!")
        else:
            for medicine in medicine_list:
                print(medicine)

    def update_medicine():
        medicine_name = input("Enter the Medicine Name to update:")
        for medicine in medicine_list:
            if medicine["Name"] == medicine_name:
                print("Existing details:", medicine)
                medicine["Type"] = input("Enter new type (Tablet / Syrup / Ointment):")
                medicine["Quantity"] = input("Enter new quantity:")
                medicine["Expiry Date"] = input("Enter new expiry date:")
                medicine["Price"] = input ("Enter new price: ")
                print("Medicine updated successfully!")
                return
        print("Medicine not found!")

    def delete_medicine():
        medicine_name = input("Enter the Medicine Name to delete: ")
        for medicine in medicine_list:
            if medicine["Name"] == medicine_name:
                medicine_list.remove(medicine)
                print("Medicine deleted successfully!")
                return
        print("Medicine not found!")

    while True:
        print("\n--- Medicine Management Menu ---")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Update Medicine")
        print("4. Delete Medicine")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_medicine()
        elif choice == '2':
            view_medicines()
        elif choice == '3':
            update_medicine()
        elif choice == '4':
            delete_medicine()
        elif choice == '5':
            print("Exiting Medicine Management...")
            break
        else:
            print("Invalid option! Please try again.")

#Menu
if __name__ == "__main__":
    while True:
        print("1. Appointment Booking")
        print("2. Patient Management")
        print("3. Nurse Management")
        print("4. Doctor Management")
        print("5. Medicine Management")
        print("6. Exit")

        main_choice = input("Choose an option:")

        if main_choice == '1':
            appointment_booking()
        elif main_choice == '2':
            patient_management()
        elif main_choice == '3':
            nurse_management()
        elif main_choice == '4':
            doctor_management()
        elif main_choice == '5':
            medicine_management()
        elif main_choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid option! Please try again.")
