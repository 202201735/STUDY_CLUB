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




# Function to insert a new category into the database
def insert_category(category_id, category_name, category_description, subject_id, sub_category):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               INSERT INTO Category (CategoryID, CategoryName, CategoryDescription, SubjectID, SubCategory)
               VALUES (%s, %s, %s, %s, %s)
           """
           cursor.execute(query, (category_id, category_name, category_description, subject_id, sub_category))
           connection.commit()
           messagebox.showinfo("Success", "Category inserted successfully!")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to insert category: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to update an existing category
def update_category(category_id, category_name, category_description, subject_id, sub_category):
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = """
               UPDATE Category
               SET CategoryName = %s, CategoryDescription = %s, SubjectID = %s, SubCategory = %s
               WHERE CategoryID = %s
           """
           cursor.execute(query, (category_name, category_description, subject_id, sub_category, category_id))
           connection.commit()
           if cursor.rowcount > 0:
               messagebox.showinfo("Success", "Category updated successfully!")
           else:
               messagebox.showwarning("Warning", "Category ID not found.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to update category: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Function to display all categories
def display_categories():
   connection = create_connection()
   if connection:
       cursor = connection.cursor()
       try:
           query = "SELECT * FROM Category"
           cursor.execute(query)
           categories = cursor.fetchall()
           category_list = "\n".join([
               f"ID: {category[0]}, Name: {category[1]}, Description: {category[2]}, SubjectID: {category[3]}, SubCategory: {category[4]}"
               for category in categories
           ])
           if category_list:
               messagebox.showinfo("All Categories", category_list)
           else:
               messagebox.showinfo("All Categories", "No categories available.")
       except mysql.connector.Error as err:
           messagebox.showerror("Error", f"Failed to fetch categories: {err}")
       finally:
           cursor.close()
           connection.close()
   else:
       messagebox.showerror("Error", "Failed to connect to the database")




# Tkinter GUI
def create_form():
   def submit():
       category_id = entry_category_id.get()
       category_name = entry_category_name.get()
       category_description = entry_category_description.get()
       subject_id = entry_subject_id.get()
       sub_category = entry_sub_category.get()


       if category_id and category_name and category_description and subject_id and sub_category:
           insert_category(category_id, category_name, category_description, subject_id, sub_category)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   def update():
       category_id = entry_category_id.get()
       category_name = entry_category_name.get()
       category_description = entry_category_description.get()
       subject_id = entry_subject_id.get()
       sub_category = entry_sub_category.get()


       if category_id and category_name and category_description and subject_id and sub_category:
           update_category(category_id, category_name, category_description, subject_id, sub_category)
       else:
           messagebox.showerror("Error", "Please fill in all fields")


   # Creating the form
   root = tk.Tk()
   root.title("Category Management")


   tk.Label(root, text="Category ID:").grid(row=0, column=0, padx=10, pady=10)
   entry_category_id = tk.Entry(root)
   entry_category_id.grid(row=0, column=1, padx=10, pady=10)


   tk.Label(root, text="Category Name:").grid(row=1, column=0, padx=10, pady=10)
   entry_category_name = tk.Entry(root)
   entry_category_name.grid(row=1, column=1, padx=10, pady=10)


   tk.Label(root, text="Description:").grid(row=2, column=0, padx=10, pady=10)
   entry_category_description = tk.Entry(root)
   entry_category_description.grid(row=2, column=1, padx=10, pady=10)


   tk.Label(root, text="Subject ID:").grid(row=3, column=0, padx=10, pady=10)
   entry_subject_id = tk.Entry(root)
   entry_subject_id.grid(row=3, column=1, padx=10, pady=10)


   tk.Label(root, text="SubCategory:").grid(row=4, column=0, padx=10, pady=10)
   entry_sub_category = tk.Entry(root)
   entry_sub_category.grid(row=4, column=1, padx=10, pady=10)


   tk.Button(root, text="Insert Category", command=submit).grid(row=5, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Update Category", command=update).grid(row=6, column=0, columnspan=2, pady=10)
   tk.Button(root, text="Show All Categories", command=display_categories).grid(row=7, column=0, columnspan=2, pady=10)


   root.mainloop()




# Run the form
create_form()
