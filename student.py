import mysql.connector
import tkinter as tk
from tkinter import messagebox




# Function to create a connection to the database
def create_connection():
   try:
       connection = mysql.connector.connect(
           host="localhost",
           user="root",
           database="Study_club"  # Adjust database name as needed
       )
       return connection
   except mysql.connector.Error as err:
       print(f"Error: {err}")
       return None




# Function to insert a new student into the database
def insert_student(student_id, first_name, last_name, gender, email, phone, academic_level):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               INSERT INTO Student (StudentID, StudFirstName, StudLastName, StudGender, StudEmail, StudPhone, AcademicLevel)
               VALUES (%s, %s, %s, %s, %s, %s, %s)
           """
           cursor.execute(query, (student_id, first_name, last_name, gender, email, phone, academic_level))
           connection.commit()
           messagebox.showinfo("Success", "Student inserted successfully!")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to insert student: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to update an existing student's details
def update_student(student_id, first_name, last_name, gender, email, phone, academic_level):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               UPDATE Student
               SET StudFirstName = %s, StudLastName = %s, StudGender = %s, StudEmail = %s, StudPhone = %s, AcademicLevel = %s
               WHERE StudentID = %s
           """
           cursor.execute(query, (first_name, last_name, gender, email, phone, academic_level, student_id))
           connection.commit()
           if cursor.rowcount > 0:
               messagebox.showinfo("Success", "Student updated successfully!")
           else:
               messagebox.showwarning("Warning", "Student ID not found.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to update student: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to display all students
def display_students():
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = "SELECT * FROM Student"
           cursor.execute(query)
           students = cursor.fetchall()
           student_list = "\n".join([f"ID: {student[0]}, Name: {student[1]} {student[2]}, Gender: {student[3]}, Email: {student[4]}, Phone: {student[5]}, Level: {student[6]}" for student in students])
           if student_list:
               messagebox.showinfo("All Students", student_list)
           else:
               messagebox.showinfo("All Students", "No students available.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to fetch students: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Tkinter GUI
def create_form():
   def submit():
       student_id = entry_student_id.get()
       first_name = entry_first_name.get()
       last_name = entry_last_name.get()
       gender = entry_gender.get()
       email = entry_email.get()
       phone = entry_phone.get()
       academic_level = entry_academic_level.get()


       if student_id and first_name and last_name and gender and email and phone and academic_level:
           insert_student(student_id, first_name, last_name, gender, email, phone, academic_level)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   def update():
       student_id = entry_student_id.get()
       first_name = entry_first_name.get()
       last_name = entry_last_name.get()
       gender = entry_gender.get()
       email = entry_email.get()
       phone = entry_phone.get()
       academic_level = entry_academic_level.get()


       if student_id and first_name and last_name and gender and email and phone and academic_level:
           update_student(student_id, first_name, last_name, gender, email, phone, academic_level)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   # Creating the form
   root = tk.Tk()
   root.title("Student Information")


   tk.Label(root, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
   entry_student_id = tk.Entry(root)
   entry_student_id.grid(row=0, column=1, padx=10, pady=10)


   tk.Label(root, text="First Name:").grid(row=1, column=0, padx=10, pady=10)
   entry_first_name = tk.Entry(root)
   entry_first_name.grid(row=1, column=1, padx=10, pady=10)


   tk.Label(root, text="Last Name:").grid(row=2, column=0, padx=10, pady=10)
   entry_last_name = tk.Entry(root)
   entry_last_name.grid(row=2, column=1, padx=10, pady=10)


   tk.Label(root, text="Gender:").grid(row=3, column=0, padx=10, pady=10)
   entry_gender = tk.Entry(root)
   entry_gender.grid(row=3, column=1, padx=10, pady=10)


   tk.Label(root, text="Email:").grid(row=4, column=0, padx=10, pady=10)
   entry_email = tk.Entry(root)
   entry_email.grid(row=4, column=1, padx=10, pady=10)


   tk.Label(root, text="Phone:").grid(row=5, column=0, padx=10, pady=10)
   entry_phone = tk.Entry(root)
   entry_phone.grid(row=5, column=1, padx=10, pady=10)


   tk.Label(root, text="Academic Level:").grid(row=6, column=0, padx=10, pady=10)
   entry_academic_level = tk.Entry(root)
   entry_academic_level.grid(row=6, column=1, padx=10, pady=10)


   tk.Button(root, text="Insert Student", command=submit).grid(row=7, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Update Student", command=update).grid(row=8, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Show All Students", command=display_students).grid(row=9, column=0, columnspan=2, pady=10)


   root.mainloop()




# Run the form
create_form()



