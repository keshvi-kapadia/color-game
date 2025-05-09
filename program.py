import tkinter as tk
import random

root = tk.Tk()

colors = ["Green", "Yellow", "Red", "Blue", "Pink", "Orange", "Black", "Brown"]

root.title("Color Game")

# Window Size and Centering
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#FFF8DC")  # Light cream background

# ---------------- UI Elements ---------------- #
time_left = 30
score = 0
color_loop_id = None
timer_loop_id = None

# Title Label
title = tk.Label(
    root, text="🎨 COLOR GAME 🎨",
    font=("Verdana", 22, "bold"),
    fg="white", bg="#FF69B4",  # Hot pink
    pady=10, padx=20
)
title.place(x=90, y=20)

# Instruction Label
instruction = tk.Label(
    root,
    text="Type the COLOR of the word shown below (not the word itself)",
    font=("Helvetica", 12, "bold"),
    fg="#2F4F4F", bg="#FFF8DC",  # Dark slate gray on cream
    wraplength=400,
    justify="center"
)
instruction.place(x=70, y=80)

# Entry Field
entry = tk.Entry(root, font=("Arial", 14), width=20)
entry.place(x=150, y=150)

# Output Label
color_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#FFF8DC")
color_label.place(x=220, y=190)

def countdown():
    global time_left
    global color_loop_id
    global timer_loop_id

    timer_label.config(text=f'Time Left : {time_left}')
    if time_left > 0:
        time_left -= 1
        timer_loop_id = root.after(1000, countdown)  # Call countdown every 1000ms
    else:
        timer_label.config(text="Game Over!!")
        if color_loop_id is not None:
            root.after_cancel(color_loop_id)
            color_loop_id = None

def change_color():
    global color_loop_id
    color_label.config(text=random.choice(colors), fg=random.choice(colors))
    color_loop_id = root.after(2000, change_color)  # Call change_color every 2000ms

# Function to start game
def start_game():
    global time_left
    global score
    global timer_loop_id
    time_left = 30
    score = 0  # Reset score when the game starts
    score_label.config(text=f'Score : {score}')
    change_color()
    
    # If timer_loop_id exists, cancel the previous timer
    if timer_loop_id is not None:
        root.after_cancel(timer_loop_id)
        
    timer_loop_id = root.after(1000, countdown)  # Start the countdown

def checkScore():
    global score
    if color_label.cget("fg").lower() == entry.get().lower():
        score += 1
        score_label.config(text=f'Score : {score}')
    entry.delete(0, tk.END)

# Start Button
button = tk.Button(
    root, text="Start New Game",
    command=start_game,
    font=("Helvetica", 12, "bold"),
    bg="#32CD32", fg="white",  # Lime green
    padx=15, pady=5
)
button.place(x=250, y=230)

subm_button = tk.Button(
    root, text="Submit",
    command=checkScore,
    font=("Helvetica", 12, "bold"),
    bg="#32CD32", fg="white",  # Lime green
    padx=15, pady=5
)
subm_button.place(x=150, y=230)

score_label = tk.Label(root, text=f'Score : {score}', font=("Helvetica", 12, "bold"))
score_label.place(x=220, y=300)

timer_label = tk.Label(root, text=f'Time Left : {time_left}', fg='red', bg='#FFF8DC')
timer_label.place(x=350, y=105)

# Main loop
root.mainloop()