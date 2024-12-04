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




# Function to insert a new rating into the database
def insert_rating(rating_id, rating_value, feedback, session_id, student_id):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               INSERT INTO Rating (RatingID, RatingValue, Feedback, SessionID, StudentID)
               VALUES (%s, %s, %s, %s, %s)
           """
           cursor.execute(query, (rating_id, rating_value, feedback, session_id, student_id))
           connection.commit()
           messagebox.showinfo("Success", "Rating inserted successfully!")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to insert rating: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to update an existing rating
def update_rating(rating_id, rating_value, feedback, session_id, student_id):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               UPDATE Rating
               SET RatingValue = %s, Feedback = %s, SessionID = %s, StudentID = %s
               WHERE RatingID = %s
           """
           cursor.execute(query, (rating_value, feedback, session_id, student_id, rating_id))
           connection.commit()
           if cursor.rowcount > 0:
               messagebox.showinfo("Success", "Rating updated successfully!")
           else:
               messagebox.showwarning("Warning", "Rating ID not found.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to update rating: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to display all ratings
def display_ratings():
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = "SELECT * FROM Rating"
           cursor.execute(query)
           ratings = cursor.fetchall()
           rating_list = "\n".join([
               f"ID: {rating[0]}, Value: {rating[1]}, Feedback: {rating[2]}, SessionID: {rating[3]}, StudentID: {rating[4]}"
               for rating in ratings
           ])
           if rating_list:
               messagebox.showinfo("All Ratings", rating_list)
           else:
               messagebox.showinfo("All Ratings", "No ratings available.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to fetch ratings: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Tkinter GUI
def create_form():
   def submit():
       rating_id = entry_rating_id.get()
       rating_value = entry_rating_value.get()
       feedback = entry_feedback.get()
       session_id = entry_session_id.get()
       student_id = entry_student_id.get()


       if rating_id and rating_value and feedback and session_id and student_id:
           insert_rating(rating_id, rating_value, feedback, session_id, student_id)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   def update():
       rating_id = entry_rating_id.get()
       rating_value = entry_rating_value.get()
       feedback = entry_feedback.get()
       session_id = entry_session_id.get()
       student_id = entry_student_id.get()


       if rating_id and rating_value and feedback and session_id and student_id:
           update_rating(rating_id, rating_value, feedback, session_id, student_id)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   # Creating the form
   root = tk.Tk()
   root.title("Rating Management")


   tk.Label(root, text="Rating ID:").grid(row=0, column=0, padx=10, pady=10)
   entry_rating_id = tk.Entry(root)
   entry_rating_id.grid(row=0, column=1, padx=10, pady=10)


   tk.Label(root, text="Rating Value:").grid(row=1, column=0, padx=10, pady=10)
   entry_rating_value = tk.Entry(root)
   entry_rating_value.grid(row=1, column=1, padx=10, pady=10)


   tk.Label(root, text="Feedback:").grid(row=2, column=0, padx=10, pady=10)
   entry_feedback = tk.Entry(root)
   entry_feedback.grid(row=2, column=1, padx=10, pady=10)


   tk.Label(root, text="Session ID:").grid(row=3, column=0, padx=10, pady=10)
   entry_session_id = tk.Entry(root)
   entry_session_id.grid(row=3, column=1, padx=10, pady=10)


   tk.Label(root, text="Student ID:").grid(row=4, column=0, padx=10, pady=10)
   entry_student_id = tk.Entry(root)
   entry_student_id.grid(row=4, column=1, padx=10, pady=10)


   tk.Button(root, text="Insert Rating", command=submit).grid(row=5, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Update Rating", command=update).grid(row=6, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Show All Ratings", command=display_ratings).grid(row=7, column=0, columnspan=2, pady=10)


   root.mainloop()




# Run the form
create_form()

