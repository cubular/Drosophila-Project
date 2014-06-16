# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _pdvpycam23
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


py_cam_get_frame = _pdvpycam23.py_cam_get_frame
pdv_open = _pdvpycam23.pdv_open
pdv_close = _pdvpycam23.pdv_close
pdv_start_image = _pdvpycam23.pdv_start_image
pdv_start_images = _pdvpycam23.pdv_start_images
pdv_wait_image = _pdvpycam23.pdv_wait_image
pdv_wait_images = _pdvpycam23.pdv_wait_images
pdv_get_width = _pdvpycam23.pdv_get_width
pdv_get_height = _pdvpycam23.pdv_get_height
pdv_get_imagesize = _pdvpycam23.pdv_get_imagesize
pdv_get_exposure = _pdvpycam23.pdv_get_exposure
pdv_get_gain = _pdvpycam23.pdv_get_gain
pdv_get_blacklevel = _pdvpycam23.pdv_get_blacklevel
pdv_multibuf = _pdvpycam23.pdv_multibuf
pdv_wait_last_image = _pdvpycam23.pdv_wait_last_image
pdv_wait_next_image = _pdvpycam23.pdv_wait_next_image


