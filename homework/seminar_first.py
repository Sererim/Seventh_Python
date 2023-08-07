# 1.1
#     - Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. 
#     - Первое число int, второе - float разделены вертикальной чертой. 
#     - Минимальное число - -1000, максимальное - +1000. 
#     - Количество строк и имя файла передаются как аргументы функции.
from random import randint, random

def fill_file(file_name: str, line: int = -1) -> None:
    with open(file_name, 'a') as f:
        f.seek(line)
        f.write(
            f"{randint(-1000, 1000)} | {random(-1000, 1001)}"
        )


if __name__ == "__main__":
    pass
