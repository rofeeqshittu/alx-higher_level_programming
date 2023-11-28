#!/usr/bin/python3
import types


def print_hidden_names(module):
    names = dir(module)
    filtered_names = [name for name in names if not name.startwith("__")]

    sorted_names = sorted(filtered_names)
    for name in sorted_names:
        print("{}".format(name))


if __name__ == "__main__":
    # Load the compiled module
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
        module = types.ModuleType("hidden_4")
        exec(compile(code, "hidden_4.pyc", "exec"), module.__dict__)

        # Print the hidden names
        print_hidden_names(module)
