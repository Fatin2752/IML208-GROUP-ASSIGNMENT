import tkinter as tk
from tkinter import ttk, messagebox

# Main Application Class
class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("600x400")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        self.create_nurse_tab()
        self.create_doctor_tab()
        self.create_appointment_tab()
        self.create_patient_tab()
        self.create_medicine_tab()

    def create_nurse_tab(self):
        nurse_tab = ttk.Frame(self.notebook)
        self.notebook.add(nurse_tab, text="Nurses")

        tk.Label(nurse_tab, text="Name").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(nurse_tab, text="ID").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(nurse_tab, text="Gender").grid(row=0, column=2, padx=10, pady=5)
        tk.Label(nurse_tab, text="Department").grid(row=0, column=3, padx=10, pady=5)
        tk.Label(nurse_tab, text="Phone").grid(row=0, column=4, padx=10, pady=5)
        tk.Label(nurse_tab, text="Shift Time").grid(row=0, column=5, padx=10, pady=5)

        self.nurse_data = []

        def add_nurse():
            name = name_entry.get()
            nurse_id = id_entry.get()
            gender = gender_entry.get()
            department = department_entry.get()
            phone = phone_entry.get()
            shift_time = shift_entry.get()

            if not (name and nurse_id and gender and department and phone and shift_time):
                messagebox.showerror("Error", "All fields are required")
                return

            self.nurse_data.append((name, nurse_id, gender, department, phone, shift_time))
            nurse_list.insert("", "end", values=(name, nurse_id, gender, department, phone, shift_time))

        name_entry = ttk.Entry(nurse_tab)
        name_entry.grid(row=1, column=0, padx=10, pady=5)

        id_entry = ttk.Entry(nurse_tab)
        id_entry.grid(row=1, column=1, padx=10, pady=5)

        gender_entry = ttk.Entry(nurse_tab)
        gender_entry.grid(row=1, column=2, padx=10, pady=5)

        department_entry = ttk.Entry(nurse_tab)
        department_entry.grid(row=1, column=3, padx=10, pady=5)

        phone_entry = ttk.Entry(nurse_tab)
        phone_entry.grid(row=1, column=4, padx=10, pady=5)

        shift_entry = ttk.Entry(nurse_tab)
        shift_entry.grid(row=1, column=5, padx=10, pady=5)

        add_button = ttk.Button(nurse_tab, text="Add Nurse", command=add_nurse)
        add_button.grid(row=2, column=0, columnspan=6, pady=10)

        nurse_list = ttk.Treeview(nurse_tab, columns=("Name", "ID", "Gender", "Department", "Phone", "Shift"), show="headings")
        nurse_list.grid(row=3, column=0, columnspan=6, pady=10)

        for col in ("Name", "ID", "Gender", "Department", "Phone", "Shift"):
            nurse_list.heading(col, text=col)

    def create_doctor_tab(self):
        doctor_tab = ttk.Frame(self.notebook)
        self.notebook.add(doctor_tab, text="Doctors")

        tk.Label(doctor_tab, text="Name").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(doctor_tab, text="ID").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(doctor_tab, text="Gender").grid(row=0, column=2, padx=10, pady=5)
        tk.Label(doctor_tab, text="Speciality").grid(row=0, column=3, padx=10, pady=5)
        tk.Label(doctor_tab, text="Phone").grid(row=0, column=4, padx=10, pady=5)
        tk.Label(doctor_tab, text="Working Hour").grid(row=0, column=5, padx=10, pady=5)

        self.doctor_data = []

        def add_doctor():
            name = name_entry.get()
            doctor_id = id_entry.get()
            gender = gender_entry.get()
            speciality = speciality_entry.get()
            phone = phone_entry.get()
            working_hour = working_hour_entry.get()

            if not (name and doctor_id and gender and speciality and phone and working_hour):
                messagebox.showerror("Error", "All fields are required")
                return

            self.doctor_data.append((name, doctor_id, gender, speciality, phone, working_hour))
            doctor_list.insert("", "end", values=(name, doctor_id, gender, speciality, phone, working_hour))

        name_entry = ttk.Entry(doctor_tab)
        name_entry.grid(row=1, column=0, padx=10, pady=5)

        id_entry = ttk.Entry(doctor_tab)
        id_entry.grid(row=1, column=1, padx=10, pady=5)

        gender_entry = ttk.Entry(doctor_tab)
        gender_entry.grid(row=1, column=2, padx=10, pady=5)

        speciality_entry = ttk.Entry(doctor_tab)
        speciality_entry.grid(row=1, column=3, padx=10, pady=5)

        phone_entry = ttk.Entry(doctor_tab)
        phone_entry.grid(row=1, column=4, padx=10, pady=5)

        working_hour_entry = ttk.Entry(doctor_tab)
        working_hour_entry.grid(row=1, column=5, padx=10, pady=5)

        add_button = ttk.Button(doctor_tab, text="Add Doctor", command=add_doctor)
        add_button.grid(row=2, column=0, columnspan=6, pady=10)

        doctor_list = ttk.Treeview(doctor_tab, columns=("Name", "ID", "Gender", "Speciality", "Phone", "Working Hour"), show="headings")
        doctor_list.grid(row=3, column=0, columnspan=6, pady=10)

        for col in ("Name", "ID", "Gender", "Speciality", "Phone", "Working Hour"):
            doctor_list.heading(col, text=col)

    def create_appointment_tab(self):
        appointment_tab = ttk.Frame(self.notebook)
        self.notebook.add(appointment_tab, text="Appointments")

        # TODO: Implement appointment functionality

    def create_patient_tab(self):
        patient_tab = ttk.Frame(self.notebook)
        self.notebook.add(patient_tab, text="Patients")

        # TODO: Implement patient functionality

    def create_medicine_tab(self):
        medicine_tab = ttk.Frame(self.notebook)
        self.notebook.add(medicine_tab, text="Medicines")

        # TODO: Implement medicine functionality

# Main Application Run
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()