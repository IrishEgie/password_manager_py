from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genpass_rd():
    pass_ent.delete(0,END)    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rd_pass_l = [rd.choice(letters) for rep in range(rd.randint(8,10))]
    rd_pass_s = [rd.choice(numbers) for rep in range(rd.randint(2,4))]
    rd_pass_n = [rd.choice(symbols) for rep in range(rd.randint(2,4))]

    password_list = rd_pass_l+rd_pass_n+rd_pass_s
    rd.shuffle(password_list)

    password = ''.join(password_list)
    pass_ent.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_pass():
    website = web_ent.get()
    eun = eun_ent.get()
    password = pass_ent.get() 
    info = f"Website: {website} \nEmail/Username: {eun} \nPass: {password}\n\n"
    # print(info)

    new_data = {
        website: {
            "email":eun,
            "password":password
        }
    }
    # Basic input validation for website and password length
    if len(website) < 3 or len(password) < 5:
        messagebox.showinfo(title="Missing Fields", message="Please do not leave fields empty")
    else:
        try:
            # Try to read the existing data from the file
            with open("passtext_py.json", mode="r") as file:
                # Check if the file is empty before loading
                content = file.read().strip()
                if content:
                    data = json.loads(content)
                else:
                    data = {}
        except FileNotFoundError:
            # If the file is not found, create a new one
            with open("passtext_py.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
            print("File not found, creating new passtext_py.json file!")
        else:
            # Update existing data with the new entry
            data.update(new_data)
            with open("passtext_py.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            # Clear the input fields after saving
            web_ent.delete(0, END)
            pass_ent.delete(0, END)
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
genpass_btn = Button(text="Generate Password", command=genpass_rd)
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
