# 1.7
# - Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# - Каждая группа включает файлы с несколькими расширениями. 
# - В исходной папке должны остаться только те файлы, которые не подошли для сортировки. 

from os import listdir
from os import mkdir
from shutil import move


def sort_files_by_extensions(extensions_list: list[str]=["txt", "md", "bat"], 
                            path:str="test/") -> None:
    """Function to sort files by their extensions and put them into a directories with extension names.
    Args:
        extensions_list (list[str], optional): Extension list for sorting. Defaults to ["txt", "md", "bat"].
        path (str, optional): Path to the sorting directory . Defaults to "test/".
    """
    directory_files_list = listdir(path)
    
    for file in directory_files_list:
        if file in extensions_list:
            directory_files_list.remove(file)
            
    
    for extension in extensions_list:
        try:
            mkdir(f"{path}{extension}")
        except FileExistsError:
            pass
    
    for file in directory_files_list:
        for extension in extensions_list:
            if extension in file:
                move(src=f"{path}{file}", dst=f"{path}{extension}/")
    

if __name__ == "__main__":
    sort_files_by_extensions()
