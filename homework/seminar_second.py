# 1.2
# - Напишите функцию, которая генерирует псевдоимена. 
# - Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. 
# - Полученные имена сохраните в файл

from random import randint, shuffle

    
def random_names():    
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    name: list[str] = []
    vowel: list[str] = ['a', 'e', 'i', 'o', 'u']
    shuffle(letters)
    
    for i in range(0, randint(4, 6)):
        if i == 0:
            name.append(letters[i].upper())
        else:
            name.append(letters[i])
    
    if len(set(name) - set(vowel)) == len(name):
        shuffle(vowel)
        name.append(vowel[0])
    
    with open("test_dir/random_names.txt", '+a') as f:
        for i in name:
            f.write(i)
        f.write('\n')


if __name__ == "__main__":
    random_names()
