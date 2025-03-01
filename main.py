import os
import tkinter as tk
from PIL import Image,ImageTk



root = tk.Tk()
root.title("Shutdown Timer Application")
root.geometry("800x800")


image = Image.open("assets/stopwatch.png")
image = image.resize((800,800))
bgImage = ImageTk.PhotoImage(image)


canvas = tk.Canvas(root,width=800,height=800)
canvas.pack(fill="both",expand=True)
canvas.create_image(400,400,image=bgImage,anchor="center")

bg_color = "#bab6aa"

def timer_start():
    try:    
        hours = hour_entry.get()
        minutes = minute_entry.get()
        
        hours = int(hours) if hours.strip() else 0
        minutes = int(minutes) if minutes.strip() else 0
        
        if hours == 0 and minutes == 0:
            countdown_label.config(text="Lütfen geçerli bir süre girin!", fg="red")
            return

        total_seconds = (hours * 3600) + (minutes * 60)
        Countdown(total_seconds)  
        countdown_label.config(fg="black")  

    except ValueError:
        print("Please enter a valid number !")

def Countdown(remaining_seconds):
    if remaining_seconds > 0:
        hours_left = remaining_seconds // 3600
        minutes_left = (remaining_seconds % 3600) // 60
        seconds_left = remaining_seconds % 60
        countdown_label.config(text=f"      {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}",font=("Pixel Font", 20), fg="green", bg="#eceadd")
        root.after(1000,Countdown,remaining_seconds-1)
    else:
        shutdown()

def shutdown():
    print("bilgisayar kapatiliyor")
    os.system("shutdown /s /t 1") # for windows
    # os.system("shutdown -h now")  for linux and mac


hour_label = tk.Label(root, text="Enter Hour Here", font=("Pixel Font", 15), bg=bg_color, fg="green")
hour_label.place(x=48,y=102)
minute_label = tk.Label(root,text="Enter Minute Here",font=("Pixel Font",15),bg =bg_color,fg="green")
minute_label.place(x=30,y=203)

countdown_label = tk.Label(root, text="Shutdown In --:--", font=("Pixel Font", 20), fg="green", bg="#eceadd")
countdown_label.place(x=295, y=400)  # Konumu ayarlayabilirsin

hour_entry = tk.Entry(root,font=("Pixel Font",16),width=3,justify="center")
hour_entry.place(x=200,y=100)
minute_entry = tk.Entry(root, font=("Pixel Font", 16), width=3, justify="center")
minute_entry.place(x=200, y=200)

start_button = tk.Button(root,text="Start ",font=("Pixel Font",17),bg="#0b1935",fg="orange",command=timer_start)
start_button.place(x=364,y=138)

root.mainloop()
