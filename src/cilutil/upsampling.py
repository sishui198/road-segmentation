from PIL import Image


def upsample_training(filenames, correct_size=(400, 400)):
    """Upsample training images."""
    print("Upsampling training images to %dx%d" % correct_size)
    resize_(filenames, correct_size)


def upsample_test(filenames, correct_size=(608, 608)):
    """Upsample test images."""
    print("Upsampling test images to %dx%d" % correct_size)
    resize_(filenames, correct_size)


def resize_(filenames, correct_size):
    """Resize given images to the correct size."""
    for filename in filenames:
        print("Resizing " + filename)
        im = Image.open(filename)
        im = im.resize(correct_size, Image.ANTIALIAS)
        im.save(filename, "PNG")