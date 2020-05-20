import cv2
import os

def errorHandler(fn):
    def wrapper(*args,**kwargs):
        try:
            return fn(*args,**kwargs)
        except:
            return []
    wrapper.__name__ = fn.__name__
    return wrapper

@errorHandler
def open_img (name, test=True):
    """
    Open an image from OUTPUT and convert it for handling
    """
    test = '_test' if test==True else ''
    path = f'./OUTPUT/{name}{test}.png'
    img = cv2.imread(path, -1)
    return cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

def image_resize(image, width = None, height = None, inter = cv2.INTER_CUBIC):
    """ 
    Wrap of cv2 resize that keeps the height width relation of the picture if desired if desired
    """
    # initialize the dimensions of the image to be resized and grab the image size
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    if height is None:
        # calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    else:
        dim = (width, height)

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

def obj_swapping(image, frame, x, y, h, w, transparency, top=False):
    """
    Substitute a haar feature by a corresponding drawing
    and tracks and redraw the object with the cam movement
    """
    #If the image exist:
    if len(image)!=0:
        #If the drawing is going to be placed on top of the rectangle
        #the height does not need to fit the rectangle height
        height = None if top==True else h
        thing = image_resize(image, width=w, height=height)
        #Get the size of the image:
        thing_h, thing_w, thing_c = thing.shape
        #If the drawing is on top, the height is not defined by the rectangle height,
        #and it is defined differently:
        y_start = y-thing_h if top==True else y
        y_end = y if top==True else y+thing_h
        #If the starting y coordinate is outside of the frame, dont draw it (specially for top drawings)
        if y_start > 0:
            if transparency==1:
                for i in range(y_start, y_end):
                    for e in range(x,x+w):
                        if thing[i-y, e-x, 3] != 0:
                            frame[i,e] = thing[i-y, e-x]
            else:                    
                frame[y_start:y_end, x:x+w] = thing

