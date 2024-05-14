import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")

    parser.add_argument(
        "--fullscreen",
        action="store_true",
        help="Run the application in fullscreen mode",
    )
    parser.add_argument(
        "--width", type=int, default=1200, help="Set the width of the application"
    )
    parser.add_argument(
        "--height", type=int, default=800, help="Set the height of the application"
    )

    return parser.parse_args()
