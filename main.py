from tkinter import *
from tkinter import messagebox
import random as rd
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genpass_rd():    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = rd.randint(8,10)
    nr_symbols = rd.randint(2,4)
    nr_numbers = rd.randint(2,4)

    rd_pass = []

    for rep in range(nr_letters):
        rd_letter = rd.choice(letters)
        rd_pass.append(rd_letter) 
    for rep in range(nr_numbers):
        rd_num = rd.choice(numbers)
        rd_pass.append(rd_num)
    for rep in range(nr_symbols): 
        rd_sym = rd.choice(symbols)
        rd_pass.append(rd_sym) 

    rd.shuffle(rd_pass)

    password = ''.join(rd_pass)
    print()
    pass_ent.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_pass():
    website = web_ent.get()
    eun = eun_ent.get()
    password = pass_ent.get() 
    info = f"Website: {website} \nEmail/Username: {eun} \nPass: {password}\n\n"
    print(info)

    if len(website)<3 or len(password)<5:
        messagebox.showinfo(title="Missing Fields", message="Please do not leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: {info}Is it OK to save?") 
        
        if is_ok:
            with open("passtext_py.txt", mode="a") as file:
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
