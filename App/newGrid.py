import tkinter as tk
from time import sleep


window = tk.Tk()
gridFrame = tk.Frame(master=window)


commonSet1=(0,1,2)
commonSet2=(3,4,5)
entryList = list()
testList = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]


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
for fakeY in range(9):
    tXentrys = list()
    for fakeX in range(9):
        
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


def possible(x,y,n):                    
    
    value = str(n)

    for axisY in range(0,9):                        #proveruvame po y oska
        if entryList[axisY][x].get() == value:
            return False
    
    for axisX in range(0,9):                        #proveruvame po x oska
        if entryList[y][axisX].get() == value:
            return False
    
    tSetX = set()
    tSetY = set()
    axisX = 0
    axisY = 0
    
    if x in commonSet1:                              #naogame u koja kocka 
        tSetX = commonSet1
    elif x in commonSet2:
        tSetX = commonSet2
    else:
        tSetX = (6,7,8)
    
    if y in commonSet1:
        tSetY = commonSet1
    elif y in commonSet2:
        tSetY = commonSet2
    else:
        tSetY = (6,7,8)

    for axisX in tSetX:                               #proveruvame u kocka
        for axisY in tSetY:
            if entryList[axisY][axisX].get() == value:
                return False
    
                                      #podocna na net najdov ovoa:
    # x0 = (x//3)*3                         
    # y0 = (y//3)*3
    # for i in range(0,3):
    #     for j in range(0,3):
    #         if entryList[y0+i][x0+j].get() == value:
    #             return False

   
    return True
    

def Solve():
    n=1
    for x in range(9):
        for y in range(9):
            if entryList[y][x].get() == "":
                for n in range(1,10):
                    if possible(x,y,n):
                        # print(x,y,n)
                        # input('print')
                        entryList[y][x].insert(0,str(n))
                        Solve()
                        entryList[y][x].delete(0, tk.END)
                        #input("more")
                return
    input("more")
    
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

def testRun():
    for xx in range(9):
        for yy in range(9):
            value = testList[xx][yy]
            if value != 0:
                entryList[xx][yy].insert(0,str(value))
TestButton = tk.Button(master=window,text="Test Case",width=36,font=("", 12), command=testRun)


window.bind("<Button-1>",clickEvent)
gridFrame.pack()
SolveButton.pack()
TestButton.pack()

window.mainloop()