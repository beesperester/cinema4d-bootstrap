"""
This module provides methods for compiling the plugin via cli.
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

import argparse
import bootstrap
import colorama
import os

from bootstrap.io import Config, \
    assert_plugin_config, \
    create_plugin
from bootstrap.utilities.path import assert_directories
from bootstrap.utilities.cli import \
    cli_format_error, \
    cli_format_success
from bootstrap.classes.fp import Left, Right, pipe, chain


def cli_module_build(args: argparse.Namespace) -> None:
    """
    This method takes all the arguments from cli and tries to build
    the plugin.
    """
    plugin_dirname, plugin_filename = os.path.split(args.plugin)
    plugin_name, plugin_extension = os.path.splitext(plugin_filename)

    destination = args.destination

    if not destination:
        destination = plugin_dirname

    root_name = args.root

    if not root_name:
        root_name = "root"

    config = Config(
        args.plugin,
        plugin_name,
        destination,
        root_name,
        None,
        None)

    return pipe([
        chain(assert_plugin_config),
        chain(create_plugin)
    ])(Right(config))


def main() -> None:
    """
    This method creates all the cli.
    """
    parser = argparse.ArgumentParser(
        description="Bootstrap a Cinema 4D plugin."
    )

    subparsers = parser.add_subparsers(
        dest="module",
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
        "-r",
        "--root",
        type=str,
        help="name of root variable"
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

    if args.module == "build":
        result = cli_module_build(args)

        if isinstance(result, Left):
            print(cli_format_error(result.value))


if __name__ == "__main__":
    main()
