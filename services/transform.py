def get_dict_from_city_str(city_line: str) -> dict:
    # Возвращает словарь: ключами являются свойства города
    city_list: list = city_line.split('\t')

    city_dict: dict = {}
    city_dict['geonameid'] = city_list[0]
    city_dict['name'] = city_list[1]
    city_dict['asciiname'] = city_list[2]
    city_dict['alternatenames'] = city_list[3]
    city_dict['latitude'] = city_list[4]
    city_dict['longitude '] = city_list[5]
    city_dict['feature class'] = city_list[6]
    city_dict['feature code'] = city_list[7]
    city_dict['country code'] = city_list[8]
    city_dict['cc2'] = city_list[9]
    city_dict['admin1 code'] = city_list[10]
    city_dict['admin2 code'] = city_list[11]
    city_dict['admin3 code'] = city_list[12]
    city_dict['admin4 code'] = city_list[13]
    city_dict['population'] = city_list[14]
    city_dict['elevation'] =city_list[15]
    city_dict['dem'] = city_list[16]
    city_dict['timezone'] = city_list[17]
    city_dict['modification date'] = city_list[18].split('\n')[0]

    return city_dict

