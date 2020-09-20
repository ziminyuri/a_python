from typing import Union

from pytils import translit
from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta

from services.transform import get_dict_from_city_str


def get_cities(page: int, count: int) -> list:
    # Получаем словарь состоящий из городов

    if page == 1:
        line_begin: int = 0
    else:
        line_begin: int = (page - 1) * count

    results: list = []
    with open('data/RU.txt') as f:
        lines = f.readlines()
        for i in range(line_begin, line_begin + count):

            try:
                city: dict = get_dict_from_city_str(lines[i])
                results.append(city)
            except:
                break

    return results


def get_city_line_by_id(geonameid: int) -> Union[str, bool]:
    # Получаем строку с городом по geonameid

    file = open('data/RU.txt', 'r')
    for line in file:
        if line.split('\t')[0] == str(geonameid):
            return line

    return False


def get_city_by_ru_name(ru_name: str) -> Union[str, bool]:
    # Получаем строку с городом по названию города

    file = _file_open()
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


def is_same_time_zone(city_1: str, city_2: str) -> dict:
    # Вовращает словарь со значением True, если временная зона одинаковая

    if city_1 and city_2:
        city_1_dict: dict = get_dict_from_city_str(city_1)
        city_2_dict: dict = get_dict_from_city_str(city_2)

        if (city_1_dict['timezone']) == (city_2_dict['timezone']):
            return {"Time zones the same": "True"}

        else:
            timezone_1 = city_1_dict['timezone']
            timezone_2 = city_2_dict['timezone']

            time_zone_difference = _tz_diff(timezone_1, timezone_2)
            return{"Time zones the same": "False", 'Time zone difference': time_zone_difference}

    elif city_1:
        return {"Error": "There is no city №2"}

    elif city_2:
        return {"Error": "There is no city №1"}

    else:
        return {"Error": "There is no cities with such names"}


def search_cities_by_part_name(part_name: str) -> dict:
    # Поиск городов по части названия

    file = _file_open()
    translit_part_name: str = translit.translify(part_name)

    cities: list = []
    for line in file:
        i_city_name: str = line.split('\t')[1]
        if translit_part_name in i_city_name:
            cities.append(i_city_name)

    search_cities: dict = {}

    if cities:
        i: int = 1
        for city in cities:
            search_cities[i] = city
            i += 1

    else:
        search_cities['Result'] = 'No city satisfying the request: ' + part_name

    return search_cities


def _get_population_from_city_line(city: str) -> float:
    # Возвращает количество жителей города

    return float(city.split('\t')[14])


def _tz_diff(home, away):
    utcnow = timezone('utc').localize(datetime.utcnow())  # generic time
    here = utcnow.astimezone(timezone(home)).replace(tzinfo=None)
    there = utcnow.astimezone(timezone(away)).replace(tzinfo=None)

    offset = relativedelta(here, there)
    return offset.hours


def _file_open():
     return open('data/RU.txt', 'r')
