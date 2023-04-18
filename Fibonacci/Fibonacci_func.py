def fibonacci_recursive(index: int) -> int:
    '''Это рекурсивная функция'''
    if index < 0:
        raise IndexError(f"Index can't be negative: {index}")
    elif index <= 1:
        return index
    else:
        number = fibonacci_recursive(index - 1) + fibonacci_recursive(index - 2)
        return number

def fibonacci_generator() -> int:
    '''Это функция-генератор'''
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
