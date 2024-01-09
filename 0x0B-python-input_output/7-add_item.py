#!/usr/bin/python3
""" A script that adds all arguments to a Python list
    and then save them to a file """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_all_arg(filename, *args):
    """ Add command-line arguments to a Python list
    and save it to a JSON file """

    try:
        existing_list = load_from_json_file(filename) or []
    except (FileNotFoundError, ValueError):
        existing_list = []

    # Add new items to the list
    existing_list.extend(args)

    # Save the updated list to the file
    save_to_json_file(existing_list, filename)


if __name__ == "__main__":
    filename = "add_item.json"
    args = sys.argv[1:]

    add_all_arg(filename, *args)
