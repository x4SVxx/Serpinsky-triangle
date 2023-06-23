from tkinter import *
import random
import time
from dot import Dot

class TRI:

    def __init__(self):

        def mousepress(event):
            pointxy = (event.x, event.y)
            presspos = list(pointxy)
            self.dotcount += 1

            if self.dotcount <= 3:
                newdot = Dot(presspos, self.dotcount, 'red')
                self.dotmas.append(newdot)
                newdot.drawdot(self.canvas)
            elif self.dotcount == 4:
                newdot = Dot(presspos, 'randomdot', 'yellow')
                self.dotmas.append(newdot)
                newdot.drawdot(self.canvas)
                self.canvas.update()
                startscript(newdot)

        def startscript(newdot):
            dotstepX = newdot.x
            dotstepY = newdot.y
            while True:
                randomdot = random.randint(1, 3)
                for dot in self.dotmas:
                    if dot.ID == str(randomdot):
                        dotstepX = (dotstepX + dot.x) / 2
                        dotstepY = (dotstepY + dot.y) / 2
                        self.canvas.create_oval(dotstepX - 2, dotstepY + 2, dotstepX + 2, dotstepY - 2, fill='blue')
                        self.canvas.update()
                time.sleep(0.01)


        self.tk = Tk()
        self.WIDTHSCREEN = self.tk.winfo_screenwidth()
        self.HEIGHTSCREEN = self.tk.winfo_screenheight()
        self.tk.overrideredirect(True)
        self.web_message_buffer = []
        self.tk.minsize(width=int(self.WIDTHSCREEN / 3 * 2), height=int(self.HEIGHTSCREEN / 5 * 4))
        self.tk.maxsize(width=int(self.WIDTHSCREEN / 3 * 2), height=int(self.HEIGHTSCREEN / 5 * 4))
        self.tk.wm_geometry("+%d+%d" % (int(self.WIDTHSCREEN / 2 - self.WIDTHSCREEN / 3 * 2 / 2),
                                        int(self.HEIGHTSCREEN / 2 - self.HEIGHTSCREEN / 5 * 4 / 2)))
        self.tk["bg"] = "light grey"

        self.canvas = Canvas(self.tk, bg='white')
        self.canvas.pack()
        self.canvas.place(x=0, y=0, width=int(self.WIDTHSCREEN / 3 * 2), height=int(self.HEIGHTSCREEN / 5 * 4))

        self.canvas.bind('<ButtonPress>', mousepress)   # Отслеживание нажатия мыши

        self.dotcount = 0
        self.dotmas = []


window = TRI()
window.tk.mainloop()