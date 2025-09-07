import argparse    

def add_nsfw_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        '-l', '--labels', 
        type=str, 
        nargs='+', 
        default=[], 
        help='List of labels to detect (default: all labels)'
    )
