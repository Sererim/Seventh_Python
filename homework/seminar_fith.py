# 1.5 
# - Доработаем предыдущую задачу. 
# - Создайте новую функцию которая генерирует файлы с разными расширениями. 
# - Расширения и количество файлов функция принимает в качестве параметров. 
# - Количество переданных расширений может быть любым. 
# - Количество файлов для каждого расширения различно. 
# - Внутри используйте вызов функции из прошлой задачи.

from seminar_fourth import make_file

def make_extensions_files(extensions: list[str]=["txt", "md", "bat"], 
                        extension_amount: list[str]=["2", "4", "2"]) -> None:
    
    if len(extensions) != len(extension_amount):
        print("Error!\nNumber of extensions and their amount must be the same.")
    
    try:
        extension_amount = list(map(int, extension_amount))
    except ValueError:
        print("Error!\nAmount of files of certain extension must be a number.")
    
    for i in range(len(extensions)):
        make_file(extension=extensions[i], amount=extension_amount[i])


if __name__ == "__main__":
    make_extensions_files()
