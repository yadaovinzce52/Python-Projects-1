from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    site_to_search = site_entry.get().title()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    else:
        if site_to_search in data:
            email = data[site_to_search]['email']
            password = data[site_to_search]['password']
            messagebox.showinfo(title=site_to_search, message=f'Email: {email}\n\nPassword: {password}')
        else:
            messagebox.showinfo(title='No website info saved', message=f'No details for {site_to_search} exists')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    passwd_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters = [choice(letters) for _ in range(randint(5, 10))]
    pwd_symbols = [choice(symbols) for _ in range(randint(2, 5))]
    pwd_numbers = [choice(numbers) for _ in range(randint(2, 5))]

    password_list = pwd_letters + pwd_symbols + pwd_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passwd_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = site_entry.get().title()
    email = user_entry.get()
    passwd = passwd_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': passwd,
        }
    }

    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title='Empty Fields', message='Please don\'t leave any fields empty!')
    else:
        try:
            with open(file='data.json', mode='r') as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # Create new json file
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)
        finally:
            site_entry.delete(0, END)
            passwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Create Password Manager window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Create Canvas for logo
canvas = Canvas(width=200, height=200)
background = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=background)
canvas.grid(row=0, column=1)

# ------------------------------Labels------------------------------ #
# Website Label
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

# Email/Username Label
user_label = Label(text='Email/Username:')
user_label.grid(row=2, column=0)

# Password Label
passwd_label = Label(text='Password:')
passwd_label.grid(row=3, column=0)

# ------------------------------Entries------------------------------ #
# Website Entry
site_entry = Entry(width=17)
site_entry.grid(row=1, column=1)
site_entry.focus()

# Email/Username entry
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(index=END, string='yadaovinzce@gmail.com')

# Password Entry
passwd_entry = Entry(width=17)
passwd_entry.grid(row=3, column=1)

# ------------------------------Buttons------------------------------ #
# Generate Password Button
generate = Button(text='Generate Password', command=generate_password)
generate.grid(row=3, column=2)

# Add Button
add = Button(text='Add', command=add_password, width=30)
add.grid(row=4, column=1, columnspan=2)

# Search Button
search = Button(text='Search', command=search_website, width=14)
search.grid(row=1, column=2)

window.mainloop()
