from Tkinter import *
from PIL import ImageTk,Image 
import sqlite3

root = Tk()
root.title('Creating checkboxes')
root.geometry("400x400")

# databases
# create a databses or connect to one
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

'''
# create table
c.execute("""CREATE TABLE addresses (
		first_name text,
		last_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")
'''

# create submit function for database

def submit():
	# because we need to connect to database
	# connect to database
	conn = sqlite3.connect('address_book.db')

	# create cursor
	c = conn.cursor()

	# insert into table 
	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
			{
				'f_name' : f_name.get(),
				'l_name' : l_name.get(),
				'address' : address.get(),
				'city' : city.get(),
				'state' : state.get(),
				'zipcode' : zipcode.get() 
			}
			)

	# commit changes to database
	conn.commit()

	#close connection
	conn.close()

	# clear the text boxes
	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)

# create query function
def query():
	# because we still need to connect to the database again

	# connect to database
	conn = sqlite3.connect('address_book.db')

	# create cursor
	c = conn.cursor()	

	# To query the database
	c.execute("SELECT *, oid FROM addresses") # oid is the primary key or unique id of each entry/record
	my_record = c.fetchall()
	#print(my_record)
	print_records = ''

	# loop through Results
	for record in my_record:
		print_records += str(record) + " " + str(record[6]) + "\n"

	query_label = Label (root, text= print_records)
	query_label.grid(row=8, column= 0, columnspan=2)

	# commit changes to database
	conn.commit()

	#close connection
	conn.close()

	


# Create text boxes
f_name= Entry(root, width=30)
f_name.grid(row=0, column =1, padx=20)
l_name= Entry(root, width=30)
l_name.grid(row=1, column =1)
address= Entry(root, width=30)
address.grid(row=2, column =1)
city= Entry(root, width=30)
city.grid(row=3, column =1)
state= Entry(root, width=30)
state.grid(row=4, column =1)
zipcode= Entry(root, width=30)
zipcode.grid(row=5, column =1)

# create text box label
f_name_label= Label (root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label= Label (root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label= Label (root, text="Adreess")
address_label.grid(row=2, column=0)
city_label= Label (root, text="City")
city_label.grid(row=3, column=0)
state_label= Label (root, text="State")
state_label.grid(row=4, column=0)
zipcode_label= Label (root, text="Zip code")
zipcode_label.grid(row=5, column=0)

# create submit button
submit_btn = Button (root, text="Add Record to Database", command= submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx= 10, ipadx=100)

# Create a Query button

query_btn= Button(root, text="Display Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# commit changes to database
conn.commit()

#close connection
conn.close()


root.mainloop() 