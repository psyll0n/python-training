from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # Color for short breaks
RED = "#e7305b"  # Color for work periods
GREEN = "#9bdeac"  # Color for long breaks and reset
YELLOW = "#f7f5dd"  # Background color
FONT_NAME = "Courier"  # Font used for text
WORK_MIN = 25  # Work period duration in minutes
SHORT_BREAK_MIN = 5  # Short break duration in minutes
LONG_BREAK_MIN = 20  # Long break duration in minutes
reps = 0  # Keeps track of work/break intervals
timer = None  # Stores the current timer reference for cancellation
timer_running = False  # Flag to check if the timer is already running


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Resets the timer and all related variables to the initial state.
    Cancels any running timer and updates the display.
    """
    global reps, timer, timer_running
    reps = 0
    timer_running = False  # Reset the timer status to not running
    if timer is not None:
        window.after_cancel(timer)  # Cancels the running timer
    app_label.config(text="Timer", fg=GREEN)  # Resets label to 'Timer'
    canvas.itemconfig(timer_text, text="00:00")  # Resets timer display
    checkmark.config(text="")  # Clears the checkmark


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Initiates the Pomodoro timer cycle. Alternates between work and break periods
    based on the `reps` count. Every 8th rep is a long break.
    """
    global reps, timer_running
    if not timer_running:  # Only start the timer if it's not running
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        # If it's the 8th rep, take a long break
        if reps % 8 == 0:
            app_label.config(text="Break", fg=GREEN)
            countdown(long_break_sec)
        # If it's the 2nd/4th/6th rep, take a short break
        elif reps % 2 == 0:
            app_label.config(text="Short Break", fg=PINK)
            countdown(short_break_sec)
        # Otherwise, it's time to work
        else:
            app_label.config(text="Time to Work", fg=RED)
            countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """
    Performs the countdown mechanism. Updates the UI every second to reflect the
    remaining time. When the countdown reaches 0, it restarts the timer for the next session.

    Args:
        count (int): Remaining time in seconds.
    """
    global timer, timer_running

    # Calculate minutes and seconds
    count_mins = math.floor(count / 60)
    count_secs = count % 60
    timer_format = f"{count_mins:02d}:{count_secs:02d}"

    # Update the timer display
    canvas.itemconfig(timer_text, text=timer_format)

    # If there is still time left, continue counting down
    if count > 0:
        timer_running = True  # Mark the timer as running
        timer = window.after(1000, countdown, count - 1)  # Calls countdown every 1 second
    else:
        timer_running = False  # Timer has finished, allow new countdown
        start_timer()  # Start the next session when current one ends

        # Update checkmarks for completed work sessions
        marks = ""
        work_sessions = math.floor(reps / 2)
        marks = "✔" * work_sessions  # Add a checkmark for each completed work session
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Main window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=50, bg=YELLOW)

# Canvas setup for the tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Load tomato image
canvas.create_image(100, 112, image=tomato_img)  # Center the image on the canvas
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

# Label that displays the current state (Timer, Break, Work)
app_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
app_label.grid(column=1, row=0)

# Start button to start the timer
start_button = Button(window, highlightthickness=0, text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset button to reset the timer
reset_button = Button(window, highlightthickness=0, text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Label to display checkmarks for completed work sessions
checkmark = Label(window, fg=GREEN, bg=YELLOW, font=("Arial", 18, "bold"))
checkmark.grid(column=1, row=3)

# Start the Tkinter event loop
window.mainloop()
