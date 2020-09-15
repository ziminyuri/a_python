from services.city import get_city_line_by_id, get_city_by_ru_name, get_northern_city
from services.transform import get_dict_from_city_str, get_dict_from_2_cities_str
from django.http import JsonResponse


def get_city_by_id(request, geonameid: int):
    if request.method == 'GET':
        # Метод возвращает информацию о городе по geonameid

        city_line: str = get_city_line_by_id(geonameid)
        if not city_line:
            return JsonResponse({"Error": "There is no city with such geonameid"})

        else:
            response_data = get_dict_from_city_str(city_line)
            return JsonResponse(response_data)


def get_info_of_two_cities(request, city_1: str, city_2: str):
    if request.method == 'GET':

        en_city_1 = get_city_by_ru_name(city_1)
        en_city_2 = get_city_by_ru_name(city_2)

        if request.GET.get("param") == 'is_north':
            # Возвращает город, который севернее из двух городов или ошибку
            response_data: dict = get_northern_city(en_city_1, en_city_2)

        else:
            # Метод возвращает информацию о двух городах
            response_data = get_dict_from_2_cities_str(city_1, city_2, en_city_1, en_city_2)

        return JsonResponse(response_data)




def get_info_of_two_cities_is_same_time_zone(request, city_1: str, city_2: str):
    if request.method == 'GET':
        # Метод возвращает одинаковая ли временая зона у двух городов
        pass
