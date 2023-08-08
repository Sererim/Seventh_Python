# 1.4
# - Создайте функцию, которая создаёт файлы с указанным расширением. 
# - Функция принимает следующие параметры:
#     расширение
#     минимальная длина случайно сгенерированного имени, по умолчанию 6
#     максимальная длина случайно сгенерированного имени, по умолчанию 30
#     минимальное число случайных байт, записанных в файл, по умолчанию 256
#     максимальное число случайных байт, записанных в файл, по умолчанию 4096
#     количество файлов, по умолчанию 42
#     Имя файла и его размер должны быть в рамках переданного диапазона.

from random import shuffle
from random import randint
from random import randbytes
from shutil import copyfile


def get_random_name(min_lenght: int, max_lenght: int) -> str:    
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    name: list[str] = []
    vowel: list[str] = ['a', 'e', 'i', 'o', 'u']
    result: str = ""
    count: int = 0
    
    shuffle(letters)
    
    if max_lenght > len(letters):
        while max_lenght > len(letters):
            if count > len(letters):
                count = 0
            count += 1
            letters.append(letters[count])
    
    for i in range(0, randint(min_lenght, max_lenght)):
        if i == 0:
            name.append(letters[i].upper())
        else:
            name.append(letters[i])
    
    if len(set(name) - set(vowel)) == len(name):
        shuffle(vowel)
        name.append(vowel[0])
    
    for i in name:
        result += i
    
    return result


def get_random_bytes(min_bytes: int, max_bytes: int) -> bytes:
    return randbytes(randint(min_bytes, max_bytes))


def make_file(extension: str = "txt", min_lenght: int = 6, max_lenght: int = 30,
              min_bytes: int = 256, max_bytes: int = 4096, amount: int = 42, path: str = "test_dir/") -> None:
    file_name = f"{get_random_name(min_lenght, max_lenght)}"
    content = get_random_bytes(min_bytes, max_bytes).decode(errors='ignore')
    
    with open(f"{path}{file_name}.{extension}", '+w', encoding='utf-8') as f:
        f.write(content)
    
    for i in range(amount):
        copyfile(f"{path}{file_name}.{extension}", f"{path}/{file_name}{i}.{extension}")
    

if __name__ == "__main__":
    # print(get_random_name(6, 30))
    # print(get_random_bytes(20, 50))
    print(make_file())
