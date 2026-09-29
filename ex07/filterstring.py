import sys


def main():
    """Filter words longer than the given number."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert isinstance(sys.argv[1], str), "the arguments are bad"
        number = int(sys.argv[2])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        return

    words = sys.argv[1].split()
    result = [
        word for word in words
        if (lambda value: len(value) > number)(word)
    ]

    print(result)


if __name__ == "__main__":
    main()
