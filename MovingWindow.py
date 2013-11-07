from tkinter import *


class MovingWindow(Tk):
    """docstring for movingWindow"""
    def __init__(self):
        super().__init__()
        self.overrideredirect(1)
        # restrict winow dimetions
        self.minsize(height=730, width=1280)
        self.maxsize(height=730, width=1280)
        self.resizable(0, 0)

        self.taskWindow = Frame(self)
        self.taskWindow.pack(fill=X)

        self.closeImg = PhotoImage(file="Close Lable.gif")
        self.closeLable = Label(self.taskWindow, image=self.closeImg)
        self.closeLable.pack()
        self.closeLable.bind("<1>", self.closeWindow)

        # allow window to move by dragging 'taskWindow'
        self.taskWindow.bind("<ButtonPress-1>", self.StartMove)
        self.taskWindow.bind("<ButtonRelease-1>", self.StopMove)
        self.taskWindow.bind("<B1-Motion>", self.OnMotion)

    def closeWindow(self, event=None):
        self.destroy()

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry("+%s+%s" % (x, y))


# ----- test ----- #
# test = MovingWindow()
# test.geometry('+150+150')
# test.mainloop()
# --- end test --- #
