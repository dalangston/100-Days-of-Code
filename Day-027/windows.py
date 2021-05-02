import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=380)
# Add space around window edge
window.config(padx=100, pady=200)

FONT = ('Arial', 24, 'normal')

# Create a text label
my_label = tkinter.Label(text="I am a Label", font=FONT)

# Place my_label inside the window
#my_label.pack(side="left")
#my_label.pack()

# Update Label
my_label['text'] = 'New Text'
my_label.config(text='New Text')
# Add Spcing around widgets
my_label.config(padx=50, pady=50)

# Button

def button_clicked():
    print("I got clicked")
    #my_label.config(text = 'I got clicked')
    my_label.config(text = text.get())

button = tkinter.Button(text='Click Me', command=button_clicked)
#button.pack()

new_button = tkinter.Button(text="New Button")

# Entry
text = tkinter.Entry(width=10)
#text.pack()

# Layout Challenge
# pack() attempts to "stack" elements
# place() allows exact placement within window
# grid() allows elements to placed relative to eachother in a grid pattern
# Connot combine other methods with pack() method
my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
text.grid(column=3, row=2)


# Keep window open
window.mainloop()
