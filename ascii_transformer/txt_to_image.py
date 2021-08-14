from PIL import Image, ImageDraw


class TxtToImage:
    def __init__(self):
        self.path = None
        self.symbols_array = None

    def open(self, path):
        """
        Loads txt file to convert to image.

        :param path: path to txt file
        :return: Returns nothing
        """
        self.path = path

    def load_data(self, data):
        """
        Loads 2d np.array with symbols.

        :param data: np.array with str
        :return: Returns nothing
        """
        self.symbols_array = data

    def imgfy_ascii(self, gap=10):
        """
        Converts txt file to image. Original purpose of this method is to save ascii art as images.

        :return: Returns nothing
        """
        if self.path:
            with open(self.path) as f:
                lines = f.readlines()
        else:
            lines = self.symbols_array
        height = gap * len(lines)
        width = gap * len(lines[0])
        image = Image.new("RGB", (width, height), "black")
        draw = ImageDraw.Draw(image)
        for i, line in enumerate(lines):
            for j, cell in enumerate(line):
                symbol = cell[0]
                if len(cell) == 2:
                    color = tuple(cell[1])
                    draw.text((j * gap, i * gap), str(symbol), fill=color)  # x, y
                else:
                    draw.text((j*gap, i*gap), str(symbol))
        image.save("Mao_Zedong_portrait_ascii.png")
