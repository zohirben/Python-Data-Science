import sys
import string


def main():
    """Count character categories in a string."""
    if len(sys.argv) == 1:
        print("What is the text to count?")
        text = input()
    else:
        assert len(sys.argv) == 2, \
            "more than one argument is provided"
        text = sys.argv[1]

    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()