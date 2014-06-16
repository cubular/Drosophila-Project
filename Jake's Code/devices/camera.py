import Image
import copy

# This module wraps all the camera functions!
#To control camera grabbing functions use the appropiate method as in cam.GetFrameImage() or use with CamThread and
# FrameBuffer

class Camera:
    import pdvpycam23 as pdv  #import here so it is only accessible through Camera

    def __init__(self,num_cam_buffer=4):
        self.num_cam_buffer = num_cam_buffer
        camid = self.id = Camera.pdv.pdv_open('pdv',0)
        
        self.height = Camera.pdv.pdv_get_height(camid)
        self.width = Camera.pdv.pdv_get_width(camid)

        self.gain = Camera.pdv.pdv_get_gain(camid)
        self.blacklevel = Camera.pdv.pdv_get_blacklevel(camid)
        self.exposure = Camera.pdv.pdv_get_exposure(camid)
        self.aperture = None
        Camera.pdv.pdv_multibuf(camid,self.num_cam_buffer)
        Camera.pdv.pdv_start_images(self.id,0)

    def __getSizeTuple(self):
        return (self.width,self.height)
    def __getSizeBytes(self):
        return self.width*self.height
    size_tuple = property(__getSizeTuple)
    size_bytes = property(__getSizeBytes)
        
    def getFrameData(self):
        "Returns current frame data. "
        if self.height == 0:
            raise IOError("Camera not initialized")
        else:
            nSkipped = None
            return Camera.pdv.py_cam_get_frame(Camera.pdv.pdv_wait_image(self.id),self.size_bytes)

    def getFrameImage(self):
        frame = Image.new("L",self.size_tuple)
        frame.fromstring(self.getFrameData())
        return frame

    def reset(self):
        Camera.pdv.pdv_flush_fifo(self.id)
        
    def close(self):
        Camera.pdv.pdv_close(self.id)

