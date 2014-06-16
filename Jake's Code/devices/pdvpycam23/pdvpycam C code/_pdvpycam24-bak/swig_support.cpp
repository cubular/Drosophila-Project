
int length = 307200;
unsigned char data[307200];
binary_data result;



binary_data out ()
{
    binary_data result;
    result.size = length;
    result.data = data;
    return result;
}
