from return_data_file import data_file
from return_data_file_2 import data_file_2

def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер строки которую хотите скопировать\n"
                               f" от 1 до {count_rows}:  "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки\n"
                                   f"от 1 до {count_rows}: "))
        with open(f"db/data_{nf}.txt", 'r', encoding='utf_8') as f:
            lst = f.readlines()[number_row - 1]
        data_2, ns = data_file_2()
        count_rows = len(data_2)
        with open(f"db/data_{ns}.txt", 'a', encoding='utf_8') as j:
            j.write(lst)
        print("Строка успешно скопирована!")

    

    # data_2, ns = data_file_2()
    # count_rows = len(data_2)
    # with open(f'db/data_{nf}.txt','r', encoding='utf-8') as firstfile, open(f'db/data_{ns}.txt','w', encoding='utf-8') as secondfile:
    #     for line in firstfile:
    #         secondfile.write(line)
    

    # print("Файл успешно скопирован!")