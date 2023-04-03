import tkinter
from tkinter import ttk
from tkinter import messagebox
#collection of themed widgets allowing us to create more modern tkinter

def enter_data():
  #get the contents of the entry
  accepted = accept_var.get()

  if accepted == 'Accepted':
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    if firstname and lastname:
      title = title_combobox.get()
      age = age_spinbox.get()
      nationality = nationality_combobox.get()
      registration_status = reg_status_var.get()
      address = address_entry.get()
      zipcode = zipcode_entry.get()
      city = city_entry.get()
      cell = phone_entry.get()
      email = email_entry.get()
      
     #Printing out all the data out  
      print('First Name: ', firstname, 'Last Name:', lastname, 'Title: ', title)
      print('Age: ', age, 'Nationality: ', nationality)
      courses = numcourses_spinbox.get()
      print('Completed Courses: ', courses)
      print('Registration Status: ', registration_status)
      print('Address: ', address, 'Zip Code: ', zipcode, '\n City: ', city, 'CellPhone: ', cell, '\n Email Address: ', email)
      print('--------------')
    else:
      tkinter.messagebox.showwarning(title='Error', message='First and Last names are required')
  else:
    tkinter.messagebox.showwarning(title='Error', message='You have not accepted the terms & condtions')







window = tkinter.Tk() #Creating the tkinter window
window.title('Data Entry Form')

#frame will contain inside the window (nested inside window)
frame = tkinter.Frame(window)
#pack/place grid 
frame.pack()

#saving User Info
#grid() - locates where it should be placed
user_info_frame = tkinter.LabelFrame(frame, text='User Information')
user_info_frame.grid(row=0, column=0, padx=20,pady=10)
#When Creating a label, 
#1. when adding a widget create and define widget 
#2. must pack, place or grid widget 
first_name_label = tkinter.Label(user_info_frame, text='First Name')
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text='Last Name')
last_name_label.grid(row=0, column=1)

#-----------------
#Creating the label entries

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

#------------------

title_label = tkinter.Label(user_info_frame, text='Title')
title_combobox = ttk.Combobox(user_info_frame,values=['Mr.', 'Ms.', 'Dr.', 'Miss']) # Allows to create a dropdown menu
title_label.grid(row=0,column=2)
title_combobox.grid(row=1, column=2)

#Create a counter for age allowing user to use the arrows to specify their age
age_label = tkinter.Label(user_info_frame, text='Age')
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110) #ranging age from 18 years - 110 years old
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = tkinter.Label(user_info_frame, text='Nationality')
nationality_combobox = ttk.Combobox(user_info_frame,values=['Africa', 'Antartica', 'Asia', 'North America', 'South America', 'Europe'])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)


#To space out all the padding labels
for widget in user_info_frame.winfo_children():
  widget.grid_configure(padx=10,pady=5)
#------------- creating labels and entries
# Personal Info
personal_frame = tkinter.LabelFrame(frame, text='Personal Information')
personal_frame.grid(row=3,column=0, padx=20,pady=20, sticky='NW')

#Labels and Entries
address_label = tkinter.Label(personal_frame, text='Address')
address_label.grid(row=4,column=0)
address_entry = tkinter.Entry(personal_frame)
address_entry.grid(row=4, column=1)

zipcode_label = tkinter.Label(personal_frame, text='Zip Code')
zipcode_label.grid(row=4, column=2)
zipcode_entry = tkinter.Entry(personal_frame)
zipcode_entry.grid(row=4, column=3)

city_label = tkinter.Label(personal_frame, text='City')
city_label.grid(row=5, column=0)
city_entry = tkinter.Entry(personal_frame)
city_entry.grid(row=5, column=1)

phone_label = tkinter.Label(personal_frame, text='Cellphone')
phone_label.grid(row=5,column=2)
phone_entry = tkinter.Entry(personal_frame)
phone_entry.grid(row=5,column=3)

email_label = tkinter.Label(personal_frame, text='Email')
email_label.grid(row=6,column=0)
email_entry = tkinter.Entry(personal_frame)
email_entry.grid(row=6,column=1)

for widget in personal_frame.winfo_children():
  widget.grid_configure(padx=10, pady=5)



#Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky='news',padx=20,pady=20)
#sticky allows us to expand the box 'news mean north,east,west,south' and adding the padding allows use to use a normal size window
registered_label = tkinter.Label(courses_frame, text='Registration Status')

reg_status_var = tkinter.StringVar(value='Not Registered') #Will allow to print a statement when checkbox is checked


registered_check = tkinter.Checkbutton(courses_frame, text='Currently Registered', variable=reg_status_var, onvalue = 'Registered', offvalue = 'Not Registered')

registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

registration_status = reg_status_var.get() 

numcourses_label = tkinter.Label(courses_frame, text='# Completed Courses')
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity') #infinity will not set a maxium
numcourses_label.grid(row=0,column=2)
numcourses_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
  widget.grid_configure(padx=10,pady=5)

#Accept Terms and Conditions
terms_frame = tkinter.LabelFrame(frame,text='Terms and Conditions')
terms_frame.grid(row=2, column=0, sticky='news', padx=20,pady=10)

accept_var = tkinter.StringVar(value='Not Accepted')


terms_check = tkinter.Checkbutton(terms_frame,text='Accept Terms & Conditions', variable=accept_var, onvalue ='Accepted', offvalue = 'Not Accepted')
terms_check.grid(row=0,column=0)

#Button
button = tkinter.Button(frame, text='Submit', command= enter_data)
button.grid(row=5,column=0, padx=20, pady=10)







window.mainloop() #run a infinte loop until you exit the application basically creating the actual main window
