# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

## CAM module interfaces uses pdvpycam to access methods of the C++ frame grabber
## pdvpycam22 is for Python 2.2 (old).  Use pdvpycam for Python 2.3 and later


import _pdvpycam
def _swig_setattr(self,class_type,name,value):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    self.__dict__[name] = value

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


py_cam_get_frame = _pdvpycam.py_cam_get_frame

class Edtinfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Edtinfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Edtinfo, name)
    __swig_setmethods__["startdma"] = _pdvpycam.Edtinfo_startdma_set
    __swig_getmethods__["startdma"] = _pdvpycam.Edtinfo_startdma_get
    if _newclass:startdma = property(_pdvpycam.Edtinfo_startdma_get,_pdvpycam.Edtinfo_startdma_set)
    __swig_setmethods__["enddma"] = _pdvpycam.Edtinfo_enddma_set
    __swig_getmethods__["enddma"] = _pdvpycam.Edtinfo_enddma_get
    if _newclass:enddma = property(_pdvpycam.Edtinfo_enddma_get,_pdvpycam.Edtinfo_enddma_set)
    __swig_setmethods__["flushdma"] = _pdvpycam.Edtinfo_flushdma_set
    __swig_getmethods__["flushdma"] = _pdvpycam.Edtinfo_flushdma_get
    if _newclass:flushdma = property(_pdvpycam.Edtinfo_flushdma_get,_pdvpycam.Edtinfo_flushdma_set)
    __swig_setmethods__["timeout"] = _pdvpycam.Edtinfo_timeout_set
    __swig_getmethods__["timeout"] = _pdvpycam.Edtinfo_timeout_get
    if _newclass:timeout = property(_pdvpycam.Edtinfo_timeout_get,_pdvpycam.Edtinfo_timeout_set)
    def __init__(self,*args):
        _swig_setattr(self, Edtinfo, 'this', apply(_pdvpycam.new_Edtinfo,args))
        _swig_setattr(self, Edtinfo, 'thisown', 1)
    def __del__(self, destroy= _pdvpycam.delete_Edtinfo):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __repr__(self):
        return "<C Edtinfo instance at %s>" % (self.this,)

class EdtinfoPtr(Edtinfo):
    def __init__(self,this):
        _swig_setattr(self, Edtinfo, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, Edtinfo, 'thisown', 0)
        _swig_setattr(self, Edtinfo,self.__class__,Edtinfo)
_pdvpycam.Edtinfo_swigregister(EdtinfoPtr)

pdv_open = _pdvpycam.pdv_open

pdv_close = _pdvpycam.pdv_close

pdv_read = _pdvpycam.pdv_read

pdv_image = _pdvpycam.pdv_image

pdv_start_image = _pdvpycam.pdv_start_image

pdv_start_images = _pdvpycam.pdv_start_images

pdv_perror = _pdvpycam.pdv_perror

pdv_setdebug = _pdvpycam.pdv_setdebug

pdv_start_hardware_continuous = _pdvpycam.pdv_start_hardware_continuous

pdv_stop_hardware_continuous = _pdvpycam.pdv_stop_hardware_continuous

pdv_flush_fifo = _pdvpycam.pdv_flush_fifo

pdv_wait_image = _pdvpycam.pdv_wait_image

pdv_last_image_timed = _pdvpycam.pdv_last_image_timed

pdv_wait_image_timed = _pdvpycam.pdv_wait_image_timed

pdv_wait_images_timed = _pdvpycam.pdv_wait_images_timed

pdv_wait_images = _pdvpycam.pdv_wait_images

pdv_get_cameratype = _pdvpycam.pdv_get_cameratype

pdv_get_camera_class = _pdvpycam.pdv_get_camera_class

pdv_get_camera_model = _pdvpycam.pdv_get_camera_model

pdv_camera_type = _pdvpycam.pdv_camera_type

pdv_get_width = _pdvpycam.pdv_get_width

pdv_set_width = _pdvpycam.pdv_set_width

