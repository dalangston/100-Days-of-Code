import random
import json
from tkinter import *
from tkinter import messagebox


PW_FILE = './data.json'

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

def check_data():
    
    site_id = web_entry.get()
    user_id = uid_entry.get()
    password = pass_entry.get()
    
    msg=""
    
    if len(site_id) == 0:
        msg += "Site Name Not Provided\n"
    if len(user_id) == 0:
        msg += "Emain/Username Not Provided\n"
    if len(password) == 0:
        msg += "Password Not Provided\n"
        
    if msg:
        messagebox.showinfo(message=msg)
        return False
     
    return True


def wirte_data():
    
    site_id = web_entry.get()
    user_id = uid_entry.get()
    password = pass_entry.get()
    
    new_data = {
        site_id: {
            "email": user_id,
            "password": password,
        }
    }
    
    if not check_data():
       return

    try:
        with open(PW_FILE, 'r') as f:
            data = json.load(f)
            data.update(new_data)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        data = new_data

    with open(PW_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    
    clear_fields()
        

def clear_fields():

    web_entry.delete(0, END)
    pass_entry.delete(0, END)

# ---------------------------- Search PASSWORD ------------------------------- #

def get_pass():

    site_id = web_entry.get()
    
    if len(site_id) == 0:
        messagebox.showinfo(message="Website is blank")
        return

    try:
        with open(PW_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found")
    else:
        if site_id in data:
            site_data = data[site_id]
            
            msg = f"Username:  {site_data['email']}\nPassword:  {site_data['password']}"
            messagebox.showinfo(title=site_id, message=str(msg))

        else:
            messagebox.showinfo(message=f"Website {site_id} not found")


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

web_entry = Entry(width=20)
uid_entry = Entry(width=35)
pass_entry = Entry(width=21)

gen_button = Button(text='Generate Password', command=gen_pass)
add_button = Button(text='Add', width=36, command=wirte_data)
search_button = Button(text='Search', command=get_pass)

# == Window Layout == #
canvas.grid(column=1, row=0)
web_label.grid(column=0, row=1)
web_entry.grid(column=1, row=1)
web_entry.focus()
search_button.grid(column=2, row=1)
uid_label.grid(column=0, row=2)
uid_entry.grid(column=1, row=2, columnspan=2)
uid_entry.insert(0, 'example@example.com')
pass_label.grid(column=0, row=3)
pass_entry.grid(column=1, row=3)
gen_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()