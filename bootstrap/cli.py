"""
This module provides methods for compiling the plugin via cli.
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

import argparse
import bootstrap
import colorama
import importlib
import os

from bootstrap.utilities.path import assert_directories
from bootstrap.classes.fp import Left, Right, Pipe


def cli_format_error(message: str) -> str:
    """
    This method takes an error message and formats it with a red
    colored "Error:" prefix for displaying it in the console.
    """
    return "{} {}".format(
        colorama.Fore.RED + "Error:" + colorama.Style.RESET_ALL,
        message
    )


def assert_plugin_path(config):
    if (
        os.path.isfile(config["plugin_path"]) and
        config["plugin_path"].endswith(".py")
    ):
        return Right(config)

    return Left("{} is not a valid python file".format(config["plugin_path"]))


def assert_python_module(config):
    plugin_dirname, plugin_filename = os.path.split(config["plugin_path"])
    plugin_name, plugin_extension = os.path.splitext(plugin_filename)

    spec = importlib.util.spec_from_file_location(
        plugin_name,
        config["plugin_path"]
    )

    if spec:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        destination = config["destination"]

        if not destination:
            destination = plugin_dirname

        return Right({
            **config,
            "module": module,
            "destination": destination
        })

    return Left("{} is not a valid python module".format(plugin))


def assert_root_attribute(config):
    try:
        root = getattr(config["module"], "root")

        return Right({
            **config,
            "root": root
        })
    except AttributeError as e:
        return Left(e)


def assert_root_attribute_type(config):
    if isinstance(config["root"], bootstrap.Description):
        return Right(config)

    return Left((
        "plugin must define variable \"root\" ",
        "of type \"bootstrap.Description\""
    ))


def assert_destination(config):
    try:
        assert_directories(config["destination"])

        return Right(config)
    except Exception as e:
        return Left(e)


def module_build(args: argparse.Namespace) -> None:
    """
    This method takes all the arguments from cli and tries to build
    the plugin.
    """

    config = {
        "plugin_path": args.plugin,
        "destination": args.destination
    }

    result = Pipe([
        assert_plugin_path,
        assert_python_module,
        assert_root_attribute,
        assert_root_attribute_type,
        assert_destination
    ])(Right(config))

    if isinstance(result, Left):
        raise AssertionError(result.value)


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

    try:
        if args.module == "build":
            module_build(args)
    except AssertionError as e:
        print(cli_format_error(e))


if __name__ == "__main__":
    main()
