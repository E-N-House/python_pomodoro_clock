def count_down(min=0, sec=0):
    if sec == 0 and min == 0:
        print("done cycle")
        canvas.itemconfig(timer_text, text="00:00")
        return
    elif sec == 0:
        min -= 1
        sec = 59
    if sec < 10:
        new_text = f"{min}:0{sec}"
    else:
        new_text = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=new_text)
    # TODO: fix sec to 1000
    window.after(10, count_down, min, sec-1)