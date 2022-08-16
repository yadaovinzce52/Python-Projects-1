from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ''

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.configure(text='Timer', fg=GREEN)
    check_mark.configure(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.configure(text='Break', fg=RED)
        countdown(long_break)
    elif reps % 2 == 0:
        timer_label.configure(text='Break', fg=PINK)
        countdown(short_break)
    else:
        timer_label.configure(text='Work', fg=GREEN)
        countdown(work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(counter):
    minutes = math.floor(counter / 60)
    seconds = counter % 60

    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if counter > 0:
        global timer
        timer = window.after(1000, countdown, counter - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'
        check_mark.configure(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.configure(padx=100, pady=100, bg=YELLOW)

# displays check mark
check_mark = Label(fg=GREEN, font=(FONT_NAME, 15, 'bold'),
                   bg=YELLOW, highlightthickness=0)
check_mark.grid(row=3, column=1)

# Canvas creation to add tomato image
# make canvas dimensions even
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=background)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# Timer label
timer_label = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), bg=YELLOW, highlightthickness=0, fg=GREEN)
timer_label.grid(row=0, column=1)

# Start Button
start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

# Reset Button
reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()
