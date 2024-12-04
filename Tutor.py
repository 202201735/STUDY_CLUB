import mysql.connector
import tkinter as tk
from tkinter import messagebox




# Function to create a connection to the database
def create_connection():
   try:
       connection = mysql.connector.connect(
           host="localhost",
           user="root",
           database="Study_club"  # New database name
       )
       return connection
   except mysql.connector.Error as err:
       print(f"Error: {err}")
       return None




# Function to insert a new tutor into the database
def insert_tutor(tutor_id, first_name, last_name, gender, email, phone, start_year):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               INSERT INTO Tutor (TutorID, TutFirstName, TutLastName, TutGender, TutEmail, TutPhone, TutStartYear)
               VALUES (%s, %s, %s, %s, %s, %s, %s)
           """
           cursor.execute(query, (tutor_id, first_name, last_name, gender, email, phone, start_year))
           connection.commit()
           messagebox.showinfo("Success", "Tutor inserted successfully!")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to insert tutor: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to update an existing tutor's details
def update_tutor(tutor_id, first_name, last_name, gender, email, phone, start_year):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               UPDATE Tutor
               SET TutFirstName = %s, TutLastName = %s, TutGender = %s, TutEmail = %s, TutPhone = %s, TutStartYear = %s
               WHERE TutorID = %s
           """
           cursor.execute(query, (first_name, last_name, gender, email, phone, start_year, tutor_id))
           connection.commit()
           if cursor.rowcount > 0:
               messagebox.showinfo("Success", "Tutor updated successfully!")
           else:
               messagebox.showwarning("Warning", "Tutor ID not found.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to update tutor: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to display all tutors
def display_tutors():
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = "SELECT * FROM Tutor"
           cursor.execute(query)
           tutors = cursor.fetchall()
           tutor_list = "\n".join([
               f"ID: {tutor[0]}, Name: {tutor[1]} {tutor[2]}, Gender: {tutor[3]}, Email: {tutor[4]}, Phone: {tutor[5]}, Start Year: {tutor[6]}"
               for tutor in tutors
           ])
           if tutor_list:
               messagebox.showinfo("All Tutors", tutor_list)
           else:
               messagebox.showinfo("All Tutors", "No tutors available.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to fetch tutors: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Tkinter GUI
def create_form():
   def submit():
       tutor_id = entry_tutor_id.get()
       first_name = entry_first_name.get()
       last_name = entry_last_name.get()
       gender = entry_gender.get()
       email = entry_email.get()
       phone = entry_phone.get()
       start_year = entry_start_year.get()


       if tutor_id and first_name and last_name and gender and email and phone and start_year:
           insert_tutor(tutor_id, first_name, last_name, gender, email, phone, start_year)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   def update():
       tutor_id = entry_tutor_id.get()
       first_name = entry_first_name.get()
       last_name = entry_last_name.get()
       gender = entry_gender.get()
       email = entry_email.get()
       phone = entry_phone.get()
       start_year = entry_start_year.get()


       if tutor_id and first_name and last_name and gender and email and phone and start_year:
           update_tutor(tutor_id, first_name, last_name, gender, email, phone, start_year)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   # Creating the form
   root = tk.Tk()
   root.title("Tutor Information")


   tk.Label(root, text="Tutor ID:").grid(row=0, column=0, padx=10, pady=10)
   entry_tutor_id = tk.Entry(root)
   entry_tutor_id.grid(row=0, column=1, padx=10, pady=10)


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


   tk.Label(root, text="Start Year:").grid(row=6, column=0, padx=10, pady=10)
   entry_start_year = tk.Entry(root)
   entry_start_year.grid(row=6, column=1, padx=10, pady=10)


   tk.Button(root, text="Insert Tutor", command=submit).grid(row=7, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Update Tutor", command=update).grid(row=8, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Show All Tutors", command=display_tutors).grid(row=9, column=0, columnspan=2, pady=10)


   root.mainloop()




# Run the form
create_form()
