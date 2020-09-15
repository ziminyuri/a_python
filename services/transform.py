def get_dict_from_city_str(city_line: str) -> dict:
    # Возвращает словарь: ключами являются свойства города
    city_list: list = city_line.split('\t')

    return {'geonameid': city_list[0], 'name': city_list[1], 'asciiname': city_list[2],
                       'alternatenames': city_list[3], 'latitude': city_list[4], 'longitude ': city_list[5],
                       'feature class': city_list[6], 'feature code': city_list[7], 'country code': city_list[8],
                       'cc2': city_list[9], 'admin1 code': city_list[10], 'admin2 code': city_list[11],
                       'admin3 code': city_list[12], 'admin4 code': city_list[13], 'population': city_list[14],
                       'elevation': city_list[15], 'dem': city_list[16], 'timezone': city_list[17],
                       'modification date': city_list[18].split('\n')[0]}


def get_dict_from_2_cities_str(request_name_city_1: str, request_name_city_2: str,
                               city_1: str = None, city_2: str = None) -> dict:
    # Возвращает словарь, состоящий из данных о двух городах. Если данных не найдено, то возвращается ошибка об
    # отсутствии информации о нужном городе

    response_data: dict = {}

    if city_1:
        response_data1: dict = get_dict_from_city_str(city_1)
        response_data['1'] = response_data1
    else:
        response_data['1'] = 'Error. There is no information about ' + request_name_city_1

    if city_2:
        response_data2: dict = get_dict_from_city_str(city_2)
        response_data['2'] = response_data2

    else:
        response_data['2'] = 'Error. There is no information about ' + request_name_city_2

    return response_data
