from PIL import Image
import numpy as np
from txt_to_image import TxtToImage


def intensity_to_iter_index(pixel_val, iterable):
    """
    Maps pixel intensity value to index of iterable. Usually a list of ascii symbols with decreasing intensity.

    :param pixel_val: 0-255 int corresponding to intensity of greyscale of a pixel
    :param iterable: list of ascii symbols with decreasing intensity
    :return: index of a ascii symbol corresponding to pixel intensity value
    """
    index = int(pixel_val // (255 / len(iterable)))
    if index == len(iterable):
        index -= 1
    return index


class AsciiTransformer:
    def __init__(self):
        self.image = None
        # could be used " .:-=+*#%@"
        self.symbols_list = [i for i in "@MBHENR#KWXDFPQASUZbdehx*8Gm&04LOVYkpq5Tagns69owz$CIu23Jcfry%1v7l+it[] {" \
                                        "}?j|()=~!-/<>\"^_';,:`. "]
        self.new_width = None
        self.new_height = None

    def load_image(self, path):
        """
        Load image from the path.

        :param path: Path of the image to be transformed
        :return: Returns nothing
        """
        self.image = Image.open(path)

    def set_symbols(self, symbols_str=None):
        """
        Adds characters that will be used in ascii image.

        :param symbols_str: List of letters
        :return: Returns nothing
        """
        symbols_list = []
        if symbols_str:
            for i in symbols_str:
                symbols_list.append(i)
            self.symbols_list = symbols_list

    def resize_image(self, new_width=100):
        """
        Resizes image. Each pixel corresponds to letter.

        :param new_width: Desired width of the resized image
        :return: Returns nothing
        """
        width, height = self.image.size
        aspect_ratio = width / height
        self.new_width = new_width
        self.new_height = int(new_width * aspect_ratio)
        self.image = self.image.resize((self.new_width, self.new_height))

    def convert_to_grayscale(self):
        """
        Converts image to grayscale.

        :return: Returns nothing
        """
        self.image = self.image.convert("L")

    def convert_to_ascii(self, color=False):
        """
        Converts pixels from image to letters based on pixel value.
        You can save pixel colors for later image conversion.

        :param color: Boolean indicating whether image will have colors or not
        :return: 2d numpy_array of letters with proper dimensions
        """
        intensity = self.image.convert("L")
        pixels = intensity.getdata()
        new_pixels = [self.symbols_list[intensity_to_iter_index(pixel, self.symbols_list)] for pixel in pixels]
        symbols_array = np.array(new_pixels)
        if color:
            color_pixels = np.array(self.image.getdata())
            symbols_array = np.array(list(zip(symbols_array, color_pixels)), dtype=object)
            symbols_array = np.reshape(symbols_array, (self.new_height, self.new_width, 2))
        else:
            symbols_array = np.reshape(symbols_array, (self.new_height, self.new_width))
        return symbols_array

    def save_txt(self):
        """
        Saves ascii art to txt file.

        :return: Returns nothing
        """
        symbols_array = self.convert_to_ascii()
        with open("ascii_image.txt", "w") as f:
            for line in symbols_array:
                f.write("".join(line))
                f.write("\n")

    def save_image(self, color=False, b_color="black"):
        """
        Saves ascii art to image.
        You can save image with colors

        :param color: Boolean indicating whether image will be colored or not
        :param b_color: String with name of the color which will be used on the background of the image
        :return: Returns nothing
        """
        symbols_array = self.convert_to_ascii(color)
        converter = TxtToImage()
        converter.load_data(symbols_array)
        converter.imgfy_ascii(b_color)
