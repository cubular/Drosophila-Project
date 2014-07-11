from PIL import Image
import os
import time

numberOfPieces = 14
numberOfRows = 14
widthOfPieces = 621
heightOfPieces = 468
area = (numberOfPieces * widthOfPieces) * (numberOfRows * heightOfPieces)
actualArea = 30000 * 30000 * (numberOfPieces * numberOfRows)
scaleFactor = actualArea/area

def makeRow(rowNumber):
    print "Attaching row " + str(rowNumber) + "..."
    blank_image = Image.new("RGB", (numberOfPieces*widthOfPieces, heightOfPieces))
    for i in range(1, numberOfPieces+1):
        img = Image.open("piece%d.png" % (((rowNumber-1)*numberOfPieces) + i))
        blank_image.paste(img, ((i-1)*widthOfPieces, 0))
    blank_image.save("row%d.png" % rowNumber)

def makeFlyMap():
    print "Stitching together FlyMap:"
    widthOfMap = widthOfPieces * numberOfPieces
    heightOfMap = heightOfPieces * numberOfRows
    fly_map = Image.new("RGB", (widthOfMap, heightOfMap))
    for i in range(1, numberOfRows + 1):
        makeRow(i)
    for i in range(1, numberOfRows+1):
        row = Image.open("row%d.png" % i)
        fly_map.paste(row, (0, (i-1)*heightOfPieces))
    #fly_map = fly_map.resize((300,300))
    fly_map.save("FlyMap.png")
    print "Fly Map successfully created. \nFlyMap.png in " + os.getcwd()

# First, we have to crop/resize all images
# (left, upper, right, lower) pixel coordinates

left = 45
upper = 17
right = 666
lower = 485
box = (left, upper, right, lower)
def resizeImages():
    print "Resizing images..."
    for i in range(1, (numberOfPieces*numberOfRows)+1):
        img = Image.open("piece%d.png" % i)
        time.sleep(1)
        img1 = img.crop(box)
        img1.save("piece%d.png" % i)

# This module takes the raw input photos and stitches them together to create a FlyMap
# Start by changing directories to where your photos are
os.chdir('C:\Program Files\Micro-Manager-1.4\Pieces')
# Make sure the pieces are saved as "piece1.jpg", "piece2.jpg", "piece3.jpg", etc.

# Resizing all images.
resizeImages()

# Next, make the Fly Map
makeFlyMap()
