to wrap C++ camera functions:

use pdvpycam.i SWIG interface that includes pvd header "edtinc.h" and py_cam_get_frame to cast to signed char

run SWIG using command prompt:  swig -python pdvpycam.i

in Visual Basic:
	- create blank DLL project
	- add to project:  edtinc.h, libpdv.c, libedt.c, libdvu.c, pdv_bayer_filter.c, pdv_dmy_image.c, pdv_interlace.c, edt_error.c
	- add pdvpycam_wrap.c (created by SWIG)
	- project settings:  	additional include dirs:  c:\python2x\include
				additional dependencies:  c:\python2x\libs\python2x.lib
				use precompiled headers:  No
				Configuration:  Active(Release), not Debug
				Repeat for individual files if necessary

copy pdvpycamxx.py, _pdvpycamxx.dll to python code directory

import _pvdpycam within Python