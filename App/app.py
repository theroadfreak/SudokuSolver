import tkinter as tk


window = tk.Tk()

largeFrame= tk.Frame(master=window)

entryDict=dict()

for mx in range(3):
    for my in range(3):
    
        mainFrame = tk.Frame(master=largeFrame,relief=tk.SOLID,borderwidth=1)
        
        for x in range(3):
            for y in range(3):
                frame = tk.Frame(master=mainFrame,relief=tk.SOLID,borderwidth=1)
                frame.grid(row=x,column=y)
                entry = tk.Entry(master=frame,width=4)
                entry.pack()
                #spakuvaj entry u  entryDict 
            
        mainFrame.grid(row=mx,column=my)

largeFrame.pack()
 
def clickEvent(*args):
    #proveri dali site elementi na entryDict se brojki
    print('click')

window.bind("<Button-1>",clickEvent)
window.mainloop()