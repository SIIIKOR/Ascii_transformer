## Asciify
Program that allows you to convert image to ascii art.
you can save it in txt file or in png format, in color or not.

## Usage
```bash
python3 asciify.py image_name.png -h
```
```bash
asciify.py [-h] [-w WIDTH] [-i] [-c] [-s SYMBOLS_LIST] image_path
```
### positional arguments:
```
  image_path            Path of image to be transformed into ascii art.
```

### optional arguments:
```
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        Insert desired image width
  -i, --image           Choose IMAGE mode else TXT mode
  -c, --color           Ascii art in IMAGE mode will have colors
  -s SYMBOLS_LIST, --symbols_list SYMBOLS_LIST
                        Insert symbols_list which will be used in ascii art
```

### Example:
```bash
python3 asciify.py pika.png -i -c -w 100 -s jfkd
```