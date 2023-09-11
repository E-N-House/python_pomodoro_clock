from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_FONT = ("Arial", 26, "bold")

# ---------------------------- TIMER RESET ------------------------------- #

def reset_click():
    # canvas.create_text(110, 140, text="00:00", font=TIMER_FONT, fill="white")

    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_click():
    # canvas.create_text(110, 140, text="11:00", font=TIMER_FONT, fill="red")
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg=YELLOW, width=300, height=300, pady=50, padx=100)
window.title("Pomodoro Timer")

main_label = Label(text="Timer", background=YELLOW, font=(FONT_NAME,50), foreground=GREEN)
main_label.grid(column=1, row=0)
main_label.config(pady=10)

canvas = Canvas(width=220, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)

canvas.create_text(110, 140, text="00:00", font=TIMER_FONT, fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start",  highlightthickness=0)
start_button.grid(column=0, row=2)
start_button.config(command=start_click)

reset_button = Button(text="Reset",  highlightthickness=0)
reset_button.grid(column=2, row=2)
reset_button.config(command=reset_click)

tracker_label = Label(text="✔", background=YELLOW, fg=GREEN, font=("arial", 15))
tracker_label.grid(column=1, row=3)


window.mainloop()