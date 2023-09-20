import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
# WORK_MIN = 2

SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_FONT = ("Arial", 26, "bold")
CHECKMARK = "✔"
# 1000 normally
SPEED = 1000
reps = 0
is_cycling = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_click():
    # TODO: figure out why it resets quick and then continues to countdown rather than pause and switches between 5 and 25 counts
    global reps
    global is_cycling
    is_cycling = False
    # reps resets correctly,
    reps = 0
    window.after_cancel(timer)
    new_time = f"00:00"

    # resets UI of start button and checkmarks
    main_label["text"] = "Timer"
    main_label["fg"] = GREEN
    canvas.itemconfig(timer_text, text=new_time)
    start_button["text"] = "Start"
    start_button["state"] = "active"

    # Resets checkmarks to NONE
    tracker_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_click():
    global is_cycling
    if is_cycling:
        is_cycling = False
    start_button["state"] = "disable"
    # start countdown cycle at beginning
    is_cycling = True
    countdown_cycle()


def countdown_cycle():
    global reps
    global is_cycling
    reps += 1
    # countdown long break
    if reps == 0 or reps > 8:
        # turn off cycles
        is_cycling = False
        return
    elif reps % 8 == 0:
        # Long Break UI
        new_checkmark_added(tracker_label["text"])
        main_label["text"] = "Break"
        main_label["fg"] = RED
        count_down(LONG_BREAK_MIN * 60)

    # countdown break
    elif reps % 2 == 0:
        new_checkmark_added(tracker_label["text"])
        main_label["text"] = "Break"
        main_label["fg"] = PINK
        count_down(SHORT_BREAK_MIN * 60)

    # countdown work cycle
    else:
        main_label["text"] = "Work"
        main_label["fg"] = GREEN

        count_down(WORK_MIN * 60)
    return True


def break_starts():
    # for changing ui design on break
    pass


def new_checkmark_added(checks):
    checks += CHECKMARK
    tracker_label.config(text=checks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    # reset the count to whole minutes rounded down
    minutes = math.floor(count/60)
    # find remainder of seconds
    seconds = count % 60

    # formats seconds in 0Num format as a string
    if seconds < 10:
        seconds = f"0{seconds}"

    if count > 0:
        global timer
        # formats timer display
        new_text = f"{minutes}:{seconds}"
        # shows timer display on screen
        canvas.itemconfig(timer_text, text=new_text)
        # DONE: fix sec to 1000
        # sets time interval to be once a second and feeds in the new count minus 1 second
        timer = window.after(SPEED, count_down, count-1)

    elif count == 0 and not is_cycling:
        reset_click()
    # checks for finished countdown and exits loop
    else:
        canvas.itemconfig(timer_text, text="00:00")
        start_click()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(bg=YELLOW, width=500, height=300, pady=50, padx=100)
window.title("Pomodoro Timer")

main_label = Label(text="Timer", background=YELLOW, font=(FONT_NAME, 50), foreground=GREEN,)
main_label.grid(column=1, row=0)
main_label.config(pady=10)

canvas = Canvas(width=220, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)

timer_text = canvas.create_text(110, 140, text="00:00", font=TIMER_FONT, fill="white", width=-100)
canvas.grid(column=1, row=1)

start_button = Button(text="Start",  highlightthickness=0, width=-5)
start_button.grid(column=0, row=2)
start_button.config(command=start_click)

reset_button = Button(text="Reset",  highlightthickness=0, width=-5)
reset_button.grid(column=2, row=2)
reset_button.config(command=reset_click)

tracker_label = Label(text="", background=YELLOW, fg=GREEN, font=("arial", 15))
tracker_label.grid(column=1, row=3)

window.mainloop()
