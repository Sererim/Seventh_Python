# 1.1
#     - Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. 
#     - Первое число int, второе - float разделены вертикальной чертой. 
#     - Минимальное число - -1000, максимальное - +1000. 
#     - Количество строк и имя файла передаются как аргументы функции.
from random import randint, random

def fill_file(file_name: str, line: int = 0) -> None:
    with open(file_name, 'a', encoding="utf-8") as f:
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
