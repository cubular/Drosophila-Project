import scipy
import ImageChops,ImageStat
import Gnuplot

step = 7500
if d.slide.pos[2] >= 0:  step = -step
d.slide.moveZ(-step/2)
z_start = d.slide.pos[2]
d.frames.fillBuffer()
d.slide.displaceZ(step)
z_frames = d.frames.getBuffer()

#sample every 5th plus its neighbor
sample_indices = [ind*5 for ind in range(len(z_frames)/5)]
z_frames = [z_frames[ind] for ind in sample_indices]
n = len(z_frames)
diffs = []
for i in range(n-2):
    diffs.append(ImageChops.difference(z_frames[i+2],z_frames[i]))
motion = []
for f in diffs:
    motion.append(ImageStat.Stat(f).sum[0])
g = Gnuplot.Gnuplot()
g.plot(motion)

max_frame = scipy.argmax(motion)
max_focus = (max_frame/float(n))*step + z_start
d.slide.moveZ(max_focus)