import random
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    
    password_list += [random.choice(letters) for x in range(nr_letters)]
    password_list += [random.choice(numbers) for x in range(nr_numbers)]
    password_list += [random.choice(symbols) for x in range(nr_symbols)]

    random.shuffle(password_list)
    
    pw = ''.join(password_list)
    
    pass_entry.delete(0, END)
    pass_entry.insert(0, pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def wirte_data():
    
    site_id = web_entry.get()
    user_id = uid_entry.get()
    password = pass_entry.get()
    
    line = f'{site_id}|{user_id}|{password}\n'
    
    msg=""
    
    if len(site_id) == 0:
        msg += "Site Name Not Provided\n"
    if len(user_id) == 0:
        msg += "Emain/Username Not Provided\n"
    if len(password) == 0:
        msg += "Password Not Provided\n"
        
    if msg:
        messagebox.showinfo(message=msg)
        return
    
    is_ok = messagebox.askokcancel(
        title=site_id, 
        message=f"These are the details entered:\n\nEmail: {user_id}\nPassword: {password}\n"
    )

    if is_ok:
        with open('data.txt', 'a') as f:
            f.write(line)
        
        clear_fields()
        

def clear_fields():

    web_entry.delete(0, END)
    pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=logo)

web_label = Label(text='Website:')
uid_label = Label(text="Email/Username:")
pass_label = Label(text='Password:')

web_entry = Entry(width=35)
uid_entry = Entry(width=35)
pass_entry = Entry(width=21)

gen_button = Button(text='Generate Password', command=gen_pass)
add_button = Button(text='Add', width=36, command=wirte_data)

# == Window Layout == #
canvas.grid(column=1, row=0)
web_label.grid(column=0, row=1)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
uid_label.grid(column=0, row=2)
uid_entry.grid(column=1, row=2, columnspan=2)
uid_entry.insert(0, 'example@example.com')
pass_label.grid(column=0, row=3)
pass_entry.grid(column=1, row=3)
gen_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()