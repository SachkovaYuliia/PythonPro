def divide(a: int, b: int) -> float:
    """
    Ділить два числа a на b. Якщо b дорівнює нулю, викидає ZeroDivisionError.

    Args:
        a (int): Ділене.
        b (int): Дільник.

    Returns:
        float: Результат поділу.

    Raises:
        ZeroDivisionError: Якщо b дорівнює нулю.
    """
    if b == 0:
        raise ZeroDivisionError("На ноль ділити неможна.")
    return a / b
