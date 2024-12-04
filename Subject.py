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




# Function to insert a new subject into the database
def insert_subject(subject_id, subject_name, subject_code, difficulty_level, tutor_id):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               INSERT INTO Subject (SubjectID, SubjectName, SubjectCode, DifficultyLevel, TutorID)
               VALUES (%s, %s, %s, %s, %s)
           """
           cursor.execute(query, (subject_id, subject_name, subject_code, difficulty_level, tutor_id))
           connection.commit()
           messagebox.showinfo("Success", "Subject inserted successfully!")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to insert subject: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to update an existing subject
def update_subject(subject_id, subject_name, subject_code, difficulty_level, tutor_id):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               UPDATE Subject
               SET SubjectName = %s, SubjectCode = %s, DifficultyLevel = %s, TutorID = %s
               WHERE SubjectID = %s
           """
           cursor.execute(query, (subject_name, subject_code, difficulty_level, tutor_id, subject_id))
           connection.commit()
           if cursor.rowcount > 0:
               messagebox.showinfo("Success", "Subject updated successfully!")
           else:
               messagebox.showwarning("Warning", "Subject ID not found.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to update subject: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to display all subjects
def display_subjects():
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = "SELECT * FROM Subject"
           cursor.execute(query)
           subjects = cursor.fetchall()
           subject_list = "\n".join([
               f"ID: {subject[0]}, Name: {subject[1]}, Code: {subject[2]}, Difficulty: {subject[3]}, TutorID: {subject[4]}"
               for subject in subjects
           ])
           if subject_list:
               messagebox.showinfo("All Subjects", subject_list)
           else:
               messagebox.showinfo("All Subjects", "No subjects available.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to fetch subjects: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Tkinter GUI
def create_form():
   def submit():
       subject_id = entry_subject_id.get()
       subject_name = entry_subject_name.get()
       subject_code = entry_subject_code.get()
       difficulty_level = entry_difficulty_level.get()
       tutor_id = entry_tutor_id.get()


       if subject_id and subject_name and subject_code and difficulty_level and tutor_id:
           insert_subject(subject_id, subject_name, subject_code, difficulty_level, tutor_id)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   def update():
       subject_id = entry_subject_id.get()
       subject_name = entry_subject_name.get()
       subject_code = entry_subject_code.get()
       difficulty_level = entry_difficulty_level.get()
       tutor_id = entry_tutor_id.get()


       if subject_id and subject_name and subject_code and difficulty_level and tutor_id:
           update_subject(subject_id, subject_name, subject_code, difficulty_level, tutor_id)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   # Creating the form
   root = tk.Tk()
   root.title("Subject Management")


   tk.Label(root, text="Subject ID:").grid(row=0, column=0, padx=10, pady=10)
   entry_subject_id = tk.Entry(root)
   entry_subject_id.grid(row=0, column=1, padx=10, pady=10)


   tk.Label(root, text="Subject Name:").grid(row=1, column=0, padx=10, pady=10)
   entry_subject_name = tk.Entry(root)
   entry_subject_name.grid(row=1, column=1, padx=10, pady=10)


   tk.Label(root, text="Subject Code:").grid(row=2, column=0, padx=10, pady=10)
   entry_subject_code = tk.Entry(root)
   entry_subject_code.grid(row=2, column=1, padx=10, pady=10)


   tk.Label(root, text="Difficulty Level:").grid(row=3, column=0, padx=10, pady=10)
   entry_difficulty_level = tk.Entry(root)
   entry_difficulty_level.grid(row=3, column=1, padx=10, pady=10)


   tk.Label(root, text="Tutor ID:").grid(row=4, column=0, padx=10, pady=10)
   entry_tutor_id = tk.Entry(root)
   entry_tutor_id.grid(row=4, column=1, padx=10, pady=10)


   tk.Button(root, text="Insert Subject", command=submit).grid(row=5, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Update Subject", command=update).grid(row=6, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Show All Subjects", command=display_subjects).grid(row=7, column=0, columnspan=2, pady=10)


   root.mainloop()




# Run the form
create_form()
