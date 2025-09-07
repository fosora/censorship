import argparse

def valid_pixel_size(pixel_size):
    pixel_size = int(pixel_size)
    if pixel_size < 1 or pixel_size > 256:
        raise argparse.ArgumentTypeError(f"The value {pixel_size} is not between 1 and 256.")
    return pixel_size

def add_image_edition_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        '-p', '--pixel-size', 
        type=valid_pixel_size, 
        default=3, 
        help='Pixelation block size for censorship (default: 3)'
    )
    parser.add_argument(
        '-b', '--blur', 
        action='store_true', 
        help='Apply blur effect for censorship instead of pixelation (Not working yet)',
    )