def reverse_string(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("Аргумент должен быть строкой")
    return s[::-1]


if __name__ == "__main__":
    user_input = input("Введите строку для реверса: ")
    
    try:
        result = reverse_string(user_input)
        print(f"Результат: {result}")
    except TypeError as e:
        print(f"Ошибка: {e}")
