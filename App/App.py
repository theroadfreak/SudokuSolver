import tkinter as tk
from time import sleep


window = tk.Tk()
gridFrame = tk.Frame(master=window)


commonSet1 = (0, 1, 2)
commonSet2 = (3, 4, 5)
entryList = list()

tempList = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]


testList = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

largeFrameList = list()
# sozdavam 9 golemi frame i skladiram u 2d lista largeFrameList[[],[],[],[]] zada moze largeFrameList[x][y]
for x in range(3):
    tSetOfThree = list()
    for y in range(3):
        frame = tk.Frame(master=gridFrame, relief=tk.SOLID, borderwidth=1)
        frame.grid(row=x, column=y)
        tSetOfThree.append(frame)
    largeFrameList.append(tSetOfThree)


largeframeX = int()
largeframeY = int()
gridX = int()
gridY = int()
for fakeY in range(9):
    tXentrys = list()
    for fakeX in range(9):

        # birame koj frame od 9te golemi i koj (x,y) u nivnio grid
        if fakeY in commonSet1:
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

        entry = tk.Entry(
            master=largeFrameList[largeframeY][largeframeX], width=4)
        entry.grid(row=gridY, column=gridX)

        tXentrys.append(entry)
    entryList.append(tXentrys)  # skladiram u 2d zada moze entryList[x][y]


def possible(x, y, n):

    value = str(n)

    for axisY in range(0, 9):  # proveruvame po y oska
        if tempList[axisY][x] == value:
            return False

    for axisX in range(0, 9):  # proveruvame po x oska
        if tempList[y][axisX] == value:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if tempList[y0+i][x0+j] == value:
                return False
    return True


def Solve():
    for x in range(9):
        for y in range(9):
            if tempList[y][x] == '0':
                for n in range(1, 10):
                    if possible(x, y, n):
                        tempList[y][x] = str(n)
                        Solve()
                        tempList[y][x] = str(0)
                return
    copytemplist()
    window.update_idletasks()


def copyentrylist():
    if checkForErrors():
        for x in range(9):
            for y in range(9):
                if entryList[y][x].get():
                    tempList[y][x] = entryList[y][x].get()
                else:
                    tempList[y][x] = str(0)
        Solve()


def copytemplist():
    Empty()
    for x in range(9):
        for y in range(9):
            if tempList[y][x] != '0':
                entryList[y][x].insert(0, tempList[y][x])


def Empty():
    for x in range(9):
        for y in range(9):
            entryList[y][x].delete(0, tk.END)


def testRun():
    Empty()
    for x in range(9):
        for y in range(9):
            value = testList[x][y]
            if value != 0:
                entryList[x][y].insert(0, str(value))


ErrorLabel = None


def clickEvent(*args):  # check if ima bukvi ili if >9
    global ErrorLabel

    if ErrorLabel:
        ErrorLabel.destroy()
        SolveButton.config(state=tk.NORMAL)

    for row in entryList:
        for value in row:
            indexValue = value.get()
            if indexValue == "":
                pass
            else:
                try:
                    if int(indexValue) > 9:
                        raise Exception()
                except:
                    if ErrorLabel:
                        pass
                    else:
                        ErrorLabel = tk.Label(
                            master=window, text="You can only enter numbers! (less than 9)", fg="red")
                        ErrorLabel.pack()
                        SolveButton.config(state=tk.DISABLED)


def checkForErrors():
    global ErrorLabel

    if ErrorLabel:
        ErrorLabel.destroy()
        SolveButton.config(state=tk.NORMAL)

    n = 0
    for row in entryList:
        for value in row:
            if value:
                n += 1

    if n > 16:
        if ErrorLabel:
            return False
        else:
            ErrorLabel = tk.Label(
                master=window, text="You entered too few numbers. (less than 17)", fg="red")
            ErrorLabel.pack()
            SolveButton.config(state=tk.DISABLED)
            return False
    return True


SolveButton = tk.Button(master=window, text="Solve",
                        width=36, font=("", 12), command=copyentrylist)
TestButton = tk.Button(master=window, text="Test Case",
                       width=36, font=("", 12), command=testRun)
ExitButton = tk.Button(master=window, text="Empty out Grid",
                       width=36, font=("", 12), command=Empty)


window.bind("<Button-1>", clickEvent)
gridFrame.pack()
SolveButton.pack()
TestButton.pack()
ExitButton.pack()

window.mainloop()
