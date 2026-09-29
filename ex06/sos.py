import sys


def main():
    """Encode an alphanumeric string into Morse code."""
    morse = {
        " ": "/", "A": ".-", "B": "-...", "C": "-.-.",
        "D": "-..", "E": ".", "F": "..-.", "G": "--.",
        "H": "....", "I": "..", "J": ".---", "K": "-.-",
        "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
        "T": "-", "U": "..-", "V": "...-", "W": ".--",
        "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----",
        "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..",
        "9": "----.",
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        text = sys.argv[1].upper()
        assert all(char in morse for char in text), \
            "the arguments are bad"

        print(" ".join(morse[char] for char in text))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
