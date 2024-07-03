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
timer_reset = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_reset)
    canvas.itemconfig(timer,text="00:00")
    my_label.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        my_label.config(text="Work",fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        my_label.config(text="Short break",fg=PINK)
    elif reps == 8:
        count_down(long_break_sec)
        my_label.config(text="Long break",fg=RED)
        reps = 0




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_reset
        timer_reset = window.after(1000,count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


my_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)

my_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer = canvas.create_text(100,130, text=f"00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)
reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

check_marks = Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(row=3,column=1)


window.mainloop()