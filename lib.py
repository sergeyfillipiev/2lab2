def fibonacci(n):
    """Возвращает список из n чисел Фибоначчи."""
    if n <= 0:
        raise ValueError("n должно быть положительным числом")
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def bubble_sort(arr):
    """Сортировка пузырьком."""
    sorted_arr = arr[:]
    n = len(sorted_arr)
    for i in range(n):
        for j in range(n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j]
    return sorted_arr

def calculator(a, b, operation):
    """Простой калькулятор."""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b
    else:
        raise ValueError("Неподдерживаемая операция")
