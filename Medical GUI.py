import tkinter as tk
from tkinter import messagebox, simpledialog


# Appointment Management System
class AppointmentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Clinic Appointment Management System")
        self.appointment_list = []

        # Buttons for CRUD operations
        tk.Button(root, text="Create Appointment", command=self.create_appointment).pack(pady=10)
        tk.Button(root, text="View Appointments", command=self.view_appointments).pack(pady=10)
        tk.Button(root, text="Update Appointment", command=self.update_appointment).pack(pady=10)
        tk.Button(root, text="Delete Appointment", command=self.delete_appointment).pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    def create_appointment(self):
        patient_id = simpledialog.askstring("Input", "Enter patient ID:")
        patient_name = simpledialog.askstring("Input", "Enter patient's name:")
        doctor_name = simpledialog.askstring("Input", "Enter doctor's name:")
        appointment_date = simpledialog.askstring("Input", "Enter appointment date (YYYY-MM-DD):")
        appointment_time = simpledialog.askstring("Input", "Enter appointment time (HH:MM):")

        if patient_id and patient_name and doctor_name and appointment_date and appointment_time:
            appointment_details = {
                "Patient ID": patient_id,
                "Patient Name": patient_name,
                "Doctor Name": doctor_name,
                "Appointment Date": appointment_date,
                "Appointment Time": appointment_time
            }
            self.appointment_list.append(appointment_details)
            messagebox.showinfo("Success", "Appointment booked successfully!")
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def view_appointments(self):
        if not self.appointment_list:
            messagebox.showinfo("Info", "No appointments found!")
        else:
            appointments = "\n".join(
                [f"ID: {a['Patient ID']}, Name: {a['Patient Name']}, Doctor: {a['Doctor Name']}, "
                 f"Date: {a['Appointment Date']}, Time: {a['Appointment Time']}"
                 for a in self.appointment_list]
            )
            messagebox.showinfo("Appointments", appointments)

    def update_appointment(self):
        patient_id = simpledialog.askstring("Input", "Enter the Patient ID of the appointment to update:")
        for appointment in self.appointment_list:
            if appointment["Patient ID"] == patient_id:
                new_doctor = simpledialog.askstring("Input", "Enter new doctor's name:")
                new_date = simpledialog.askstring("Input", "Enter new appointment date (YYYY-MM-DD):")
                new_time = simpledialog.askstring("Input", "Enter new appointment time (HH:MM):")
                if new_doctor and new_date and new_time:
                    appointment["Doctor Name"] = new_doctor
                    appointment["Appointment Date"] = new_date
                    appointment["Appointment Time"] = new_time
                    messagebox.showinfo("Success", "Appointment updated successfully!")
                else:
                    messagebox.showwarning("Warning", "All fields are required!")
                return
        messagebox.showerror("Error", "Appointment not found!")

    def delete_appointment(self):
        patient_id = simpledialog.askstring("Input", "Enter the Patient ID of the appointment to delete:")
        for appointment in self.appointment_list:
            if appointment["Patient ID"] == patient_id:
                self.appointment_list.remove(appointment)
                messagebox.showinfo("Success", "Appointment deleted successfully!")
                return
        messagebox.showerror("Error", "Appointment not found!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentManagementSystem(root)
    root.mainloop()

# Patient Record Management System
class PatientManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Record Management System")
        self.patient_list = []

        # Buttons for CRUD operations
        tk.Button(root, text="Add Patient", command=self.create_patient).pack(pady=10)
        tk.Button(root, text="View Patients", command=self.view_patients).pack(pady=10)
        tk.Button(root, text="Update Patient", command=self.update_patient).pack(pady=10)
        tk.Button(root, text="Delete Patient", command=self.delete_patient).pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    def create_patient(self):
        name = simpledialog.askstring("Input", "Enter patient name:")
        patient_id = simpledialog.askstring("Input", "Enter patient ID:")
        gender = simpledialog.askstring("Input", "Enter patient gender (Male / Female):")
        age = simpledialog.askstring("Input", "Enter patient age:")
        phone = simpledialog.askstring("Input", "Enter patient phone:")

        if name and patient_id and gender and age and phone:
            patient = {
                "Name": name,
                "ID": patient_id,
                "Gender": gender,
                "Age": age,
                "Phone": phone
            }
            self.patient_list.append(patient)
            messagebox.showinfo("Success", "Patient added successfully!")
        else:
            messagebox.showwarning("Warning", "All fields are required!")

    def view_patients(self):
        if not self.patient_list:
            messagebox.showinfo("Info", "No patients found!")
        else:
            patients = "\n".join(
                [f"Name: {p['Name']}, ID: {p['ID']}, Gender: {p['Gender']}, Age: {p['Age']}, Phone: {p['Phone']}"
                 for p in self.patient_list]
            )
            messagebox.showinfo("Patients", patients)

    def update_patient(self):
        patient_id = simpledialog.askstring("Input", "Enter the Patient ID to update:")
        for patient in self.patient_list:
            if patient["ID"] == patient_id:
                new_name = simpledialog.askstring("Input", "Enter new patient name:")
                new_gender = simpledialog.askstring("Input", "Enter new gender (Male / Female):")
                new_age = simpledialog.askstring("Input", "Enter new age:")
                new_phone = simpledialog.askstring("Input", "Enter new phone:")

                if new_name and new_gender and new_age and new_phone:
                    patient["Name"] = new_name
                    patient["Gender"] = new_gender
                    patient["Age"] = new_age
                    patient["Phone"] = new_phone
                    messagebox.showinfo("Success", "Patient updated successfully!")
                else:
                    messagebox.showwarning("Warning", "All fields are required!")
                return
        messagebox.showerror("Error", "Patient not found!")

    def delete_patient(self):
        patient_id = simpledialog.askstring("Input", "Enter the Patient ID to delete:")
        for patient in self.patient_list:
            if patient["ID"] == patient_id:
                self.patient_list.remove(patient)
                messagebox.showinfo("Success", "Patient deleted successfully!")
                return
        messagebox.showerror("Error", "Patient not found!")


if __name__ == "__main__":
    root = tk.Tk()
    app = PatientManagementSystem(root)
    root.mainloop()

class NurseRecordManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Nurse Record Management")
        
        self.nurse_list = []
        
        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(self.master, text="Add Nurse", command=self.add_nurse)
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.master, text="View Nurses", command=self.view_nurses)
        self.view_button.pack(pady=10)

        self.update_button = tk.Button(self.master, text="Update Nurse", command=self.update_nurse)
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Nurse", command=self.delete_nurse)
        self.delete_button.pack(pady=10)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.pack(pady=10)

    def add_nurse(self):
        nurse_name = simpledialog.askstring("Input", "Enter nurse name:")
        nurse_id = simpledialog.askstring("Input", "Enter nurse ID:")
        nurse_gender = simpledialog.askstring("Input", "Enter nurse gender (Male / Female):")
        nurse_department = simpledialog.askstring("Input", "Enter nurse department:")
        nurse_phone = simpledialog.askstring("Input", "Enter nurse phone:")
        nurse_shift_time = simpledialog.askstring("Input", "Enter nurse shift time:")

        nurse = {
            "Name": nurse_name,
            "ID": nurse_id,
            "Gender": nurse_gender,
            "Department": nurse_department,
            "Phone": nurse_phone,
            "Shift Time": nurse_shift_time
        }
        self.nurse_list.append(nurse)
        messagebox.showinfo("Success", "Nurse added successfully!")

    def view_nurses(self):
        if not self.nurse_list:
            messagebox.showwarning("Warning", "No nurses found!")
        else:
            nurses_info = "\n".join([str(nurse) for nurse in self.nurse_list])
            messagebox.showinfo("Nurses List", nurses_info)

    def update_nurse(self):
        nurse_id = simpledialog.askstring("Input", "Enter the Nurse ID to update:")
        for nurse in self.nurse_list:
            if nurse["ID"] == nurse_id:
                nurse["Name"] = simpledialog.askstring("Input", "Enter new nurse name:", initialvalue=nurse["Name"])
                nurse["Gender"] = simpledialog.askstring("Input", "Enter new gender (Male / Female):", initialvalue=nurse["Gender"])
                nurse["Department"] = simpledialog.askstring("Input", "Enter new department:", initialvalue=nurse["Department"])
                nurse["Phone"] = simpledialog.askstring("Input", "Enter new phone:", initialvalue=nurse["Phone"])
                nurse["Shift Time"] = simpledialog.askstring("Input", "Enter new shift time:", initialvalue=nurse["Shift Time"])
                messagebox.showinfo("Success", "Nurse updated successfully!")
                return
        messagebox.showwarning("Warning", "Nurse not found!")

    def delete_nurse(self):
        nurse_id = simpledialog.askstring("Input", "Enter the Nurse ID to delete:")
        for nurse in self.nurse_list:
            if nurse["ID"] == nurse_id:
                self.nurse_list.remove(nurse)
                messagebox.showinfo("Success", "Nurse deleted successfully!")
                return
        messagebox.showwarning("Warning", "Nurse not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NurseRecordManagement(root)
    root.mainloop()

class DoctorRecordManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor Record Management")
        
        self.doctor_list = []
        
        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(self.master, text="Add Doctor", command=self.add_doctor)
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.master, text="View Doctors", command=self.view_doctors)
        self.view_button.pack(pady=10)

        self.update_button = tk.Button(self.master, text="Update Doctor", command=self.update_doctor)
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Doctor", command=self.delete_doctor)
        self.delete_button.pack(pady=10)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.pack(pady=10)

    def add_doctor(self):
        doctor_name = simpledialog.askstring("Input", "Enter doctor name:")
        doctor_id = simpledialog.askstring("Input", "Enter doctor ID:")
        doctor_gender = simpledialog.askstring("Input", "Enter doctor gender (Male / Female):")
        doctor_specialty = simpledialog.askstring("Input", "Enter doctor specialty:")
        doctor_phone = simpledialog.askstring("Input", "Enter doctor phone:")
        doctor_working_hour = simpledialog.askstring("Input", "Enter doctor working hour:")

        doctor = {
            "Name": doctor_name,
            "ID": doctor_id,
            "Gender": doctor_gender,
            "Specialty": doctor_specialty,
            "Phone": doctor_phone,
            "Working Hour": doctor_working_hour
        }
        self.doctor_list.append(doctor)
        messagebox.showinfo("Success", "Doctor added successfully!")

    def view_doctors(self):
        if not self.doctor_list:
            messagebox.showwarning("Warning", "No doctors found!")
        else:
            doctors_info = "\n".join([str(doctor) for doctor in self.doctor_list])
            messagebox.showinfo("Doctors List", doctors_info)

    def update_doctor(self):
        doctor_id = simpledialog.askstring("Input", "Enter the Doctor ID to update:")
        for doctor in self.doctor_list:
            if doctor["ID"] == doctor_id:
                doctor["Name"] = simpledialog.askstring("Input", "Enter new doctor name:", initialvalue=doctor["Name"])
                doctor["Gender"] = simpledialog.askstring("Input", "Enter new gender (Male / Female):", initialvalue=doctor["Gender"])
                doctor["Specialty"] = simpledialog.askstring("Input", "Enter new specialty:", initialvalue=doctor["Specialty"])
                doctor["Phone"] = simpledialog.askstring("Input", "Enter new phone:", initialvalue=doctor["Phone"])
                doctor["Working Hour"] = simpledialog.askstring("Input", "Enter new working hour:", initialvalue=doctor["Working Hour"])
                messagebox.showinfo("Success", "Doctor updated successfully!")
                return
        messagebox.showwarning("Warning", "Doctor not found!")

    def delete_doctor(self):
        doctor_id = simpledialog.askstring("Input", "Enter the Doctor ID to delete:")
        for doctor in self.doctor_list:
            if doctor["ID"] == doctor_id:
                self.doctor_list.remove(doctor)
                messagebox.showinfo("Success", "Doctor deleted successfully!")
                return
        messagebox.showwarning("Warning", "Doctor not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DoctorRecordManagement(root)
    root.mainloop()

class MedicineRecordManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine Record Management")
        
        self.medicine_list = []

        self.create_widgets()

    def create_widgets(self):
        self.add_button = tk.Button(self.master, text="Add Medicine", command=self.add_medicine)
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.master, text="View Medicines", command=self.view_medicines)
        self.view_button.pack(pady=10)

        self.update_button = tk.Button(self.master, text="Update Medicine", command=self.update_medicine)
        self.update_button.pack(pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Medicine", command=self.delete_medicine)
        self.delete_button.pack(pady=10)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.pack(pady=10)

    def add_medicine(self):
        medicine_name = simpledialog.askstring("Input", "Enter medicine name:")
        medicine_type = simpledialog.askstring("Input", "Enter medicine type (Tablet / Syrup / Ointment):")
        medicine_quantity = simpledialog.askstring("Input", "Enter medicine quantity:")
        medicine_expiry_date = simpledialog.askstring("Input", "Enter medicine expiry date:")
        medicine_price = simpledialog.askstring("Input", "Enter medicine price:")

        medicine = {
            "Name": medicine_name,
            "Type": medicine_type,
            "Quantity": medicine_quantity,
            "Expiry Date": medicine_expiry_date,
            "Price": medicine_price
        }
        self.medicine_list.append(medicine)
        messagebox.showinfo("Success", "Medicine added successfully!")

    def view_medicines(self):
        if not self.medicine_list:
            messagebox.showwarning("Warning", "No medicines found!")
        else:
            medicines_info = "\n".join([str(medicine) for medicine in self.medicine_list])
            messagebox.showinfo("Medicines List", medicines_info)

    def update_medicine(self):
        medicine_name = simpledialog.askstring("Input", "Enter the Medicine Name to update:")
        for medicine in self.medicine_list:
            if medicine["Name"] == medicine_name:
                medicine["Type"] = simpledialog.askstring("Input", "Enter new type (Tablet / Syrup / Ointment):", initialvalue=medicine["Type"])
                medicine["Quantity"] = simpledialog.askstring("Input", "Enter new quantity:", initialvalue=medicine["Quantity"])
                medicine["Expiry Date"] = simpledialog.askstring("Input", "Enter new expiry date:", initialvalue=medicine["Expiry Date"])
                medicine["Price"] = simpledialog.askstring("Input", "Enter new price:", initialvalue=medicine["Price"])
                messagebox.showinfo("Success", "Medicine updated successfully!")
                return
        messagebox.showwarning("Warning", "Medicine not found!")

    def delete_medicine(self):
        medicine_name = simpledialog.askstring("Input", "Enter the Medicine Name to delete:")
        for medicine in self.medicine_list:
            if medicine["Name"] == medicine_name:
                self.medicine_list.remove(medicine)
                messagebox.showinfo("Success", "Medicine deleted successfully!")
                return
        messagebox.showwarning("Warning", "Medicine not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicineRecordManagement(root)
    root.mainloop()
