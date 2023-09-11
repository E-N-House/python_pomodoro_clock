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
    new_time = f"{WORK_MIN}:00"
    count_down(min=0, sec=0)
    canvas.itemconfig(timer_text, text=new_time)
    tracker_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_click():
    count_down(WORK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(min=0, sec=0):
    if sec == 0 and min == 0:
        print("done cycle")
        canvas.itemconfig(timer_text, text="00:00")
        return
    if sec == 0:
        min -= 1
        sec = 59
    if sec < 10:
        new_text = f"{min}:0{sec}"
    else:
        new_text = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=new_text)
    # TODO: fix sec to 1000
    window.after(10, count_down, min, sec-1)


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

timer_text = canvas.create_text(110, 140, text="00:00", font=TIMER_FONT, fill="white")
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

