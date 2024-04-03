from print_data import print_file


def choice_number_file_2():
    print_file()
    number_row2 = int(input("Выберете файл в которй хотите скопировать\n"
                                    "Введите цифру 1, 2 или 3: "))
    while number_row2 < 1 or number_row2 > 3:
        number_row2 = int(input("Ошибка!!!\n"
                                "Введите цифру 1, 2 или 3: "))
    return number_row2