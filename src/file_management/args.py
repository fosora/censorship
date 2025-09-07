import argparse

def add_file_management_args(parser: argparse.ArgumentParser):
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
        '-e', '--extensions', 
        type=str, 
        nargs='+', 
        default=['.jpeg', '.jpg', '.png'], 
        help='List of image file extensions to process (default: .jpeg .jpg .png)'
    )
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='Recursively search for images in subdirectories'
    )
