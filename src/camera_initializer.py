# Check here for class functions: http://valelab.ucsf.edu/~aedelstein/mm_doc/html/class_c_m_m_core.html#0c3b3d0a85c26d9a9d65abfed597d8c4

#Initialize Camera
import MMCorePy
from pylab import *
import matplotlib.pyplot as plt
mmc = MMCorePy.CMMCore()

class CameraDriver:

    # Initiate camera
    def __init__(self):
        print "Initializing Camera..."
        mmc.loadDevice("cam","HamamatsuHam","HamamatsuHam_DCAM")
        mmc.initializeDevice("cam")
        mmc.setCameraDevice("cam")
        print "Camera initialization successful!"
        
    def snapImage(self):
    	mmc.snapImage()
    	print "Image acquired"
		
    def saveImage(self, string):
        im1 = mmc.getImage()
        fig = plt.imshow(im1, cmap = cm.gray)
        plt.axis('off')
        savefig(string)

    def reset(self):
        mmc.reset()
