"""
This module provides methods for compiling the plugin via cli.
"""

import argparse
import bootstrap4c4d
import colorama
import os

from bootstrap4c4d.io import Config, \
    CreatePluginConfig, \
    build_plugin, \
    create_plugin
from bootstrap4c4d.utilities.path import assert_directories
from bootstrap4c4d.utilities.cli import \
    cli_format_error, \
    cli_format_success
from bootstrap4c4d.classes.fp import Left, Right


def cli_module_build(args: argparse.Namespace) -> None:
    """
    This method takes all the arguments from cli and tries to build
    the plugin
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

    return build_plugin(Right(config))


def cli_module_create(args: argparse.Namespace) -> None:
    """
    This method takes all the arguments from cli and tries to create
    the plugin
    """
    name = args.name

    template = "tag"

    if args.template == "object":
        template = "object"

    config = CreatePluginConfig(
        name,
        args.destination,
        template
    )

    return create_plugin(Right(config))


def main() -> None:
    """
    This method creates the cli
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
        "name",
        type=str,
        help="name of your plugin"
    )

    create.add_argument(
        "template",
        type=str,
        help="plugin template that should be created (tag|object)"
    )

    create.add_argument(
        "destination",
        type=str,
        help="path to the destination directory"
    )

    args = parser.parse_args()

    if args.module == "build":
        result = cli_module_build(args)

        if isinstance(result, Left):
            print(cli_format_error(result.value))
        else:
            config = result.value

            message = "build plugin {}".format(config.path)

            print(cli_format_success(message))
    elif args.module == "create":
        result = cli_module_create(args)

        if isinstance(result, Left):
            print(cli_format_error(result.value))
        else:
            config = result.value

            message = "build plugin {}".format(config.path)

            print(cli_format_success(message))


if __name__ == "__main__":
    main()
