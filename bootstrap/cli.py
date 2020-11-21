"""
This module provides methods for compiling the plugin via cli.
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

import argparse


def main():
    parser = argparse.ArgumentParser(description="Build a Cinema 4D plugin.")

    # parser.add_argument("test", type=str, help="path to a plugin python file")

    subparsers = parser.add_subparsers(
        help="sub-command help"
    )

    build = subparsers.add_parser(
        "build",
        help="build an existing plugin"
    )

    build.add_argument(
        "plugin",
        type=str,
        help="path to a plugin python file"
    )

    build.add_argument(
        "-d",
        "--destination",
        type=str,
        help="path to the destination directory"
    )

    create = subparsers.add_parser(
        "create",
        help="create a new plugin from scratch"
    )

    create.add_argument(
        "plugin",
        type=str,
        help="path where plugin should be created"
    )

    create.add_argument(
        "type",
        type=str,
        help="type of plugin that should be created"
    )

    args = parser.parse_args()

    print(args)


if __name__ == "__main__":
    main()
