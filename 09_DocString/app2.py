# Variable Annotation

x: int = 10
y: float = 20.2
z: str = "Python"






# Parameter Annotation
def greeting(first_name: str) -> bool:
    """To great every new employee

    Args:
        first_name (str): The name of the employee

    Returns:
        bool: confirmation of greeting
    """

    result: bool = True

    print("Hello", first_name)

    return result


x = str(x)

print(x)
