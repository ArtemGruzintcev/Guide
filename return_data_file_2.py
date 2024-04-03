from choice_file_2 import choice_number_file_2


def data_file_2():
    ns = choice_number_file_2()
    with open(f'db/data_{ns}.txt', 'r', encoding='utf-8') as file:
        data_2 = file.readlines()
    return data_2, ns