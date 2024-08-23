import tkinter
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Define colors used in the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Define duration for work and breaks (in minutes)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Initialize variables
reps = 0  # Counter for the number of completed sessions
time_ = None  # Reference to the timer


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    """Reset the timer and UI to the initial state."""
    global reps, time_

    # Check if the timer is already at "00:00"
    current_time = canvas.itemcget(time_text, 'text')
    if current_time == "00:00":
        return

    window.after_cancel(time_)  # Cancel the ongoing timer
    canvas.itemconfig(time_text, text="00:00")  # Reset the timer display
    title_label.config(text="Timer")  # Reset the title label
    checkmark_label.config(text="")  # Clear the checkmark label
    reps = 0  # Reset the session counter


# ---------------------------- TIMER MECHANISM ------------------------------- #

def work_display(text, color):
    """Update the title label for work sessions."""
    title_label.config(text=text, fg=color)


def short_break_display(text, color):
    """Update the title label for short breaks."""
    title_label.config(text=text, fg=color)


def long_break_display(text, color):
    """Update the title label for long breaks."""
    title_label.config(text=text, fg=color)


def start_timer():
    """Start the timer and determine the session type."""
    global reps
    reps += 1  # Increment the session counter

    # Convert minutes to seconds for countdown
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine the type of session and start the countdown
    if reps % 8 == 0:
        long_break_display("Long Break", RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        short_break_display("Short Break", PINK)
        count_down(short_break_sec)
    else:
        work_display("Work Time", GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    """Perform the countdown and update the timer display."""
    global time_

    count_min = math.floor(count / 60)  # Convert seconds to minutes
    count_sec = count % 60  # Remaining seconds
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Format seconds with leading zero if needed

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")  # Update the timer display
    if count > 0:
        time_ = window.after(1000, count_down, count - 1)  # Call countdown every second
    else:
        start_timer()  # Start the next session
        if reps % 2 == 0:
            checkmark = "✔" * (int(reps / 2))  # Update checkmarks based on completed work sessions
            checkmark_label.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = tkinter.Tk()
window.title("Pomodoro Timer")  # Set the window title
window.config(padx=100, pady=100, bg=YELLOW)  # Set padding and background color

# Create a canvas for displaying the tomato image and timer
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="images/tomato.png")  # Load the tomato image
canvas.create_image(100, 112, image=tomato_img)  # Add the image to the canvas
time_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)  # Position the canvas in the grid

# Labels
title_label = tkinter.Label(text="Time", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)  # Label for the timer title

checkmark_label = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 17, "bold"))
checkmark_label.grid(column=1, row=3)  # Label for displaying completed sessions

# Buttons
start_button = tkinter.Button(text="Start", bg=YELLOW, command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)  # Button to start the timer

reset_button = tkinter.Button(text="Reset", bg=YELLOW, command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)  # Button to reset the timer

# Run the application
window.mainloop()
