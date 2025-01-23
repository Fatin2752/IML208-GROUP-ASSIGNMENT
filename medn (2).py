import sqlite3

# Database setup 
def create_connection():
    return sqlite3.connect("medn.db")

def create_tables(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                diagnosis TEXT NOT NULL,
                number_phone TEXT NOT NULL UNIQUE
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS doctors (
                doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                speciality TEXT NOT NULL,
                shift_hours TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS medications (
                medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                diagnosis TEXT NOT NULL,
                medication TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS pharmacists (
                pharmacist_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                prescription TEXT NOT NULL,
                medication TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')

        # Insert default users
        conn.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (111, 'Adilah', 'adm195', 'staff')")
        conn.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (222, 'Iman', 'imzy77', 'patient')")
        conn.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (333, 'Atiqah', 'daisy', 'doctor')")
        conn.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (444, 'Fatin', 'rose', 'pharmacist')")
        conn.execute("INSERT OR IGNORE INTO doctors (doctor_id, name, speciality, shift_hours) VALUES (11, 'Doctor Strange', 'stephen', '9-5')")
# Login functionality
def login(username, password):
    conn = create_connection()
    cursor = conn.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

# CRUD functions for Patients
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    diagnosis = input("Enter diagnosis: ")
    number_phone = input("Enter phone number: ")

    conn = create_connection()
    conn.execute("INSERT INTO patients (name, age, gender, diagnosis, number_phone) VALUES (?, ?, ?, ?, ?)",
                 (name, age, gender, diagnosis, number_phone))
    conn.commit()
    conn.close()
    print("Patient added successfully.")

def view_patients():
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM patients")
    for row in cursor:
        print(row)
    conn.close()

def update_patient():
    patient_id = int(input("Enter patient ID: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    gender = input("Enter new gender: ")
    diagnosis = input("Enter new diagnosis: ")
    number_phone = input("Enter new phone number: ")

    conn = create_connection()
    conn.execute("UPDATE patients SET name = ?, age = ?, gender = ?, diagnosis = ?, number_phone = ? WHERE patient_id = ?",
                 (name, age, gender, diagnosis, number_phone, patient_id))
    conn.commit()
    conn.close()
    print("Patient updated successfully.")

def delete_patient():
    patient_id = int(input("Enter patient ID: "))
    conn = create_connection()
    conn.execute("DELETE FROM patients WHERE patient_id = ?", (patient_id,))
    conn.commit()
    conn.close()
    print("Patient deleted successfully.")

# CRUD functions for Doctor
def add_doctors():
    name = input("Enter doctor's name: ")
    speciality = input("Enter doctor's speciality: ")
    shift_hours = input("Enter shift hours: ")
    conn = create_connection()
    conn.execute("INSERT INTO doctors (name, speciality, shift_hours) VALUES (?, ?, ?)", (name, speciality, shift_hours))
    conn.commit()
    conn.close()
    print("Doctor added successfully.")

def view_doctors():
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM doctors")
    for row in cursor:
        print(row)
    conn.close()

def update_doctors():
    doctor_id = int(input("Enter doctor's ID: "))
    name = input("Enter new doctor's name: ")
    speciality = input("Enter new doctor's speciality: ")
    shift_hours = input("Enter new shift hours: ")
    conn = create_connection()
    conn.execute("UPDATE doctors SET name = ?, speciality = ?, shift_hours = ? WHERE doctor_id = ?", 
                 (name, speciality, shift_hours, doctor_id))
    conn.commit()
    conn.close()
    print("Doctor updated successfully.")

def delete_doctors():
    doctor_id = int(input("Enter doctor's ID: "))
    conn = create_connection()
    conn.execute("DELETE FROM doctors WHERE doctor_id = ?", (doctor_id,))
    conn.commit()
    conn.close()
    print("Doctor deleted successfully.")

# CRUD functions for medications
def add_medication():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    diagnosis = input("Enter patient diagnosis: ")
    medication = input("Enter name of medication: ")
    quantity = int(input("Enter quantity: "))
    conn = create_connection()
    conn.execute("INSERT INTO medications (name, age, diagnosis, medication, quantity) VALUES (?, ?, ?, ?, ?)", 
                 (name, age, diagnosis, medication, quantity))
    conn.commit()
    conn.close()
    print("Medication added successfully.")

def view_medication():
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM medications")
    for row in cursor:
        print(row)
    conn.close()

def update_medication():
    medication_id = int(input("Enter medication ID: "))
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    diagnosis = input("Enter patient diagnosis: ")
    medication = input("Enter medication name: ")
    quantity = int(input("Enter quantity: "))
    conn = create_connection()
    conn.execute("UPDATE medications SET name = ?, age = ?, diagnosis = ?, medication = ?, quantity = ? WHERE medication_id = ?", 
                 (name, age, diagnosis, medication, quantity, medication_id))   
    conn.commit()
    conn.close()
    print("Medication updated successfully.")

def delete_medication():
    medication_id = int(input("Enter medication ID: "))
    conn = create_connection()
    conn.execute("DELETE FROM medications WHERE medication_id = ?", (medication_id,))
    conn.commit()
    conn.close()
    print("Medication deleted successfully.")

# CRUD functions for Pharmacist
def add_pharmacist():
    name = input("Enter pharmacist name: ")
    prescription = input("Enter prescription: ")
    medication = input("Enter name of medication: ")
    quantity = int(input("Enter quantity: "))
    conn = create_connection()
    conn.execute("INSERT INTO pharmacists (name, prescription, medication, quantity) VALUES (?, ?, ?, ?)", 
                 (name, prescription, medication, quantity))
    conn.commit()
    conn.close()
    print("Pharmacist added successfully.")

def view_pharmacist():
    conn = create_connection()
    cursor = conn.execute("SELECT * FROM pharmacists")
    for row in cursor:
        print(row)
    conn.close()

def update_pharmacist():
    pharmacist_id = int(input("Enter pharmacist ID: "))
    name = input("Enter pharmacist name: ")
    prescription = input("Enter prescription: ")
    medication = input("Enter medication name: ")
    quantity = int(input("Enter quantity: "))
    conn = create_connection()
    conn.execute("UPDATE pharmacists SET name = ?, prescription = ?, medication = ?, quantity = ? WHERE pharmacist_id = ?", 
                 (name, prescription, medication, quantity, pharmacist_id))   
    conn.commit()
    conn.close()
    print("Pharmacist updated successfully.")

def delete_pharmacist():
    pharmacist_id = int(input("Enter pharmacist ID: "))
    conn = create_connection()
    conn.execute("DELETE FROM pharmacists WHERE pharmacist_id = ?", (pharmacist_id,))
    conn.commit()
    conn.close()
    print("Pharmacist deleted successfully.")

# Role-specific menus
def staff_menu():
    while True:
        print("\nStaff Menu:")
        print("1. Add patient")
        print("2. View patients")
        print("3. Update patient")
        print("4. Delete patient")
        print("5. Logout")

        choice = input("Enter choice: ")
        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def patient_menu():
    while True:
        print("\nPatient Menu:")
        print("1. View doctors")
        print("2. Logout")

        choice = input("Enter choice: ")
        if choice == '1':
            view_doctors()
        elif choice == '2':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def doctor_menu():
    while True:
        print("\nDoctor Menu:")
        print("1. Add medication")
        print("2. View medications")
        print("3. Update medication")
        print("4. Delete medication")
        print("5. Logout")

        choice = input("Enter choice: ")
        if choice == '1':
            add_medication()
        elif choice == '2':
            view_medication()
        elif choice == '3':
            update_medication()
        elif choice == '4':
            delete_medication()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def pharmacist_menu():
    while True:
        print("\nPharmacist Menu:")
        print("1. Add pharmacist")
        print("2. View pharmacists")
        print("3. Update pharmacist")
        print("4. Delete pharmacist")
        print("5. Logout")

        choice = input("Enter choice: ")
        if choice == '1':
            add_pharmacist()
        elif choice == '2':
            view_pharmacist()
        elif choice == '3':
            update_pharmacist()
        elif choice == '4':
            delete_pharmacist()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    conn.close()

    print("Welcome to the Medical System")
    while True:
        username = input("Username: ")
        password = input("Password: ")
        role = login(username, password)
        if role:
            if role == 'staff':
                staff_menu()
            elif role == 'patient':
                patient_menu()
            elif role == 'doctor':
                doctor_menu()
            elif role == 'pharmacist':
                pharmacist_menu()
        else:
            print("Invalid credentials. Please try again.")
