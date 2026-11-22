import sys


def main() -> None:
    """argument encodes into Morse Code"""
    args = sys.argv

    if len(args) != 2:
        print("AssertionError: more than one argument is provided")
        return

    text = args[1]

    ft_dict = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    result = ""
    for ch in text:
        if ch.islower():
            ch = ch.upper()
        if ch not in ft_dict:
            print("AssertionError: the arguments are bad")
            return
        if result != "":
            result = result + " "
        result = result + ft_dict[ch]
    print(result)


if __name__ == "__main__":
    main()
