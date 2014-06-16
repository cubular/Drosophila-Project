import Image
import ImageDraw
import math

def displayCam(draw_mask):
    im = Image.new("L",(640,480))
    frameDraw = ImageDraw.Draw(im)
    for mask in draw_mask:
        frameDraw.point(mask,fill=255)  #draws MMode line on frame
    im.show()
    del frameDraw

def calcMasks():
    """ Calculates mask and draw_mask. Draw mask is set one pixel from mask so that they can be
    incorporated in the same image without the M-mode capturing pixels in the drawn line.  Masks
    are applied to image in FlywxFrame.DisplayCam"""
    n_mmodes = 5
    mask_lib = {}                 # mask = pixels to read for M-mode
    draw_mask_lib = {}            # draw_mask = pixels to draw M-mode line
    
    x_mid = 320         # coordinates of image center, useful shorthand
    y_mid = 240
    spacing = 10
    length = 160
    
    # vertical line
    mask_lib['vertical'] = []
    draw_mask_lib['vertical'] = []
    for i in range(5):
        offset = math.floor(n_mmodes/2)*spacing
        # line_mask is vector of x,y coordinates representing M-mode line
        line_mask = [(x_mid-offset+i*spacing,y_mid-length/2+j) for j in range(length)]
        mask_lib['vertical'].append(line_mask)
        # draw_mask is same as line_mask but offset by 1 for drawing gray line on image that is not recorded
        draw_mask = [(x_mid-offset+i*spacing+1,y_mid-length/2+j) for j in range(length)]
        draw_mask_lib['vertical'].append(draw_mask)
    
    # horizontal line
    mask_lib['horizontal'] = []
    draw_mask_lib['horizontal'] = []
    for i in range(n_mmodes):
        offset = math.floor(n_mmodes/2)*spacing
        # line_mask is vector of x,y coordinates representing M-mode line
        line_mask = [(x_mid-length/2+j,y_mid-offset+i*spacing) for j in range(length)]
        mask_lib['horizontal'].append(line_mask)
        # draw_mask is same as line_mask but offset by 1 for drawing gray line on image that is not recorded
        draw_mask = [(x_mid-length/2+j,y_mid-offset+i*spacing+1) for j in range(length)]
        draw_mask_lib['horizontal'].append(draw_mask)

    # diag line, neg slope
    mask_lib['diag-back'] = []
    draw_mask_lib['diag-back'] = []
    for i in range(n_mmodes):
        offset = math.floor(n_mmodes/2)*spacing
        # line_mask is vector of x,y coordinates representing M-mode line
        line_mask = [(x_mid-length/2-offset+i*spacing+j,y_mid-length/2+offset-i*spacing+j) for j in range(length)]
        mask_lib['diag-back'].append(line_mask)
        # draw_mask is same as line_mask but offset by 1 for drawing gray line on image that is not recorded
        draw_mask = [(x_mid-length/2-offset+i*spacing+j,y_mid-length/2+offset-i*spacing+j+1) for j in range(length)]
        draw_mask_lib['diag-back'].append(draw_mask)
        
    # diag line, pos slope
    mask_lib['diag-forward'] = []
    draw_mask_lib['diag-forward'] = []
    for i in range(n_mmodes):
        offset = math.floor(n_mmodes/2)*spacing
        # line_mask is vector of x,y coordinates representing M-mode line
        line_mask = [(x_mid-length/2-offset+i*spacing+j,y_mid+length/2-offset+i*spacing-j) for j in range(length)]
        mask_lib['diag-forward'].append(line_mask)
        # draw_mask is same as line_mask but offset by 1 for drawing gray line on image that is not recorded
        draw_mask = [(x_mid-length/2-offset+i*spacing+j,y_mid+length/2-offset+i*spacing-j+1) for j in range(length)]
        draw_mask_lib['diag-forward'].append(draw_mask)
    return mask_lib,draw_mask_lib