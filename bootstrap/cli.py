"""
This module provides methods for compiling the plugin via cli.
"""

__author__ = "Bernhard Esperester <bernhard@esperester.de>"

import argparse
import bootstrap
import colorama
import importlib
import os

from bootstrap.io import \
    write_resource, \
    write_header, \
    write_locales, \
    compile_plugin
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


def cli_format_success(message: str) -> str:
    """
    This method takes a success message and formats it with a green
    colored "Success:" prefix for displaying it in the console.
    """
    return "{} {}".format(
        colorama.Fore.GREEN + "Success:" + colorama.Style.RESET_ALL,
        message
    )


def assert_plugin_path(config: dict) -> dict:
    if (
        os.path.isfile(config["plugin_path"]) and
        config["plugin_path"].endswith(".py")
    ):
        return Right(config)

    return Left("{} is not a valid python file".format(config["plugin_path"]))


def assert_python_module(config: dict) -> dict:
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
            "destination": destination,
            "name": plugin_name
        })

    return Left("{} is not a valid python module".format(plugin))


def assert_root_attribute(config: dict) -> dict:
    try:
        root = getattr(config["module"], "root")

        return Right({
            **config,
            "root": root
        })
    except AttributeError as e:
        return Left(e)


def assert_root_attribute_type(config: dict) -> dict:
    if isinstance(config["root"], bootstrap.Description):
        return Right(config)

    return Left((
        "plugin must define variable 'root' ",
        "of type 'bootstrap.Description'"
    ))


def assert_destination(config: dict) -> dict:
    try:
        assert_directories(config["destination"])

        return Right(config)
    except Exception as e:
        return Left(e)


def build_resource(config: dict) -> dict:
    try:
        result = write_resource(
            config["root"],
            config["destination"],
            config["name"]
        )

        message = "done writing {}".format(result)

        print(cli_format_success(message))

        return Right(config)
    except Exception as e:
        return Left(e)


def build_header(config: dict) -> dict:
    try:
        result = write_header(
            config["root"],
            config["destination"],
            config["name"]
        )

        message = "done writing {}".format(result)

        print(cli_format_success(message))

        return Right(config)
    except Exception as e:
        return Left(e)


def build_locales(config: dict) -> dict:
    try:
        result = write_locales(
            config["root"],
            config["destination"],
            config["name"]
        )

        message = "done writing {}".format(result)

        print(cli_format_success(message))

        return Right(config)
    except Exception as e:
        return Left(e)


def build_plugin(config: dict) -> dict:
    try:
        result = compile_plugin(
            config["plugin_path"],
            config["destination"],
            config["name"]
        )

        message = "done writing {}".format(result)

        print(cli_format_success(message))

        return Right(config)
    except Exception as e:
        return Left(e)


def create_plugin(config: dict) -> dict:
    return Pipe([
        build_resource,
        build_header,
        build_locales,
        build_plugin
    ])(Right(config))


def assert_plugin_config(config: dict) -> dict:
    return Pipe([
        assert_plugin_path,
        assert_python_module,
        assert_root_attribute,
        assert_root_attribute_type,
        assert_destination
    ])(Right(config))


def cli_module_build(args: argparse.Namespace) -> None:
    """
    This method takes all the arguments from cli and tries to build
    the plugin.
    """

    config = {
        "plugin_path": args.plugin,
        "destination": args.destination
    }

    return Pipe([
        assert_plugin_config,
        create_plugin
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