pdv_get_height = _pdvpycam.pdv_get_height

pdv_set_height = _pdvpycam.pdv_set_height

pdv_get_depth = _pdvpycam.pdv_get_depth

pdv_get_extdepth = _pdvpycam.pdv_get_extdepth

pdv_set_depth = _pdvpycam.pdv_set_depth

pdv_set_extdepth = _pdvpycam.pdv_set_extdepth

pdv_get_imagesize = _pdvpycam.pdv_get_imagesize

pdv_get_allocated_size = _pdvpycam.pdv_get_allocated_size

pdv_set_exposure = _pdvpycam.pdv_set_exposure

pdv_set_gain = _pdvpycam.pdv_set_gain

pdv_set_blacklevel = _pdvpycam.pdv_set_blacklevel

pdv_set_binning = _pdvpycam.pdv_set_binning

pdv_set_mode = _pdvpycam.pdv_set_mode

pdv_get_exposure = _pdvpycam.pdv_get_exposure

pdv_get_gain = _pdvpycam.pdv_get_gain

pdv_get_blacklevel = _pdvpycam.pdv_get_blacklevel

pdv_set_aperture = _pdvpycam.pdv_set_aperture

pdv_set_timeout = _pdvpycam.pdv_set_timeout

pdv_get_timeout = _pdvpycam.pdv_get_timeout

pdv_update_values_from_camera = _pdvpycam.pdv_update_values_from_camera

pdv_overrun = _pdvpycam.pdv_overrun

pdv_timeouts = _pdvpycam.pdv_timeouts

pdv_timeout_cleanup = _pdvpycam.pdv_timeout_cleanup

pdv_in_continuous = _pdvpycam.pdv_in_continuous

pdv_debug_level = _pdvpycam.pdv_debug_level

pdv_buffer_addresses = _pdvpycam.pdv_buffer_addresses

pdv_alloc = _pdvpycam.pdv_alloc

pdv_free = _pdvpycam.pdv_free

pdv_multibuf = _pdvpycam.pdv_multibuf

pdv_set_baud = _pdvpycam.pdv_set_baud

pdv_get_baud = _pdvpycam.pdv_get_baud

pdv_check = _pdvpycam.pdv_check

pdv_checkfrm = _pdvpycam.pdv_checkfrm

pdv_set_roi = _pdvpycam.pdv_set_roi

pdv_enable_roi = _pdvpycam.pdv_enable_roi

pdv_set_cam_width = _pdvpycam.pdv_set_cam_width

pdv_set_cam_height = _pdvpycam.pdv_set_cam_height

pdv_access = _pdvpycam.pdv_access

pdv_setup_continuous = _pdvpycam.pdv_setup_continuous

pdv_stop_continuous = _pdvpycam.pdv_stop_continuous

pdv_get_min_shutter = _pdvpycam.pdv_get_min_shutter

pdv_get_max_shutter = _pdvpycam.pdv_get_max_shutter

pdv_get_min_gain = _pdvpycam.pdv_get_min_gain

pdv_get_max_gain = _pdvpycam.pdv_get_max_gain

pdv_get_min_offset = _pdvpycam.pdv_get_min_offset

pdv_get_max_offset = _pdvpycam.pdv_get_max_offset

pdv_invert = _pdvpycam.pdv_invert

pdv_wait_last_image = _pdvpycam.pdv_wait_last_image

pdv_wait_next_image = _pdvpycam.pdv_wait_next_image

pdv_get_cam_width = _pdvpycam.pdv_get_cam_width

pdv_get_cam_height = _pdvpycam.pdv_get_cam_height

pdv_force_single = _pdvpycam.pdv_force_single

pdv_variable_size = _pdvpycam.pdv_variable_size

pdv_pause_for_serial = _pdvpycam.pdv_pause_for_serial

pdv_set_defaults = _pdvpycam.pdv_set_defaults

pdv_readcfg = _pdvpycam.pdv_readcfg

pdv_initcam = _pdvpycam.pdv_initcam


