""" Format the permisson level into a string. """


def format_permisson(level: int):
    """ Format the permisson level into a string. """
    if level == 1:
        return "Partial Permissions"
    if level == 2:
        return "Full Permissions"
    if level == 3:
        return "Owner"
    return "Unknown Permissions"
