import tkinter
import time
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
time_ = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    window.after_cancel(time_)
    canvas.itemconfig(time_text, text="00:00")
    title_label.config(text="Timer")
    checkmark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def work_display(text, color):
    title_label.config(text=text, fg=color)

def short_break_display(text, color):
    title_label.config(text=text, fg=color)

def long_break_display(text, color):
    title_label.config(text=text, fg=color)


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    

    if reps%8 == 0:
        long_break_display("Long Break", RED)
        count_down(long_break_sec)
    elif reps%2 == 0:
        short_break_display("Short Break", PINK)
        count_down(short_break_sec)
    else:
        work_display("Work Time", GREEN)
        count_down(work_sec)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global time_
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        time_ = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps%2 == 0:
            checkmark = "✔"*(int(reps/2))
            checkmark_label.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pamadoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
title_label = tkinter.Label(text="Time", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

checkmark_label = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 17, "bold"))
checkmark_label.grid(column=1, row=3)

# Buttons
start_button = tkinter.Button(text="Start", bg=YELLOW, command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", bg=YELLOW, command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()
