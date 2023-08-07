# 1.3 
# - Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# - Перемножьте пары чисел. В новый файл сохраните имя и произведение:
#     если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
#     если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# - В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
# - При достижении конца более короткого файла, возвращайтесь в его начало.

def letter_case(num) -> bool:
    return True if num > 0 else False


def modulus(num) -> bool:
    return num * (-1) if num < 0 else num


def read_from_files():
    
    files: list[str] = ["test_dir/test_1.txt", "test_dir/random_names.txt", "test_dir/test_3.txt"]
    name_list: list[str] = []
    num_list = []
    result_list = []
    diff: int = 0
    count: int = 0
    
    with open(files[0], 'r', encoding='utf-8') as f:
        for line in f:
            if "|" in line:
                temp = line.strip().split(" ")
                num_list.append(
                    eval(f"{temp[0]} * {temp[2]}")
                )
            
    with open(files[1], 'r', encoding='utf-8') as f:
        name_list = list(f)

    diff = len(name_list) - len(num_list)
    if diff > 0:
        while diff != 0:
            if count > len(num_list):
                count = 0
            num_list.append(num_list[count])
            count += 1
            diff = len(name_list) - len(num_list)
    elif diff < 0:
        while diff != 0:
            if count > len(name_list):
                count = 0
            num_list.append(name_list[count])
            count += 1
            diff = len(num_list) - len(name_list)
    
    for i in range(len(name_list)):
        
        if letter_case(num_list[i]):
            name_list[i].lower()
            num_list[i] = int(num_list[i])
        else:
            name_list[i].upper()
            num_list[i] = modulus(num_list[i])
            
        result_list.append(f"{name_list[i].strip()} : {num_list[i]}")
    
    with open(files[2], '+a') as f:
        for line in result_list:
            f.write(f"{line}\n")
    
    
if __name__ == "__main__":
    read_from_files()
