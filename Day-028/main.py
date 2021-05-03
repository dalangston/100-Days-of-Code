from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'
#----------------------------- GLOBALS ----------------------------------- #
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    
    global timer
    global reps
    
    window.after_cancel(timer)
    
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    completed_label.config(text="")
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    
    global reps
    
    reps = (reps + 1) % 8
    
    if reps == 0:
        timer_label.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 != 0:
        timer_label.config(text='Work', fg=GREEN)
        count_down(WORK_MIN * 60)
    else:
        timer_label.config(text='Break', fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    global reps
    global timer
    
    min = floor(count / 60)
    sec = count % 60
    
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # args= time(ms), function_name, *args passed to function_name
    else:
        if reps % 2 == 0:
            completed_label.config(text=f"{completed_label.cget('text')} {CHECK_MARK}")
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='./tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 48, 'normal'))
start_button = Button(text='Start', fg=GREEN, highlightthickness=0, command=start_timer)
reset_button = Button(text='Reset', fg=GREEN, highlightthickness=0, command=reset_timer)
#completed_label = Label(text=CHECK_MARK, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 22, 'normal'))
completed_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 22, 'normal'))

# Window Layout
timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
completed_label.grid(column=1, row=3)


window.mainloop()