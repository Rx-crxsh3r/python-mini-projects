# Import Required Libraries
from tkinter import *
import datetime
import time
from threading import *
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# List to store alarms
alarms = []

# Rainbow colors for wake up message
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
color_index = 0

# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    # Infinite Loop
    while True:
        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        for alarm_time in alarms:
            # Check whether set alarm is equal to current time or not
            if current_time == alarm_time:
                print("Time to Wake up")
                alarms.remove(alarm_time)
                update_alarm_list()
                show_wakeup_window()
                # Playing sound
                pygame.mixer.music.load("sounds.mp3")
                pygame.mixer.music.play()
                break

def add_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarms.append(alarm_time)
    update_alarm_list()

def update_alarm_list():
    alarm_listbox.delete(0, END)
    for alarm_time in alarms:
        alarm_listbox.insert(END, alarm_time)

def update_time_label():
	current_time = datetime.datetime.now().strftime("%H:%M:%S")
	time_label.config(text="Current time is: " + current_time) 
	time_label.after(1000, update_time_label)
    
def delete_alarm(event):
	selected_time = alarm_listbox.get(alarm_listbox.curselection())
	alarms.remove(selected_time)
	update_alarm_list()

def change_color(label):
     global color_index
     label.config(fg=colors[color_index])
     color_index = (color_index + 1) % len(colors)
     label.after(999, change_color, label)

def show_wakeup_window():
     wakeup_window = Toplevel(root)
     wakeup_window.attributes('-fullscreen', True)
     wakeup_window.title("Alarm")
     wakeup_label = Label(wakeup_window, text="TIME TO WAKE UP!!!", font=("Helvetica", 20, "bold"))
     wakeup_label.pack(expand=True)
     change_color(wakeup_label)
     close_button = Button(wakeup_window, text="Close", font=("Helvetica", 15), command=lambda: stop_alarm(wakeup_window))
     close_button.pack(pady=20)
     
def stop_alarm(wakeup_window):
     pygame.mixer.music.stop()
     wakeup_window.destroy()
     
# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = (
    '00', '01', '02', '03', '04', '05', '06', '07',
    '08', '09', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23'
)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = (
    '00', '01', '02', '03', '04', '05', '06', '07',
    '08', '09', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23',
    '24', '25', '26', '27', '28', '29', '30', '31',
    '32', '33', '34', '35', '36', '37', '38', '39',
    '40', '41', '42', '43', '44', '45', '46', '47',
    '48', '49', '50', '51', '52', '53', '54', '55',
    '56', '57', '58', '59'
)
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = (
    '00', '01', '02', '03', '04', '05', '06', '07',
    '08', '09', '10', '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20', '21', '22', '23',
    '24', '25', '26', '27', '28', '29', '30', '31',
    '32', '33', '34', '35', '36', '37', '38', '39',
    '40', '41', '42', '43', '44', '45', '46', '47',
    '48', '49', '50', '51', '52', '53', '54', '55',
    '56', '57', '58', '59'
)
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=add_alarm).pack(pady=10)

time_label = Label(root, text="", font=("Helvetica 15 bold"))
time_label.pack()
# Listbox to display alarms
alarm_listbox = Listbox(root, font=("Helvetica 12"))
alarm_listbox.pack(pady=20)

# bind listbox with a double click event allowing user to delete alarm by double clicking on it
alarm_listbox.bind('<Double-1>', delete_alarm)

# Start the alarm checking thread
Threading()

#Start updating the time label 
update_time_label()

# Execute Tkinter
root.mainloop()
