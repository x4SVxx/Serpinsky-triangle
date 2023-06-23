class Dot():

    def __init__(self, dotcoords, ID, color):

        self.x = float(dotcoords[0])
        self.y = float(dotcoords[1])
        self.ID = str(ID)
        self.color = color
        self.dotwidth = 5

    def drawdot(self, canvas):
        canvas.create_oval(self.x - self.dotwidth, self.y + self.dotwidth,
                           self.x + self.dotwidth, self.y - self.dotwidth, fill=self.color, tag=self.ID)
