from typing import Any


def all_thing_is_obj(object: Any) -> int:
    if type(object) is str:
        print(object, "is in the kitchen : " f"{type(object)}")
    elif type(object) is list:
        print("List : " f"{type(object)}")
    elif type(object) is tuple:
        print("Tuple : " f"{type(object)}")
    elif type(object) is set:
        print("Set : " f"{type(object)}")
    elif type(object) is dict:
        print("Dict : " f"{type(object)}")
    else:
        print("Type not found")
    return (42)
