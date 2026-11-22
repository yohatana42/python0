import sys


def main() -> None:
    """ function :command-line argument is odd or even. """
    args = sys.argv

    if len(args) == 1:
        return
    elif len(args) != 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        if args[1].startswith("-"):
            body = args[1][1:]
        else:
            body = args[1]
        assert body.isdigit(), "argument is not an integer"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    val = int(args[1])
    if val % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
