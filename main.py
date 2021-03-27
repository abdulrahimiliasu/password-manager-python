from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR -------------------------------


def find_password():
    website = ent_website.get()
    if len(website) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields before adding")
    else:
        try:
            with open('data.json', mode='r') as file:
                try:
                    data = json.load(file)
                    details = data[website]
                except KeyError:
                    messagebox.showerror(title="Error", message=f"No Details For {website} Found")
                else:
                    messagebox.showinfo(title=website, message=f"Email: {details['email']}\n"
                                                               f"Password: {details['password']}\n")
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found")


def generate_password():
    password = Password()
    pyperclip.copy(password.generate())
    ent_pass.insert(0, password.generate())

# ---------------------------- SAVE PASSWORD -------------------------------


def save():
    website = ent_website.get()
    email = ent_email.get()
    password = ent_pass.get()
    new_data = {website: {
            'email': email,
            'password': password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields before adding")
    else:
        confirmed = messagebox.askyesno(title=website, message=f"Do you want to save the details below?\n Email: "
                                                               f"{email}\n Password: {password}")
        if confirmed:
            try:
                with open('data.json', mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    json.dump(data, file, indent=4)
            else:
                with open('data.json', mode='w') as file:
                    data = json.load(file)
                    data.update(new_data)
                    json.dump(data, file, indent=4)
            finally:
                ent_website.delete(0, END)
                ent_pass.delete(0, END)

# ---------------------------- UI SETUP -------------------------------


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Texts
text_website = Label(text="Website:")
text_website.grid(row=1, column=0)
text_email = Label(text="Email/Username:")
text_email.grid(row=2, column=0)
text_pass = Label(text="Password:")
text_pass.grid(row=3, column=0)

# Entries
ent_website = Entry(width=21)
ent_website.focus()
ent_website.grid(row=1, column=1)
ent_email = Entry(width=35)
ent_email.grid(row=2, column=1, columnspan=2)
ent_email.insert(0, "abduliliasu69@gmail.com")
ent_pass = Entry(width=21)
ent_pass.grid(row=3, column=1)

# Buttons
generate_password_bttn = Button(text="Generate Password", command=generate_password)
generate_password_bttn.grid(row=3, column=2)
add_bttn = Button(text="Add", width=36, command=save)
add_bttn.grid(row=4, column=1, columnspan=2)
search_bttn = Button(text="Search", width=13, command=find_password)
search_bttn.grid(row=1, column=2)

window.mainloop()
