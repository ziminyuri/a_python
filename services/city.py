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

            time_zone_difference = tz_diff(timezone_1, timezone_2)
            return{"Time zones the same": "False", 'Time zone difference': time_zone_difference}

    elif city_1:
        return {"Error": "There is no city №2"}

    elif city_2:
        return {"Error": "There is no city №1"}

    else:
        return {"Error": "There is no cities with such names"}


def _get_population_from_city_line(city: str) -> float:
    # Возвращает количество жителей города

    return float(city.split('\t')[14])


def tz_diff(home, away):
    utcnow = timezone('utc').localize(datetime.utcnow())  # generic time
    here = utcnow.astimezone(timezone(home)).replace(tzinfo=None)
    there = utcnow.astimezone(timezone(away)).replace(tzinfo=None)

    offset = relativedelta(here, there)
    return offset.hours
