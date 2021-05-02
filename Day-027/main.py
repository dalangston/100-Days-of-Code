import tkinter
#from tkinter import Tk, Button, Entry, Label


def mi_to_km():
    
    miles = float(in_units.get())
    km = 1.609344 * miles
    result.config(text=str(km))


window = tkinter.Tk()
window.title('Mile to Km Contersion')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

input_units = tkinter.Label(text='Miles', padx=10)
output_units = tkinter.Label(text='Km', padx=10)
output_label = tkinter.Label(text='is equal to', padx=10)
result = tkinter.Label(text='0', padx=10, pady=10)

in_units = tkinter.Entry(width=10)
in_units.insert(0, string='0')

button = tkinter.Button(text='Calculate', command=mi_to_km)


# Layout Window Grid
output_label.grid(column=0, row=1)
in_units.grid(column=1, row=0)
input_units.grid(column=2, row=0)
result.grid(column=1, row=1)
button.grid(column=1, row=2)
output_units.grid(column=2, row=1)

window.mainloop()