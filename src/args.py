import argparse

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
        type=int, 
        default=3, 
        help='Pixelation block size for censorship (default: 3)'
    )
    parser.add_argument(
        '-d', '--debug', 
        action='store_true', 
        help='Enable debug mode to save debug images'
    )
    return parser.parse_args()