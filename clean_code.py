"""
A simple and clean Python module for demonstration.
"""

def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def subtract_numbers(a: int, b: int) -> int:
    """Return the difference of two integers."""
    return a - b


def main() -> None:
    """Main function to execute sample operations."""
    x = 10
    y = 5

    print("Addition:", add_numbers(x, y))
    print("Subtraction:", subtract_numbers(x, y))


if __name__ == "__main__":
    main()