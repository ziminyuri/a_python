from typing import Union
from pytils import translit


def get_city_line_by_id(geonameid: int) -> Union[str, bool]:
    # Получаем строку с городом по geonameid

    file = open('data/RU.txt', 'r')
    for line in file:
        if line.split('\t')[0] == str(geonameid):
            return line

    return False


def get_city_by_ru_name(ru_name: str) -> Union[str, bool]:
    # Получаем строку с городом по названию города

    file = open('data/RU.txt', 'r')
    translit_city_name: str = translit.translify(ru_name)

    city_line = ''
    for line in file:
        print(line)
        i_city_name: str = line.split('\t')[1]
        if i_city_name == translit_city_name:
            if city_line == '':
                city_line: str = line

            else:
                if _get_population_from_city_line(city_line) < _get_population_from_city_line(line):
                    city_line: str = line
    if city_line:
        return city_line

    else:
        return False


def _get_population_from_city_line(city: str) -> float:
    population = city.split('\t')[14]
    return float(population)
