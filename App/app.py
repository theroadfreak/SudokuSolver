import tkinter as tk

window = tk.Tk()

label = tk.Label(text="hi",
                 bg="black",
                 fg="green",
                 width=10,
                 height=10)
label.pack()

butt = tk.Button(text="Click me",
                 fg="white",
                 bg="black",
                 width=10,
                 height=5)
butt.pack()


NameLabel = tk.Label(text="Name",
                 bg="black",
                 fg="green",
                 width=10,
                 height=10)
NameLabel.pack()


nameEn = tk.Entry()
nameEn.pack()


print(nameEn.get())


window.mainloop()
