def star_pyramid(n: int) -> None:
    """Print a centered pyramid of '*' of height n."""
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
