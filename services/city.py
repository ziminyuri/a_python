from typing import Union
from pytils import translit
from services.transform import get_dict_from_city_str


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


def get_northern_city(city_1: str, city_2: str) -> dict:
    if city_1 and city_2:
        city_1_dict: dict = get_dict_from_city_str(city_1)
        city_2_dict: dict = get_dict_from_city_str(city_2)

        if float(city_1_dict['latitude']) > float(city_2_dict['latitude']):
            return city_1_dict
        else:
            return city_2_dict

    elif city_1:
        return {"Error": "There is no city №2"}

    elif city_2:
        return {"Error": "There is no city №1"}

    else:
        return {"Error": "There is no cities with such names"}


def _get_population_from_city_line(city: str) -> float:
    population = city.split('\t')[14]
    return float(population)
