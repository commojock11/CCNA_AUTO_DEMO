"""Basic Python feature example."""


def greet_user(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    clean_name = name.strip()
    if not clean_name:
        return "Hello, world!"
    return f"Hello, {clean_name.title()}!"


def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet_user("clay"))
    print(add_numbers(2, 3))
