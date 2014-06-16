# Check here for class functions: http://valelab.ucsf.edu/~aedelstein/mm_doc/html/class_c_m_m_core.html#0c3b3d0a85c26d9a9d65abfed597d8c4


#Initialize Camera
print "Initializing Camera..."
import MMCorePy
from pylab import *
mmc = MMCorePy.CMMCore()

mmc.loadDevice("cam","HamamatsuHam","HamamatsuHam_DCAM")
mmc.initializeDevice("cam")
mmc.setCameraDevice("cam")
print "Camera initialization successful!"
