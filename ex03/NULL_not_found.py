from typing import Any


def NULL_not_found(object: Any) -> int:
    """ object is "null-like" values, return 0 """
    if type(object) is type(None):
        print("Nothing: " f"{object}" " " f"{type(object)}")
        return (0)
    elif type(object) is float and object != object:
        print("Cheese: " f"{object}" " " f"{type(object)}")
        return (0)
    elif type(object) is int and object == 0:
        print("Zero: " f"{object}" " " f"{type(object)}")
        return (0)
    elif type(object) is str and object == "":
        print("Empty: " f"{object}" f"{type(object)}")
        return (0)
    elif type(object) is bool and object is False:
        print("Fake: " f"{object}" " " f"{type(object)}")
        return (0)
    print("Type not Found")
    return (1)
