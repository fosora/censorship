import argparse
from src.debug_mode.args import add_debug_args, add_log_args
from src.image_edition.args import add_image_edition_args
from src.file_management.args import add_file_management_args
from src.nsfw_detection.args import add_nsfw_args 

def get_args():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        prog="censorship",
        usage="python main.py [options]",
        description="Nude Image Censorship Tool"
    )

    add_debug_args(parser)
    add_log_args(parser)
    add_nsfw_args(parser)
    add_file_management_args(parser)
    add_image_edition_args(parser)

    return parser.parse_args()