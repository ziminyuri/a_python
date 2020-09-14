from services.city import get_city_line_by_id, get_city_by_ru_name
from services.transform import get_dict_from_city_str
from django.http import JsonResponse


def get_city_by_id(request, geonameid: int):
    if request.method == 'GET':
        # Метод возвращает информацию о городе по geonameid

        city_line: str = get_city_line_by_id(geonameid)
        if not city_line:
            return JsonResponse({"error": "There is no city with such geonameid"})

        else:
            response_data = get_dict_from_city_str(city_line)
            return JsonResponse(response_data)


def get_info_of_two_cities(request, city_1: str, city_2: str):
    if request.method == 'GET':
        # Метод возвращает информацию о двух городах

        en_city_1 = get_city_by_ru_name(city_1)
        en_city_2 = get_city_by_ru_name(city_2)

        if en_city_1:
            response_data1 = get_dict_from_city_str(en_city_1)

            if en_city_2:
                response_data2 = get_dict_from_city_str(en_city_2)

                response_data = {response_data1, response_data2}
                return JsonResponse(response_data)


def get_info_of_two_cities_is_north(request, city_1: str, city_2: str):
    if request.method == 'GET':
        # Метод возвращает город, который севернее из двух городов
        pass


def get_info_of_two_cities_is_same_time_zone(request, city_1: str, city_2: str):
    if request.method == 'GET':
        # Метод возвращает одинаковая ли временая зона у двух городов
        pass
