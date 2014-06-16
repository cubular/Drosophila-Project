/* File : pdvpycam24.i */
%module pdvpycam24

%{
#include "c:\program files\pdv\edtinc.h"
%}
%newobject py_cam_get_frame;

%typemap(newfree) char * {
        free($1);
    }

//%import cstring

%inline %{
char *py_cam_get_frame (unsigned char *frame_p, int img_size)
{ 
	char *img_data = (char *) malloc(img_size);
	//img_data = new char[img_size];
	int i;	
	for(i=0; i<img_size; i++)
	{
		*(img_data+i) = (char) (*(frame_p + i));
	}
	return img_data;
}

%}
typedef EdtDev PdvDev;

PdvDev *pdv_open(char *devname, int unit);
int pdv_close(PdvDev *pdv_p);
void pdv_start_image(PdvDev *pdv_p) ;
void pdv_start_images(PdvDev *pdv_p, int count) ;
unsigned char *pdv_wait_image(PdvDev *pdv_p) ;
unsigned char *pdv_wait_images(PdvDev *pdv_p, int count) ;
int pdv_get_width(PdvDev *pdv_p);
int pdv_get_height(PdvDev *pdv_p);
int pdv_get_imagesize(PdvDev *pdv_p);
int pdv_get_exposure(PdvDev *pdv_p) ;
int pdv_get_gain(PdvDev *pdv_p) ;
int pdv_get_blacklevel(PdvDev *pdv_p) ;
int  pdv_multibuf(EdtDev *edt_p, int numbufs) ;
unsigned char * pdv_wait_last_image(PdvDev * pdv_p, int *nSkipped);
unsigned char * pdv_wait_next_image(PdvDev * pdv_p, int *nSkipped);
