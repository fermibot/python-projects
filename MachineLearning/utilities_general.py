import datetime
import sys

# ANSI escape codes for colors and styles
colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",  # Reset to default color
}
styles = {
    "bold": "\033[1m",
    "underline": "\033[4m",
    "reset": "\033[0m",  # Reset to default style
}


def print_formatter(message, color=None, style=None):
    """
    Prints a message with a timestamp and optional color and style.

    Args:
        message (str): The message to print.
        color (str, optional): The color to use (e.g., "red", "green", "blue").
                               Defaults to None.
        style (str, optional): The style to use (e.g., "bold", "underline").
                               Defaults to None.
    """
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    color_code = colors.get(color.lower(), "") if color else ""
    style_code = styles.get(style.lower(), "") if style else ""

    print(f"{timestamp} {color_code}{style_code}{message}{colors['reset']}{styles['reset']}")


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    # Print Newline on Complete
    if iteration == total:
        print()
