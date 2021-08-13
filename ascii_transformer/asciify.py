import argparse
from ascii_transformer import AsciiTransformer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Path of image to be transformed into ascii art.", type=str)
    parser.add_argument("-w", "--width", help="Insert desired image width", type=int, default=100)
    parser.add_argument("-i", "--image", help="Choose IMAGE mode else TXT mode", action='store_true')
    parser.add_argument("-c", "--color", help="Ascii art in IMAGE mode will have colors", action='store_true')
    parser.add_argument("-s", "--symbols_list", help="Insert symbols_list which will be used in ascii art", type=str)

    args = parser.parse_args()
    trans = AsciiTransformer()
    trans.load_image(args.image_path)
    trans.resize_image(args.width)
    trans.set_symbols(args.symbols_list)
    if args.image:
        trans.save_image(args.color)
    else:
        trans.save_txt()


if __name__ == '__main__':
    main()
