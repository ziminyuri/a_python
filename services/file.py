def count_number_of_lines_in_file() -> int:
    # Возвращаем количество строк в файле

    file_name: str = 'data/RU.txt'
    return len(open(file_name).readlines())
