import Tkinter
from PIL import Image, ImageTk
from sys import argv
import os

execfile("stage only moveTo.py")

stage = StageDriver()

window = Tkinter.Tk(className="FlyMap interactive GUI")

os.chdir("C:\Users\BodmerLab\Desktop")
image = Image.open(argv[1] if len(argv) >=2 else "FlyMapTest.png")
canvas = Tkinter.Canvas(window, width=image.size[0], height=image.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(image.size[0]//2, image.size[1]//2, image=image_tk)

def callback(event):
    print "Fly Located at: ", event.x, event.y
    xPosition = -event.x * 1400 + 40000
    yPosition = -event.y * 1400 + 14000
    print "Translated to: " + str(xPosition) + ", " + str(yPosition)
    stage.moveTo(xPosition, yPosition)

canvas.bind("<Button-1>", callback)
Tkinter.mainloop()
