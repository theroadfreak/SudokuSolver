import tkinter as tk


window = tk.Tk()

largeFrame= tk.Frame(master=window)

entryDict=dict()
index = 1

for mx in range(3):
    for my in range(3):
    
        mainFrame = tk.Frame(master=largeFrame,relief=tk.SOLID,borderwidth=1)
        
        for x in range(3):
            for y in range(3):
                frame = tk.Frame(master=mainFrame,relief=tk.SOLID,borderwidth=1)
                frame.grid(row=x,column=y)
                entry = tk.Entry(master=frame,width=4)
                entry.pack()
                
                # Label = tk.Label(master=frame, text="{}".format(index) ,width=4,height=4)
                # Label.pack()            
        
                index += 1
                entryDict[index] = entry
                
        mainFrame.grid(row=mx,column=my)

largeFrame.pack()
 
def Solve():
    pass
    

SolveButton = tk.Button(master=window,text="Solve",width=36,font=("", 12), command=Solve)
SolveButton.pack()


ErrorLabel = None
def clickEvent(*args): #check if ima bukvi
    global ErrorLabel
    
    if ErrorLabel:
        ErrorLabel.destroy()
        SolveButton.config(state=tk.NORMAL)    
        
    for _key,value in entryDict.items():
        indexValue=value.get()
        if indexValue == "":
            pass
        else:
            try:
                int(indexValue)
            except:
                ErrorLabel = tk.Label(master=window, text="You can only enter numbers", fg="red")
                ErrorLabel.pack()            
                SolveButton.config(state=tk.DISABLED)


window.bind("<Button-1>",clickEvent)
window.mainloop()