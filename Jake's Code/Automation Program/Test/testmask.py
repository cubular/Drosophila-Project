import scipy
import Image
max_distance = 200
mask = Image.new('L',(640,480))
m = float(slope)
x0 = 320    # frame is centered around fly centroid, which in the frame space is at (320,240)
y0 = 240
b0 = y0-m*x0  #get y intercept of fly axis in space of frame

d_range = range(1000)
f_table = [int(255.*scipy.exp(-d**2/2./(max_distance/3.)**2)) for d in d_range]

if abs(m) < .1:             # avoids the divide by zero error
    for x in range(640):
        for y in range(480):
            if abs(y-y0) < max_distance:   mask.putpixel((x,y),255)

for x in range(640): #coords of x domain
    for y in range(480):
        b1 = y+(1/m)*x  #get eq for line through each point, perpendicular to axis
        x_int = (b1-b0)/(m+(1/m))  # equate to get coords of intersection
        y_int = (-1/m)*x_int+b1    # plug in for y
        dist = int(((x-x_int)**2+(y-y_int)**2)**0.5)  # calculate distance between intersection and coords
        f = f_table[dist]
        mask.putpixel((x,y),f) 