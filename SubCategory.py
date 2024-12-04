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




# Function to insert a new subcategory into the database
def insert_subcategory(subcategory_id, subcategory_name, sub_description):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               INSERT INTO SubCategory (SubCategoryID, SubCategoryName, SubDescription)
               VALUES (%s, %s, %s)
           """
           cursor.execute(query, (subcategory_id, subcategory_name, sub_description))
           connection.commit()
           messagebox.showinfo("Success", "SubCategory inserted successfully!")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to insert subcategory: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to update an existing subcategory
def update_subcategory(subcategory_id, subcategory_name, sub_description):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               UPDATE SubCategory
               SET SubCategoryName = %s, SubDescription = %s
               WHERE SubCategoryID = %s
           """
           cursor.execute(query, (subcategory_name, sub_description, subcategory_id))
           connection.commit()
           if cursor.rowcount > 0:
               messagebox.showinfo("Success", "SubCategory updated successfully!")
           else:
               messagebox.showwarning("Warning", "SubCategory ID not found.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to update subcategory: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to display all subcategories
def display_subcategories():
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = "SELECT * FROM SubCategory"
           cursor.execute(query)
           subcategories = cursor.fetchall()
           subcategory_list = "\n".join([
               f"ID: {subcategory[0]}, Name: {subcategory[1]}, Description: {subcategory[2]}"
               for subcategory in subcategories
           ])
           if subcategory_list:
               messagebox.showinfo("All SubCategories", subcategory_list)
           else:
               messagebox.showinfo("All SubCategories", "No subcategories available.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to fetch subcategories: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Tkinter GUI
def create_form():
   def submit():
       subcategory_id = entry_subcategory_id.get()
       subcategory_name = entry_subcategory_name.get()
       sub_description = entry_sub_description.get()


       if subcategory_id and subcategory_name and sub_description:
           insert_subcategory(subcategory_id, subcategory_name, sub_description)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   def update():
       subcategory_id = entry_subcategory_id.get()
       subcategory_name = entry_subcategory_name.get()
       sub_description = entry_sub_description.get()


       if subcategory_id and subcategory_name and sub_description:
           update_subcategory(subcategory_id, subcategory_name, sub_description)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   # Creating the form
   root = tk.Tk()
   root.title("SubCategory Management")


   tk.Label(root, text="SubCategory ID:").grid(row=0, column=0, padx=10, pady=10)
   entry_subcategory_id = tk.Entry(root)
   entry_subcategory_id.grid(row=0, column=1, padx=10, pady=10)


   tk.Label(root, text="SubCategory Name:").grid(row=1, column=0, padx=10, pady=10)
   entry_subcategory_name = tk.Entry(root)
   entry_subcategory_name.grid(row=1, column=1, padx=10, pady=10)


   tk.Label(root, text="Description:").grid(row=2, column=0, padx=10, pady=10)
   entry_sub_description = tk.Entry(root)
   entry_sub_description.grid(row=2, column=1, padx=10, pady=10)


   tk.Button(root, text="Insert SubCategory", command=submit).grid(row=3, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Update SubCategory", command=update).grid(row=4, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Show All SubCategories", command=display_subcategories).grid(row=5, column=0, columnspan=2, pady=10)


   root.mainloop()




# Run the form
create_form()
