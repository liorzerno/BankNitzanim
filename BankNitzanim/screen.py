import tkinter
from tkinter import ttk
import PIL
from PIL import Image

window = tkinter.Tk()

def header(screen):
    header_frame = tkinter.Frame(screen, bg="limegreen", height=50)
    header_frame.pack(fill="x", side="top")
    header_frame.pack_propagate(False)


def image(screen):
    img = Image.open("alien_teacher.png")
    screen.create_image(0, 0, image=img)
    screen.pack()

window.geometry("800x600")
header(window)
image(window)
window.configure(bg="lavenderblush")


def open_new_window():
    window.destroy()
    window2 = tkinter.Tk()
    window2.geometry("800x600")
    window2.configure(bg="midnightblue")
    header(window2)
    image(window2)
    sum_money = tkinter.Label(window2, text="0", font=("Helvetica", 30, "bold"), fg="white", bg="midnightblue")
    sum_money.pack(pady=(50, 0))

    window2.mainloop()



style = ttk.Style()
style.configure("Big.TButton", font=("Arial", 18, "bold"))
btn = ttk.Button(window, text="OPEN BANK \n  ACCOUNT", command=open_new_window, style="Big.TButton", width=18)
btn.place(relx=0.5, rely=0.5, anchor="center")



window.mainloop()

