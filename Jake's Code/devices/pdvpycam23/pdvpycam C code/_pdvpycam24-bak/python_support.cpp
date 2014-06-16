void py_cam_get_frame (unsigned char **img_data_string, unsigned char *frame_p, int img_size)
{ 
	int ii;
	
	*img_data_string = calloc( (img_size), sizeof(unsigned char) );

	for(ii=0; ii<img_size; ii++)
	{
		*(*img_data_string + ii) = *(frame_p + ii);
	}
}