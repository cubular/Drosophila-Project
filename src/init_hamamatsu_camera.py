import MMCorePy
from pylab import *
mmc = MMCorePy.CMMCore()
mmc.loadDevice("cam","HamamatsuHam","HamamatsuHam_DCAM")
mmc.initializeDevice("cam")

# Snap and retrieve an image:
#mmc.setCameraDevice("cam")
#mmc.snapImage()
#im1 = mmc.getImage()
#savefig("TESTER.png")
