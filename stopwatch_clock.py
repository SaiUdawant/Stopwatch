import tkinter as tk
from datetime import datetime
import time

# Initialize window
window = tk.Tk()
window.title("Stopwatch & Clock")
window.geometry("300x250")
window.config(bg="lightgray")

# Variables
start_time = None
elapsed_time = 0
running = False

# Functions
def update_clock():
    now = datetime.now().strftime('%H:%M:%S')
    clock_label.config(text=now)
    window.after(1000, update_clock)

def update_stopwatch():
    if running:
        global elapsed_time
        current_time = time.time()
        elapsed_time = current_time - start_time
        mins, secs = divmod(int(elapsed_time), 60)
        millis = int((elapsed_time - int(elapsed_time)) * 100)
        stopwatch_label.config(text=f"{mins:02}:{secs:02}:{millis:02}")
        window.after(10, update_stopwatch)

def start():
    global start_time, running
    if not running:
        start_time = time.time() - elapsed_time
        running = True
        update_stopwatch()

def stop():
    global running
    running = False

def reset():
    global elapsed_time, running
    running = False
    elapsed_time = 0
    stopwatch_label.config(text="00:00:00")

# Labels
clock_label = tk.Label(window, text="", font=("Helvetica", 20), bg="lightgray")
clock_label.pack(pady=10)

stopwatch_label = tk.Label(window, text="00:00:00", font=("Helvetica", 24), bg="white", width=10)
stopwatch_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(window, bg="lightgray")
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="Start", command=start, width=8, bg="green", fg="white")
start_btn.grid(row=0, column=0, padx=5)

stop_btn = tk.Button(btn_frame, text="Stop", command=stop, width=8, bg="red", fg="white")
stop_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", command=reset, width=8, bg="blue", fg="white")
reset_btn.grid(row=0, column=2, padx=5)

# Start the real-time clock
update_clock()

# Run the app
window.mainloop()
