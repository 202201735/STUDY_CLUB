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




# Function to insert a new session into the database
def insert_session(session_id, session_number, session_date, start_time, end_time, tutor_id, student_id):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               INSERT INTO Session (SessionID, SessionNumber, SessionDate, SessionStartTime, SessionEndTime, TutorID, StudentID)
               VALUES (%s, %s, %s, %s, %s, %s, %s)
           """
           cursor.execute(query, (session_id, session_number, session_date, start_time, end_time, tutor_id, student_id))
           connection.commit()
           messagebox.showinfo("Success", "Session inserted successfully!")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to insert session: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to update an existing session
def update_session(session_id, session_number, session_date, start_time, end_time, tutor_id, student_id):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               UPDATE Session
               SET SessionNumber = %s, SessionDate = %s, SessionStartTime = %s, SessionEndTime = %s, TutorID = %s, StudentID = %s
               WHERE SessionID = %s
           """
           cursor.execute(query, (session_number, session_date, start_time, end_time, tutor_id, student_id, session_id))
           connection.commit()
           if cursor.rowcount > 0:
               messagebox.showinfo("Success", "Session updated successfully!")
           else:
               messagebox.showwarning("Warning", "Session ID not found.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to update session: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to display all sessions
def display_sessions():
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = "SELECT * FROM Session"
           cursor.execute(query)
           sessions = cursor.fetchall()
           session_list = "\n".join([
               f"ID: {session[0]}, Number: {session[1]}, Date: {session[2]}, Start Time: {session[3]}, End Time: {session[4]}, TutorID: {session[5]}, StudentID: {session[6]}"
               for session in sessions
           ])
           if session_list:
               messagebox.showinfo("All Sessions", session_list)
           else:
               messagebox.showinfo("All Sessions", "No sessions available.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to fetch sessions: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Tkinter GUI
def create_form():
   def submit():
       session_id = entry_session_id.get()
       session_number = entry_session_number.get()
       session_date = entry_session_date.get()
       start_time = entry_start_time.get()
       end_time = entry_end_time.get()
       tutor_id = entry_tutor_id.get()
       student_id = entry_student_id.get()


       if session_id and session_number and session_date and start_time and end_time and tutor_id and student_id:
           insert_session(session_id, session_number, session_date, start_time, end_time, tutor_id, student_id)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   def update():
       session_id = entry_session_id.get()
       session_number = entry_session_number.get()
       session_date = entry_session_date.get()
       start_time = entry_start_time.get()
       end_time = entry_end_time.get()
       tutor_id = entry_tutor_id.get()
       student_id = entry_student_id.get()


       if session_id and session_number and session_date and start_time and end_time and tutor_id and student_id:
           update_session(session_id, session_number, session_date, start_time, end_time, tutor_id, student_id)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   # Creating the form
   root = tk.Tk()
   root.title("Session Management")


   tk.Label(root, text="Session ID:").grid(row=0, column=0, padx=10, pady=10)
   entry_session_id = tk.Entry(root)
   entry_session_id.grid(row=0, column=1, padx=10, pady=10)


   tk.Label(root, text="Session Number:").grid(row=1, column=0, padx=10, pady=10)
   entry_session_number = tk.Entry(root)
   entry_session_number.grid(row=1, column=1, padx=10, pady=10)


   tk.Label(root, text="Session Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
   entry_session_date = tk.Entry(root)
   entry_session_date.grid(row=2, column=1, padx=10, pady=10)


   tk.Label(root, text="Start Time (HH:MM:SS):").grid(row=3, column=0, padx=10, pady=10)
   entry_start_time = tk.Entry(root)
   entry_start_time.grid(row=3, column=1, padx=10, pady=10)


   tk.Label(root, text="End Time (HH:MM:SS):").grid(row=4, column=0, padx=10, pady=10)
   entry_end_time = tk.Entry(root)
   entry_end_time.grid(row=4, column=1, padx=10, pady=10)


   tk.Label(root, text="Tutor ID:").grid(row=5, column=0, padx=10, pady=10)
   entry_tutor_id = tk.Entry(root)
   entry_tutor_id.grid(row=5, column=1, padx=10, pady=10)


   tk.Label(root, text="Student ID:").grid(row=6, column=0, padx=10, pady=10)
   entry_student_id = tk.Entry(root)
   entry_student_id.grid(row=6, column=1, padx=10, pady=10)


   tk.Button(root, text="Insert Session", command=submit).grid(row=7, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Update Session", command=update).grid(row=8, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Show All Sessions", command=display_sessions).grid(row=9, column=0, columnspan=2, pady=10)


   root.mainloop()




# Run the form
create_form()
