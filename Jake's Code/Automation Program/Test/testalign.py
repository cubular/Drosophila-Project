
import scipy
import Image
slope = 1
deg = scipy.arctan(slope)*180./scipy.pi+90
fly_image = Image.open(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\fly.bmp')
x,y = fly_image.size
large_size = (3*x,3*y)
paste_corner = (x,y)
large = Image.new("L",large_size,255)
large.paste(fly_image,paste_corner)
#convert slope to angle and rotate to vertical
aligned = large.rotate(deg)
crop_edges = (int(.5*x),int(.5*y),int(2.5*x),int(2.5*y))
cropped = aligned.crop(crop_edges)
thresh = cropped.point(lambda p: 255*(p < 250))
bounded = cropped.crop(thresh.getbbox())

large.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\large.bmp')
cropped.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\cropped.bmp')
aligned.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\aligned.bmp')
thresh.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\thresh.bmp')
bounded.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\bounded.bmp')