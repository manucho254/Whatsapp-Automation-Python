from tkinter import *
import pywhatkit
from tkinter import messagebox
import time
import threading

root = Tk()
root.title("WHATSAPP")

root.geometry('405x350')
root.configure(bg='#2B547E')
root.resizable(width=0, height=0)

label = Label(root, text="Whatsapp Automation", font="bold",
              width=40, fg="white", bg="black", padx=10, pady=13)
label.grid(row=0, columnspan=3, padx=10, pady=10)
label.place(x=10,
            y=10)

#First Entry and label

label = Label(
    root, text="Phone Number: Format [+]", font=10, fg="white", bg="black")
label.grid(row=1, padx=10, pady=10)
label.place(x=10,
            y=90)
number_str = StringVar()
entry1 = (Entry(root, width=30, textvariable=number_str,
                bd=6, font=14, borderwidth=6))
entry1.insert(0, "+")
entry1.grid(row=1, column=1, columnspan=1, padx=10, pady=13)

entry1.place(x=10,
             y=120)

#main function


def whatsup():
   try:
      number = entry1.get()
      message = entry2.get()
      time = int(entry3.get())
      time2 = int(entry4.get())
      pywhatkit.sendwhatmsg(number, message, time, time2)
   except:
      messagebox.showerror("error", "Please fill the details")
      
def whatsupthreaded():
    mythreads = threading.Thread(target=whatsup)
    mythreads.start()

#Second Entry and label


label = Label(root, text="Message", font=20, fg="white", bg="black")
label.grid(row=1, padx=10, pady=10)
label.place(x=10,
            y=160)
message_str = StringVar()
entry2 = (Entry(root, width=41, textvariable=message_str,
                bd=6, font=14, borderwidth=6))
entry2.insert(0, "write your message")
entry2.grid(row=1, column=1, columnspan=1, padx=10, pady=13)
entry2.place(x=10,
             y=200)

#Time label and Function
label = Label(root, text="Set Time:24/hr clock system",
              font=20, fg="white", bg="black")
label.grid(row=1, padx=10, pady=10)
label.place(x=10,
            y=240)


label4 = Label(root, font=20, fg="white", bg="black")
label4.grid(row=1, padx=10, pady=10)
label4.place(x=220,
             y=240)


def localtime():
   t = time.localtime()
   current_time = time.strftime("%H:%M:%S", t)
   label4.config(text="Localtime:"+current_time)
   label4.after(200, localtime)


localtime()

entry3 = (Entry(root, width=20))
entry3.insert(0, "15")
entry3.grid(row=1, column=1, columnspan=1, padx=5, pady=13)
entry3.place(x=15,
             y=280)

entry4 = (Entry(root, width=20))
entry4.insert(0, "20")
entry4.grid(row=1, column=1, columnspan=1, padx=5, pady=13)
entry4.place(x=150,
             y=280)

send = Button(root, font="30", width=40, text="Send",
              fg="green", bg="black", command=whatsupthreaded)
send.grid(row=3, column=1, padx=10, pady=10)
send.place(x=15,
           y=310)

root.mainloop()
