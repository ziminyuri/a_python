from services.city import get_city_line_by_id, get_city_by_ru_name, get_northern_city, is_same_time_zone, get_cities
from services.transform import get_dict_from_city_str, get_dict_from_2_cities_str
from services.file import count_number_of_lines_in_file
from django.http import JsonResponse


def city_by_id(request, geonameid: int):
    if request.method == 'GET':
        # Метод возвращает информацию о городе по geonameid

        city_line: str = get_city_line_by_id(geonameid)
        if not city_line:
            return JsonResponse({"Error": "There is no city with such geonameid"})

        else:
            response_data = get_dict_from_city_str(city_line)
            return JsonResponse(response_data)


def cities(request):
    if request.method == 'GET':
        # Возвращает json с городами с учетом пагинации

        lines: int = count_number_of_lines_in_file()

        try:
            page: int = int(request.GET.get("page"))
        except:
            page: int = 1

        try:
            count: int = int(request.GET.get("count"))
        except:
            count: int = 10

        response_data: dict = {}
        if page != 1:
            previous_page: int = page - 1
            response_data['previous'] = request.get_host() + request.path + '?page=' + str(previous_page) + '&count=' \
                                        + str(count)

        if page * count < lines:
            response_data['next'] = request.get_host() + request.path + '?page=' + str(page + 1) + '&count=' \
                                    + str(count)

        response_data['results'] = get_cities(page, count)
        return JsonResponse(response_data)


def info_of_two_cities(request, city_1: str, city_2: str):
    if request.method == 'GET':

        en_city_1 = get_city_by_ru_name(city_1)
        en_city_2 = get_city_by_ru_name(city_2)

        if request.GET.get("param") == 'is_north':
            # Возвращает город, который севернее из двух городов или ошибку
            response_data: dict = get_northern_city(en_city_1, en_city_2)

        elif request.GET.get("param") == 'is_same_time_zone':
            # Возвращает True если одинаковая временая зона, False в обратном случае или ошибку
            response_data: dict = is_same_time_zone(en_city_1, en_city_2)

        else:
            # Метод возвращает информацию о двух городах
            response_data = get_dict_from_2_cities_str(city_1, city_2, en_city_1, en_city_2)

        return JsonResponse(response_data)
