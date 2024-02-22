SIZE = 4
SHIPS = 2
SHIP = chr(119)
EMPTY = chr(183)
EQUAL_SIGN = chr(61)


def color_blue(string):
    """
    Returns the input string wrapped in ANSI escape codes to display it in blue color in the console.

    Parameters:
    string (str): The string to be displayed in blue color.

    Returns:
    str: The input string wrapped in ANSI escape codes for blue color.
    """
    return "\033[94m" + string + "\033[0m"


def color_red(string):
    """
    Returns the given string wrapped in ANSI escape codes to display it in red color.

    Parameters:
    string (str): The string to be colored red.

    Returns:
    str: The colored string.
    """
    return "\033[91m" + string + "\033[0m"


def color_yellow(string):
    """
    Returns the input string wrapped in ANSI escape codes to display it in yellow color in the console.

    Parameters:
    string (str): The string to be wrapped.

    Returns:
    str: The input string wrapped in ANSI escape codes.
    """
    return "\033[93m" + string + "\033[0m"


HIT = color_red(chr(88))
MISS = color_blue(chr(164))
