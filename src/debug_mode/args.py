import argparse

def add_log_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        '-v', '--verbose', 
        action='store_true', 
        help='Enable verbose output'
    )
    parser.add_argument(
        '-q', '--quiet', 
        action='store_true', 
        help='Suppress non-error messages'
    )
    parser.add_argument(
        '--logfile', 
        type=str, 
        default='logs', 
        help='Path to the log file (default: logs)'
    )
    parser.add_argument(
        '--logfile-level', 
        type=str, 
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO', 
        help='Logging level for the log file (default: INFO)'
    )

def add_debug_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        '-d', '--debug', 
        action='store_true', 
        help='Enable debug mode to save debug images'
    )
    parser.add_argument(
        '--save-result-json', 
        action='store_true', 
        help='Save the results to a JSON file'
    )
