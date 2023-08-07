# 1.1
#     - Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. 
#     - Первое число int, второе - float разделены вертикальной чертой. 
#     - Минимальное число - -1000, максимальное - +1000. 
#     - Количество строк и имя файла передаются как аргументы функции.
from random import randint, random

def fill_file(file_name: str, line: int = 0) -> None:
    """Simple function to fill a fill a text file with two numbers separated by a line,
    the first number is integer,
    the second number is float point number
    all numbers are within [-1000, 1000]

    Args:
        file_name (str): file name
        line (int, optional): Line from where the changes happen. Defaults to 0.
    """
    with open(file_name, 'r+', encoding="utf-8") as f:
        if line == 0:
            f.seek(line, 2)
        else:
            f.seek(line, 0)
        
        f.write(
            f"{randint(-1000, 1000)} | {randint(-1000, 1000) + random()}\n"
        )


if __name__ == "__main__":
    name: str = "test_dir/test_1.txt"
    fill_file(name)
    fill_file(name, 10)
    fill_file(name, 20)
