"""
This module provides methods for working with the cli
"""

import colorama


def cli_format_error(message: str) -> str:
    """
    This method takes an error message and formats it with a red
    colored "Error:" prefix for displaying it in the console
    """
    return "{} {}".format(
        colorama.Fore.RED + "Error:" + colorama.Style.RESET_ALL,
        message
    )


def cli_format_success(message: str) -> str:
    """
    This method takes a success message and formats it with a green
    colored "Success:" prefix for displaying it in the console
    """
    return "{} {}".format(
        colorama.Fore.GREEN + "Success:" + colorama.Style.RESET_ALL,
        message
    )
