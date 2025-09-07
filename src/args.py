import argparse

def valid_pixel_size(pixel_size):
    pixel_size = int(pixel_size)
    if pixel_size < 1 or pixel_size > 256:
        raise argparse.ArgumentTypeError(f"The value {pixel_size} is not between 1 and 256.")
    return pixel_size

def get_args():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Nude Image Censorship Tool"
    )
    parser.add_argument(
        '-i', '--input', 
        type=str, 
        default='files', 
        help='Input directory containing images to process'
    )
    parser.add_argument(
        '-o', '--output', 
        type=str, 
        default='output', 
        help='Output directory to save processed images'
    )
    parser.add_argument(
        '-p', '--pixel-size', 
        type=valid_pixel_size, 
        default=3, 
        help='Pixelation block size for censorship (default: 3)'
    )
    parser.add_argument(
        '-d', '--debug', 
        action='store_true', 
        help='Enable debug mode to save debug images'
    )
    return parser.parse_args()