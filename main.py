import math
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
REPS = 0
CHECK_TEXT = ""
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS
    REPS = 0
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_check.config(text="")
    lbl_timer.config(text="TIMER")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 2 == 0:
        lbl_timer.config(text='SHORT BREAK', fg=PINK)
        count_down(short_break)
    elif REPS == 8:
        lbl_timer.config(text='LONG BREAK', fg=RED)
        count_down(long_break)
    else:
        lbl_timer.config(text='WORK', fg=GREEN)
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global  CHECK_TEXT
    global REPS
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if REPS % 2 == 0:
            CHECK_TEXT += "✔"
            lbl_check.config(text=CHECK_TEXT)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

lbl_timer = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 30, 'bold'), bg=YELLOW)
lbl_timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill='white', font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)

btn_start = Button(text="Start", bg='white', highlightthickness=0, command=start_timer)
btn_start.grid(column=0, row=2)
lbl_check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
lbl_check.grid(column=1, row=3)
btn_reset = Button(text="Resert", bg='white', highlightthickness=0, command=reset)
btn_reset.grid(column=2, row=2)

window.mainloop()

