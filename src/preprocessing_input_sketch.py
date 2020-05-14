from PIL import Image


def process_input(path):
    im = Image.open(path)
    im = test_custom.resize((28,28),Image.ANTIALIAS)
    im = np.asarray(im.convert('L'))
    im = np.array([255-i for i in im])
    plt.imshow(im, cmap='gray')
    return im.reshape(1,28, 28,1)