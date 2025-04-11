from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Courier", 10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters) ]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols) ]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers) ]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    gen_password = "".join(password_list)

    pyperclip.copy(gen_password)
    password_entry.delete(0, END)
    password_entry.insert(0, gen_password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found, use 'Add' to make a new one.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Website not found", message=f"{website} is not saved, please use the 'Add'"
                                                                   f" button to save your data to that website.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_contents():
    # print(website_entry.get())
    web_entry = website_entry.get()
    pass_entry = password_entry.get()
    user_entry = email_user_entry.get()

    web_stripped = web_entry.strip()
    pass_stripped = pass_entry.strip()
    user_stripped = user_entry.strip()

    new_data = {
        web_entry: {
            "email": user_entry,
            "password": pass_entry,
        }
    }

    if len(web_stripped) <= 0 or len(pass_stripped) <= 0 or len(user_stripped) <= 0:
        messagebox.showinfo(title="Invalid Input", message="Please do not leave fields empty.")
    else:
       # check = messagebox.askokcancel(title="Check Entry", message="Do you wish to save current inputs?")
       #
       # if check:

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            # Optional use if you don't use the same email for multiple sites
            # email_user_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showinfo(title="Data Saved", message="Data has been saved successfully")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0, sticky=E)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.place(x=268, y=200)

email_user_label = Label(text="Email/Username:", font=FONT)
email_user_label.grid(row=2, column=0, sticky=E)

email_user_entry = Entry(width=42)
email_user_entry.grid(row=2, column=1, columnspan=3, sticky=W)

password_label = Label(text="Password:", font=FONT, )
password_label.grid(row=3, column=0, sticky=E)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W)

password_blankspace = Label(text="Password Button Goes Here", fg="#F0F0F0")
password_blankspace.grid(row=3, column=2, sticky=W)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.place(x=269, y=245)

add_button = Button(text="Add",width=35, command=add_contents)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()