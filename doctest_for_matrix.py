# Завдання 8. Тестування з використанням doctest та покриття складних сценаріїв (опціонально)

# Додайте документацію з прикладами використання більш складних функцій, які включають роботу з матрицями. Реалізуйте функції для роботи з матрицями:

# matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]: множення двох матриць.
# transpose_matrix(matrix: List[List[int]]) -> List[List[int]]: транспонування матриці.

from typing import List

def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Множить дві матриці.

    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]

    >>> matrix_multiply([[2, 0], [0, 2]], [[1, 2], [3, 4]])
    [[2, 4], [6, 8]]

    >>> matrix_multiply([[1]], [[1]])
    [[1]]

    >>> matrix_multiply([[1, 2]], [[3], [4]])
    [[11]]

    Помилка: неправильні розміри матриць
    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6]])
    Traceback (most recent call last):
        ...
    ValueError: Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої.
    """

    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    if cols_matrix1 != rows_matrix2:
        raise ValueError("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої.")

    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Транспонує матрицю.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]

    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]

    >>> transpose_matrix([[1]])
    [[1]]

    >>> transpose_matrix([[5, -2], [0, 7], [8, 9]])
    [[5, 0, 8], [-2, 7, 9]]

    Порожня матриця:
    >>> transpose_matrix([])
    []
    """
    
    if not matrix:
        return []
    return list(map(list, zip(*matrix)))
