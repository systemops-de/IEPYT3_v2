"""
This program is to great the new incomer to WBS.
"""


def greeting(message):
    """_summary_

    Args:
        message(type): _description_

    Returns:
        _type_: _description_
    """
    teilnehmende = ["Thomas", "Ingo", "Sara", "Lena"]

    for tn in teilnehmende:
        print(f"{message}, {tn.title()}")

    return True


def main():
    """_summary_
    """
    pass
