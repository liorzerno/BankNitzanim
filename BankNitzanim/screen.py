import tkinter
from tkinter import ttk, filedialog
import PIL
import tkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk
import PIL
from PIL import Image, ImageTk
from datetime import *

from PIL.ImageChops import screen

window = tkinter.Tk()
window.title("Bank Nitzanim")


def header(screen):
    header_frame = tkinter.Frame(screen, bg="limegreen", height=50)
    header_frame.pack(fill="x", side="top")
    header_frame.pack_propagate(False)

def skip_day(screen1):
    date1 = datetime(3500,1,1)
    date1 += timedelta(days=1)
    date_label = tkinter.Label(screen1, text=f"{date1:%d\%B\%Y}", font=("Arial", 16), fg="limegreen")
    date_label.pack(pady=50)


# def image(screen):
#     img = Image.open("alien_teacher.png")
#     screen.create_image(0, 0, image=img)
#     screen.pack()
    #url = https://stackoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter

 # def plus_button(screen):
 #     btn = ttk.Button(window, text="+", command=skip_day(screen), style="Big.TButton", width=18)
 #     btn.place(relx=0.5, rely=0.5, anchor="center")


def open_new_window():

    window.destroy()
    window2 = tkinter.Tk()
    window2.geometry("800x600")
    window2.configure(bg="lavenderblush")
    header(window2)
    #image(window)

    skip_day(window2)
    sum_money = tkinter.Label(window2, text="0", font=("Helvetica", 30, "bold"), fg="black")
    sum_money.pack(pady=(30, 0))


def open_button():
    style = ttk.Style()
    style.configure("Big.TButton", font=("Arial", 18, "bold"))
    btn = ttk.Button(window, text="OPEN BANK \n  ACCOUNT", command=open_new_window, style="Big.TButton", width=18)
    btn.place(relx=0.5, rely=0.5, anchor="center")

def plus_button():
    style = ttk.Style()
    style.configure("Small.TButton", font=("Arial", 18, "bold"))
    btn1 = ttk.Button(window, text="+", command=plus_button, style="Small.TButton")
    btn1.place(relx=0.5, rely=0.5, anchor="center")


window.geometry("800x600")
header(window)
open_button()
plus_button()
#image(window)
window.configure(bg="lavenderblush")

window.mainloop()

