from services.city import get_city_line_by_id
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




