import cv2
import os

# source: https://stackoverflow.com/a/44659589

def errorHandler(fn):
    def wrapper(*args,**kwargs):
        try:
            return fn(*args,**kwargs)
        except:
            return []
    wrapper.__name__ = fn.__name__
    return wrapper

@errorHandler
def open_img (name, ):
    """
    Open an image from OUTPUT and convert it for handling
    """
    path = f'./OUTPUT/{name}_test.jpg'
    img = cv2.imread(path, -1)
    return cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

def image_resize(image, width = None, height = None, inter = cv2.INTER_CUBIC):
    """ 
    Wrap of cv2 resize that keeps the height width relation of the picture if desired if desired
    """
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]
    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image
    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # otherwise, the height is None
    if height is None:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    else:
        dim = (width, height)

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)
    # return the resized image
    return resized





