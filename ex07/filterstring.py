import sys


def main():
    """Filter words longer than the given number."""
    assert len(sys.argv) == 3, "the arguments are bad"
    assert isinstance(sys.argv[1], str), "the arguments are bad"

    try:
        number = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = sys.argv[1].split()

    is_long = lambda word: len(word) > number
    result = [word for word in words if is_long(word)]

    print(result)


if __name__ == "__main__":
    main()