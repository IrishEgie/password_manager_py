from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_pass():
    info = f"Website: {web_ent.get()} \nEmail/Username: {eun_ent.get()} \nPass: {pass_ent.get()}"
    print(info)
    with open("passtext_py.txt", mode="w") as file:
        file.write(info)

    web_ent.delete(0,END)
    pass_ent.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#create a canvas & an image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_pic)

# labels
web_lbl = Label(text="Website:")
eun_lbl = Label(text="Email/Username: ")
pass_lbl = Label(text="Password: ") 

#entry fields
web_ent = Entry(width=51)
web_ent.focus()
eun_ent = Entry(width=51)
eun_ent.insert(0, "hotpepoy@gmail.com")
pass_ent = Entry(width=33)

#button
genpass_btn = Button(text="Generate Password")
addpass_btn = Button(text="Add", width=43,command=write_pass)


#UI Layout
canvas.grid(column=1, row=0)
web_lbl.grid(column=0, row=1)
eun_lbl.grid(column=0, row=2)
pass_lbl.grid(column=0, row=3)

web_ent.grid(column=1, row=1, columnspan = 2)
eun_ent.grid(column=1, row=2, columnspan = 2)
pass_ent.grid(column=1, row=3)

genpass_btn.grid(column=2, row=3)
addpass_btn.grid(column=1, row=4, columnspan = 2)

window.mainloop()
