import mysql.connector
import tkinter as tk
from tkinter import messagebox




# Function to create a connection to the database
def create_connection():
   try:
       connection = mysql.connector.connect(
           host="localhost",
           user="root",
           database="Study_club"  # Database name
       )
       return connection
   except mysql.connector.Error as err:
       print(f"Error: {err}")
       return None




# Function to insert a new tutor-subject relationship into the database
def insert_tutor_subject(tutor_subject_id, tutor_id, subject_id):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               INSERT INTO TutorSubject (TutorSubjectID, TutorID, SubjectID)
               VALUES (%s, %s, %s)
           """
           cursor.execute(query, (tutor_subject_id, tutor_id, subject_id))
           connection.commit()
           messagebox.showinfo("Success", "Tutor-Subject relationship inserted successfully!")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to insert relationship: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to update an existing tutor-subject relationship
def update_tutor_subject(tutor_subject_id, tutor_id, subject_id):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               UPDATE TutorSubject
               SET TutorID = %s, SubjectID = %s
               WHERE TutorSubjectID = %s
           """
           cursor.execute(query, (tutor_id, subject_id, tutor_subject_id))
           connection.commit()
           if cursor.rowcount > 0:
               messagebox.showinfo("Success", "Tutor-Subject relationship updated successfully!")
           else:
               messagebox.showwarning("Warning", "TutorSubjectID not found.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to update relationship: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to display all tutor-subject relationships
def display_tutor_subjects():
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = "SELECT * FROM TutorSubject"
           cursor.execute(query)
           tutor_subjects = cursor.fetchall()
           relationship_list = "\n".join([
               f"ID: {relationship[0]}, TutorID: {relationship[1]}, SubjectID: {relationship[2]}"
               for relationship in tutor_subjects
           ])
           if relationship_list:
               messagebox.showinfo("All Tutor-Subject Relationships", relationship_list)
           else:
               messagebox.showinfo("All Tutor-Subject Relationships", "No relationships available.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to fetch relationships: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Tkinter GUI
def create_form():
   def submit():
       tutor_subject_id = entry_tutor_subject_id.get()
       tutor_id = entry_tutor_id.get()
       subject_id = entry_subject_id.get()


       if tutor_subject_id and tutor_id and subject_id:
           insert_tutor_subject(tutor_subject_id, tutor_id, subject_id)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   def update():
       tutor_subject_id = entry_tutor_subject_id.get()
       tutor_id = entry_tutor_id.get()
       subject_id = entry_subject_id.get()


       if tutor_subject_id and tutor_id and subject_id:
           update_tutor_subject(tutor_subject_id, tutor_id, subject_id)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   # Creating the form
   root = tk.Tk()
   root.title("Tutor-Subject Management")


   tk.Label(root, text="TutorSubject ID:").grid(row=0, column=0, padx=10, pady=10)
   entry_tutor_subject_id = tk.Entry(root)
   entry_tutor_subject_id.grid(row=0, column=1, padx=10, pady=10)


   tk.Label(root, text="Tutor ID:").grid(row=1, column=0, padx=10, pady=10)
   entry_tutor_id = tk.Entry(root)
   entry_tutor_id.grid(row=1, column=1, padx=10, pady=10)


   tk.Label(root, text="Subject ID:").grid(row=2, column=0, padx=10, pady=10)
   entry_subject_id = tk.Entry(root)
   entry_subject_id.grid(row=2, column=1, padx=10, pady=10)


   tk.Button(root, text="Insert Relationship", command=submit).grid(row=3, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Update Relationship", command=update).grid(row=4, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Show All Relationships", command=display_tutor_subjects).grid(row=5, column=0, columnspan=2, pady=10)


   root.mainloop()




# Run the form
create_form()
