import sys


def main() -> None:
    """print argument text more than argument num"""
    args = sys.argv
    if len(args) != 3:
        print("AssertionError: the arguments are bad")
        return

    text = args[1]
    try:
        assert args[2].isdigit(), "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    num = int(args[2])
    is_longer = (lambda w, n: len(w) > n)
    result = [word for word in text.split() if is_longer(word, num)]
    print(result)


if __name__ == "__main__":
    main()
