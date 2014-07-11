mmc.snapImage()
im1 = mmc.getImage()

# Display the image:
from pylab import *
ion() # Activate interactive mode
#import pdb;pdb.set_trace()
figure()
imshow(im1,cmap = cm.gray) 
savefig('test.png')