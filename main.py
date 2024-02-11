import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
passwd = tkinter.Entry(width=31)
passwd.grid(row=3, column=1)

# Password generator Button
passwd_button = tkinter.Button(text="Generate Password", highlightthickness=0, font=("Arial", 8))
passwd_button.grid(column=2, row=3)
# Add button
add_button = tkinter.Button(text="Add", width=40)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
