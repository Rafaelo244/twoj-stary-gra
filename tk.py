import pyperclip
import tkinter
import tkinter as tk
root = tk.Tk()
root.geometry("1500x1000")
root.title("tfuj stary gra")

textbox = tk.Text(root, height = 10)
textbox.place(anchor=tk.CENTER, relx=0.5, rely=0.3)


def funkcjaprzycisku():
    print(textbox.get("1.0",'end-1c'))

def funkcjaprzycisku2():
    textbox.delete(1.0, tk.END)


def funkcjaprzycisku3():
    pyperclip.copy(textbox.get(1.0, tk.END).rstrip("\n"))

label = tk.Label(root, text = "siema eniu", font= ('Arial', 20))
label.pack(padx=0, pady=0)

b = tkinter.Button(root, text="SEND", font='Arial',  command=funkcjaprzycisku)
b.place(relx = 0.5, rely = 0.4, anchor=tk.N)

b2 = tkinter.Button(root, text="DELETE", font='Arial',  command=funkcjaprzycisku2)
b2.place(relx = 0.4, rely =0.4, anchor=tk.N)

b3 = tkinter.Button(root, text="COPY", font='Arial',  command=funkcjaprzycisku3)
b3.place(relx = 0.6, rely = 0.4, anchor=tk.N)






root.mainloop()

