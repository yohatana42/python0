import sys


def main() -> None:
    """count kind character"""
    args = sys.argv

    if len(args) > 2:
        print("AssertionError: more than one argument is provided")
        return

    text_len = 0
    upper = 0
    lower = 0
    punc = 0
    space = 0
    digit = 0

    if len(args) == 1:
        print("What is the text to count?")
        try:
            text = sys.stdin.readline()
        except EOFError:
            return
        text_len = len(text)
    elif len(args) == 2:
        text = args[1]
        text_len = len(args[1])

    for char in text:
        if char.isupper():
            upper = upper + 1
        elif char.islower():
            lower = lower + 1
        elif char.isspace():
            space = space + 1
        elif char.isdigit():
            digit = digit + 1
        else:
            punc = punc + 1

    print("The text contains " f"{text_len}" " characters:")
    print(f"{upper}" " upper letters") 
    print(f"{lower}" " lower letters") 
    print(f"{punc}" " punctuation marks")
    print(f"{space}" " spaces")
    print(f"{digit}" " digits")

if __name__ == "__main__":
    main()