# 2. Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# - К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 

from os import rename
from os import listdir


def mass_rename(new_name: str = "test", num_order: int = 0, old_extension: str = "txt", new_extension = "cpp",
                old_name_save: range = [3, 6], path: str = "test/txt/") -> None:
    
    file_list = [i for i in listdir(path) if old_extension in i]
    
    temp_name: str = ""
    
    for file in file_list:
        for i in old_name_save:
            temp_name += file[i]
        
        temp_name += new_name
        temp_name += f"{num_order}"
        num_order += 1
        temp_name += f".{new_extension}"
        
        rename(src=f"{path}{file}",dst=f"{path}{temp_name}")
        
        temp_name = ""
    


if __name__ == "__main__":
    mass_rename()
 