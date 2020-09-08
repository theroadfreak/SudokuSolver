import tkinter as tk



window = tk.Tk()
gridFrame = tk.Frame(master=window)


commonSet1=(1,2,3)
commonSet2=(4,5,6)
entryList = list()


largeFrameList = list()
for x in range(3): #sozdavam 9 golemi frame i skladiram u 2d lista largeFrameList[[],[],[],[]] zada moze largeFrameList[x][y]
    tSetOfThree=list()
    for y in range(3):
        frame = tk.Frame(master=gridFrame,relief=tk.SOLID,borderwidth=1)
        frame.grid(row=x,column=y)
        tSetOfThree.append(frame)
    largeFrameList.append(tSetOfThree)


largeframeX = int()
largeframeY = int()
gridX = int()
gridY = int()
for fakeY in range(1,10):
    tXentrys = list()
    for fakeX in range(1,10):
        
        if fakeY in commonSet1: #birame koj frame od 9te golemi i koj (x,y) u nivnio grid
            largeframeY = 0
            gridY = fakeY
        elif fakeY in commonSet2:
            largeframeY = 1
            gridY = fakeY-2
        else:
            largeframeY = 2
            gridY = fakeY-6
        
        if fakeX in commonSet1:
            largeframeX = 0
            gridX = fakeX
        elif fakeX in commonSet2:
            largeframeX = 1
            gridX = fakeX-2
        else:
            largeframeX = 2
            gridX = fakeX-6

        entry = tk.Entry(master=largeFrameList[largeframeY][largeframeX],width=4)
        entry.grid(row=gridY,column=gridX)
        
        # label = tk.Label(master=largeFrameList[largeframeY][largeframeX],text="{},{}".format(fakeX,fakeY) ,width=4,height=2)   #debuging
        # label.grid(row=gridY,column=gridX)    #debuging
        
        tXentrys.append(entry)
        # tXentrys.append(label) #debuging
    entryList.append(tXentrys)      #skladiram u 2d zada moze entryList[x][y]


def possible(x,y):
    
    value = entryList[x][y].get()

    for axisY in range(0,9):
        if y != axisY:
            if entryList[x][axisY].get() == value:
                return False
    
    for axisX in range(0,9):
        if x != axisX:
            if entryList[axisX][y].get() == value:
                return False
    
    return True
    

def Solve():
    print(possible(0,0))
SolveButton = tk.Button(master=window,text="Solve",width=36,font=("", 12), command=Solve)

ErrorLabel = None
def clickEvent(*args): #check if ima bukvi ili if >9
    global ErrorLabel
    
    if ErrorLabel:
        ErrorLabel.destroy()
        SolveButton.config(state=tk.NORMAL)    
        
    for row in entryList:
        for value in row:
            indexValue=value.get()
            if indexValue == "":
                pass
            else:
                try:
                    if int(indexValue) > 9:
                        raise Exception()
                except:
                    ErrorLabel = tk.Label(master=window, text="You can only enter numbers! (less than 9)", fg="red")
                    ErrorLabel.pack()            
                    SolveButton.config(state=tk.DISABLED)


window.bind("<Button-1>",clickEvent)
gridFrame.pack()
SolveButton.pack()

window.mainloop()