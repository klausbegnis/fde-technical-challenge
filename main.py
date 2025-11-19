MAX_VOLUME = 1_000_000  # cm³
MAX_SIDE_LENGTH = 150  # cm
MAX_MASS = 20  # kg


def validate_package(width: float, height: float, length: float, mass: float) -> bool:
    """Validate the package.

    Args:
        width (float): The width of the package (cm).
        height (float): The height of the package (cm).
        length (float): The length of the package (cm).
        mass (float): The mass of the package (kg).

    Returns:
        bool: True if the package is valid, False otherwise.
    """
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        return False
    return True


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Sort the package into a stack.

    Args:
        width (float): The width of the package (cm).
        height (float): The height of the package (cm).
        length (float): The length of the package (cm).
        mass (float): The mass of the package (kg).

    Returns:
        str: The stack of the package.
    """
    if not validate_package(width, height, length, mass):
        raise ValueError("Invalid package dimensions")
    # Calculate volume
    volume = width * height * length

    # Check if the package is oversized
    has_big_volume = volume >= MAX_VOLUME  # cm³
    has_any_side_too_long = (
        width >= MAX_SIDE_LENGTH
        or height >= MAX_SIDE_LENGTH
        or length >= MAX_SIDE_LENGTH
    )  # cm

    # Check if the package is bulky or heavy
    is_bulky = has_big_volume or has_any_side_too_long
    is_heavy = mass >= MAX_MASS

    # Return the classification
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"


if __name__ == "__main__":
    print(sort(100, 100, 100, 10))
