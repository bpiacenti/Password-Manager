from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_contents():
    # print(website_entry.get())
    web_entry = website_entry.get()
    pass_entry = password_entry.get()
    user_entry = email_user_entry.get()

    web_stripped = web_entry.strip()
    pass_stripped = pass_entry.strip()
    user_stripped = user_entry.strip()

    if len(web_stripped) <= 0 or len(pass_stripped) <= 0 or len(user_stripped) <= 0:
        messagebox.showinfo(title="Invalid Input", message="Please do not leave fields empty.")
    else:
       check = messagebox.askokcancel(title="Check Entry", message="Do you wish to save current inputs?")

       if check:
            messagebox.showinfo(title="Data Saved", message="Data has been saved successfully")

            with open("data.txt", "a") as file:
                file.write(f"{web_stripped} | {user_stripped} | {pass_stripped}\n")
                website_entry.delete(0, END)
                # Optional use if you don't use the same email for multiple sites
                # email_user_entry.delete(0, END)
                password_entry.delete(0, END)
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

website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=3, sticky=W)
website_entry.focus()

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
generate_password_button.place(x=270, y=245)

add_button = Button(text="Add",width=35, command=add_contents)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)




window.mainloop()