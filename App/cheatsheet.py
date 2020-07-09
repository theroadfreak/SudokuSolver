import tkinter as tk

#Using Events and Event Handlers

window = tk.Tk()

frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frameB = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
frameGrid=tk.Frame(master=window)
label = tk.Label(text="HI",
                 bg="black",
                 fg="green",
                 height=2,
                 width=5,
                 master=frame)
label.pack()

butt = tk.Button(text="Click me",
                 fg="white",
                 bg="black",
                 width=10,
                 height=5,
                 master=frame)
butt.pack()

NameLabel = tk.Label(text="Name:",
                 bg="black",
                 fg="green",
                 width=5,
                 height=1,
                 master=frameB)
NameLabel.pack()

nameEn = tk.Entry(master=frameB,width=5)
nameEn.pack()


for x in range(3):
    for y in range(3):
        _frame = tk.Frame(master=frameGrid,relief=tk.RAISED,borderwidth=1)
        _frame.grid(row=x,column=y,padx=1,pady=1) 
        _label = tk.Label(master=_frame,text = "x={}\ny={}".format(x,y))
        _label.pack()

for i in range(3):
    frameGrid.rowconfigure(i, weight=2 , minsize=50)
    frameGrid.columnconfigure(i, weight=2 , minsize=50)
    
frameB.pack(fill=tk.BOTH,expand=True)
frame.pack(fill=tk.BOTH,expand=True)
frameGrid.pack(fill=tk.BOTH,expand=True)


window.mainloop()
