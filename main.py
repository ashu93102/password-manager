import tkinter
from tkinter import messagebox
import random
import pyperclip
# To show popup we can use popup module
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    # below line is called list comprehension
    total_letters = [random.choice(letters) for _ in range(nr_letters)]
    total_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    total_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password = total_letters + total_symbols + total_numbers
    random.shuffle(password)
    # Converting list to string using map function of list comprehension
    new_pass = ''.join(map(str, password))

    passwd.insert(tkinter.END, new_pass)

    # Below line will make text for copy to clipboard
    pyperclip.copy(new_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #


class Data:
    def __init__(self, **kwargs):
        self.website_data = kwargs.get("website_data")
        self.email = kwargs.get("email")
        self.passw = kwargs.get("passw")


def userdata():
    """Gets data from tkinter entry widget and puts it into a text file"""
    website_data = website.get()
    email_user_name = email.get()
    site_password = passwd.get()

    # To show Popup message box, and it returns value as Boolean data type (true or false)
    if len(website_data) > 0 and len(site_password) > 0:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"email/username:-{email_user_name}\nPassword:-{site_password}\n"
                                               f" Do you want to save?")
        if is_ok:
            with open("userdata.txt", "a") as file:
                file.write(
                    "website:- " + website_data + "/ " + "email/username:-" + email_user_name + "/ " + "Password:-"
                    + site_password + "\n")
    else:
        messagebox.showwarning(title="Data Empty", message="Please fill blank fields")

    website.delete(0, tkinter.END)
    passwd.delete(0, tkinter.END)
    # below line shows python class and put data into class
    user_input_data = Data(website_data=website_data, email=email_user_name, passw=site_password)
    print(user_input_data.website_data)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas_logo = tkinter.Canvas(width=200, height=200)
item_logo = tkinter.PhotoImage(file="logo.png")
canvas_logo.create_image(100, 100, image=item_logo)
canvas_logo.grid(column=1, row=0)

# Logo website
web_logo = tkinter.Label(text="Website:")
web_logo.grid(column=0, row=1)
# Logo Email
email_logo = tkinter.Label(text="Email/Username:")
email_logo.grid(column=0, row=2)
# Logo Password
pass_logo = tkinter.Label(text="Password:")
pass_logo.grid(column=0, row=3)

# Entry
website = tkinter.Entry(width=48)
website.grid(column=1, row=1, columnspan=2)
website.focus()
# Entry
email = tkinter.Entry(width=48)
email.grid(column=1, row=2, columnspan=2)
email.insert(tkinter.END, "ashu@gmail.com")
# Entry
passwd = tkinter.Entry(width=31, show="*")
passwd.grid(row=3, column=1)

# Password generator Button
passwd_button = tkinter.Button(text="Generate Password", highlightthickness=0, font=("Arial", 8),
                               command=generate_passwd)
passwd_button.grid(column=2, row=3)
# Add button
add_button = tkinter.Button(text="Add", width=40, command=userdata)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
