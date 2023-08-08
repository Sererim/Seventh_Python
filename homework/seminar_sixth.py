# 1.6
# - Дорабатываем функции из предыдущих задач. 
# - Генерируйте файлы в указанную директорию — отдельный параметр функции. 
# - Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 
# - Существующие файлы не должны удаляться/изменяться в случае совпадения имён

from seminar_fourth import make_file
from os import mkdir
from shutil import SameFileError

def make_files_in_directory(extensions: list[str]=["txt", "md", "bat"], 
                        extension_amount: list[str]=["2", "4", "2"], path: str = "test_dir/") -> None:
    
    if len(extensions) != len(extension_amount):
        print("Error!\nNumber of extensions and their amount must be the same.")
    
    try:
        extension_amount = list(map(int, extension_amount))
    except ValueError:
        print("Error!\nAmount of files of certain extension must be a number.")
    
    for i in range(len(extensions)):
        try:
            make_file(extension=extensions[i], amount=extension_amount[i], path=path)
        except FileNotFoundError:
            mkdir(path=path)
            make_file(extension=extensions[i], amount=extension_amount[i], path=path)
        except SameFileError:
            make_file(extension=extensions[i], amount=extension_amount[i], path=path)


if __name__ == "__main__":
    make_files_in_directory(path="test/")
