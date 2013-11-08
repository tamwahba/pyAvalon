from MovingWindow import *


class introPage(MovingWindow):
    """docstring for introPage"""
    def __init__(self):
        super().__init__()
        self.mainFrame = Frame(self)
        self.mainFrame.pack()

        self.background = PhotoImage(
            file='resources\Avalon intro background -- castle1280.gif')

        self.backgroundLabel = Label(self.mainFrame, image=self.background)
        self.backgroundLabel.pack()


def main():
    window = introPage()
    window.geometry('+150+150')
    window.mainloop()

main()
