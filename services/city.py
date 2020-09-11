from typing import Union
from pytils import translit


def get_city_line_by_id(geonameid: int) -> Union[str, bool]:
    # Получаем строку с городом по geonameid

    file = open('data/RU.txt', 'r')
    for line in file:
        if line.split('\t')[0] == str(geonameid):
            return line

    return False


def get_city_by_name(ru_name: str) -> Union[str, bool]:
    # Получаем строку с городом по названию города

    file = open('data/RU.txt', 'r')
    translit_name: str = translit.translify(ru_name)

    city_line = None
    for line in file:
        print(line)
        if line.split(' ')[1] == translit_name:
            if city_line is None:
                city_line: str = line

            else:
                pass

    return False

