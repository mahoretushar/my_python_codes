import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User Info
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if first_name and last_name:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Course Info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print(f"First Name: {first_name}, Last Name: {last_name}")
            print(f"Title: {title}, Age: {age}, Nationality: {nationality}")
            print(f"# Courses: {numcourses}, # Semester: {numsemesters}")
            print(f"Registration Status: {registration_status}")
            print("---------------------------------------------------------")

            # Create Table
            conn = sqlite3.connect("data.db")

            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
                                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
                                    registration_status TEXT, num_courses INT, num_semesters INT)'''

            conn.execute(table_create_query)

            # Insert Data
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, 
            title, age, nationality, registration_status, num_courses, num_semesters) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (
                first_name, last_name, title, age, nationality, registration_status, numcourses, numsemesters)

            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            conn.close()


        else:
            tkinter.messagebox.showwarning(title="Error",
                                           message="First Name and Last Name is Mandatory.")
    else:
        tkinter.messagebox.showwarning(title="Error",
                                       message="You have not accepted the Terms and Conditions")


window = tkinter.Tk()
window.title("Data Entry App")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Information
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["India", "Asia", "Africa", "Europe", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semester")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept Terms
terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terns_check = tkinter.Checkbutton(terms_frame, text="I accept the Terms and Conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terns_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
