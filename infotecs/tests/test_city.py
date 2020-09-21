from django.test import TestCase

from services.city import (get_cities, get_city_by_ru_name,
                           get_city_line_by_id, get_northern_city,
                           is_same_time_zone, search_cities_by_part_name)


class CityTestCase(TestCase):
    def test_get_city_by_wrong_id(self):
        result = get_city_line_by_id(123)
        self.assertEqual(False, result)

    def test_get_city_by_id(self):
        result = get_city_line_by_id(451773)
        test_result = '451773\tYakshino\tYakshino\t\t57.08518\t34.60433\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t188\t' \
                      'Europe/Moscow\t2011-07-09\n'
        self.assertEqual(test_result, result)

    def test_get_cities(self):
        result = get_cities(2, 3)

        test_result: list = []

        city_1: dict = {'geonameid': '451750', 'name': 'Zhitovo', 'asciiname': 'Zhitovo',
                        'alternatenames': '', 'latitude': '57.29693', 'longitude ': '34.41848',
                        'feature class': 'P', 'feature code': 'PPL', 'country code': 'RU',
                        'cc2': '', 'admin1 code': '77', 'admin2 code': '',
                        'admin3 code': '', 'admin4 code': '', 'population': '0',
                        'elevation': '', 'dem': '247', 'timezone': 'Europe/Moscow',
                        'modification date': '2011-07-09'}

        city_2: dict = {'geonameid': '451751', 'name': 'Zhitnikovo', 'asciiname': 'Zhitnikovo',
                        'alternatenames': '', 'latitude': '57.20064', 'longitude ': '34.57831',
                        'feature class': 'P', 'feature code': 'PPL', 'country code': 'RU',
                        'cc2': '', 'admin1 code': '77', 'admin2 code': '',
                        'admin3 code': '', 'admin4 code': '', 'population': '0',
                        'elevation': '', 'dem': '198', 'timezone': 'Europe/Moscow',
                        'modification date': '2011-07-09'}

        city_3: dict = {'geonameid': '451752', 'name': 'Zhelezovo', 'asciiname': 'Zhelezovo',
                        'alternatenames': '', 'latitude': '57.02591', 'longitude ': '34.51886',
                        'feature class': 'P', 'feature code': 'PPL', 'country code': 'RU',
                        'cc2': '', 'admin1 code': '77', 'admin2 code': '',
                        'admin3 code': '', 'admin4 code': '', 'population': '0',
                        'elevation': '', 'dem': '192', 'timezone': 'Europe/Moscow',
                        'modification date': '2011-07-09'}

        test_result.append(city_1)
        test_result.append(city_2)
        test_result.append(city_3)

        self.assertEqual(test_result, result)

    def test_get_city_by_ru_name(self):
        result = get_city_by_ru_name('Тимошкино')
        test_result: str = '451811\tTimoshkino\tTimoshkino\t\t57.19533\t34.87121\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t176\t' \
                           'Europe/Moscow\t2011-07-09\n'
        self.assertEqual(test_result, result)

    def test_get_city_by_wrong_ru_name(self):
        result = get_city_by_ru_name('Тимошкинос')
        self.assertEqual(False, result)

    def test_get_northern_city_no_city_2(self):
        city_1 = '451811\tTimoshkino\tTimoshkino\t\t57.19533\t34.87121\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t176\t' \
                 'Europe/Moscow\t2011-07-09\n'
        result = get_northern_city(city_1, False)
        test_result: dict = {"Error": "There is no city №2"}
        self.assertEqual(test_result, result)

    def test_get_northern_city_no_city_1(self):
        city_2 = '451811\tTimoshkino\tTimoshkino\t\t57.19533\t34.87121\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t176\t' \
                 'Europe/Moscow\t2011-07-09\n'
        result = get_northern_city(False, city_2)
        test_result: dict = {"Error": "There is no city №1"}
        self.assertEqual(test_result, result)

    def test_get_northern_city_no_city_1_and_city_2(self):
        result = get_northern_city(False, False)
        test_result: dict = {"Error": "There is no cities with such names"}
        self.assertEqual(test_result, result)

    def test_get_northern_city(self):
        city_1 = '451811\tTimoshkino\tTimoshkino\t\t57.19533\t34.87121\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t176\t' \
                 'Europe/Moscow\t2011-07-09\n'
        city_2 = '451907\tPatrakovo\tPatrakovo\tPatrakovo,Патраково\t56.75165\t34.69534\tP\tPPL\tRU\t\t77' \
                 '\t\t\t\t0\t\t202\tEurope/Moscow\t2012-01-16\n'

        result = get_northern_city(city_1, city_2)
        test_result: dict = {"geonameid": "451811", "name": "Timoshkino", "asciiname": "Timoshkino",
                             "alternatenames": "", "latitude": "57.19533", "longitude ": "34.87121",
                             "feature class": "P", "feature code": "PPL", "country code": "RU", "cc2": "",
                             "admin1 code": "77", "admin2 code": "", "admin3 code": "", "admin4 code": "",
                             "population": "0", "elevation": "", "dem": "176", "timezone": "Europe/Moscow",
                             "modification date": "2011-07-09"}
        self.assertEqual(test_result, result)

    def test_is_same_time_zone_is_true(self):
        city_1 = '451811\tTimoshkino\tTimoshkino\t\t57.19533\t34.87121\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t176\t' \
                 'Europe/Moscow\t2011-07-09\n'
        city_2 = '451907\tPatrakovo\tPatrakovo\tPatrakovo,Патраково\t56.75165\t34.69534\tP\tPPL\tRU\t\t77' \
                 '\t\t\t\t0\t\t202\tEurope/Moscow\t2012-01-16\n'

        result = is_same_time_zone(city_1, city_2)
        test_result: dict = {"Time zones the same": "True"}
        self.assertEqual(test_result, result)

    def test_is_same_time_zone_is_false(self):
        city_1 = '451811\tTimoshkino\tTimoshkino\t\t57.19533\t34.87121\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t176\t' \
                 'Europe/Moscow\t2011-07-09\n'
        city_2 = '483893\tTaz\tTaz\tTaz,Таз\t57.4391\t57.3105\tH\tSTM\tRU\t\t90\t\t\t\t0\t\t122\t' \
                 'Asia/Yekaterinburg\t2012-01-17\n'

        result = is_same_time_zone(city_1, city_2)
        test_result: dict = {"Time zones the same": "False", "Time zone difference": -2}
        self.assertEqual(test_result, result)

    def test_is_same_time_zone_no_city_2(self):
        city_1 = '451811\tTimoshkino\tTimoshkino\t\t57.19533\t34.87121\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t176\t' \
                 'Europe/Moscow\t2011-07-09\n'
        result = is_same_time_zone(city_1, False)
        test_result: dict = {"Error": "There is no city №2"}
        self.assertEqual(test_result, result)

    def test_is_same_time_zone_no_city_1(self):
        city_2 = '451811\tTimoshkino\tTimoshkino\t\t57.19533\t34.87121\tP\tPPL\tRU\t\t77\t\t\t\t0\t\t176\t' \
                 'Europe/Moscow\t2011-07-09\n'
        result = is_same_time_zone(False, city_2)
        test_result: dict = {"Error": "There is no city №1"}
        self.assertEqual(test_result, result)

    def test_is_same_time_zone_no_city_1_and_city_2(self):
        result = is_same_time_zone(False, False)
        test_result: dict = {"Error": "There is no cities with such names"}
        self.assertEqual(test_result, result)

    def test_search_cities_by_part_name(self):
        result = search_cities_by_part_name('Таз')
        test_result: dict = {1: "Urochishche Tazhgul", 2: "Tazovo", 3: "Tazneyevo", 4: "Tazlud",
                             5: "Stantsiya Tazlarovo", 6: "Tazlarovo", 7: "Tazino", 8: "Tazen-Kala",
                             9: "Tazbichi", 10: "Taz", 11: "Taz Russkiy", 12: "Tazeyevo",
                             13: "Zimnik Tazhedenovskiy", 14: "Tazovo", 15: "Tazhbay", 16: "Letovka Tazeli",
                             17: "Balka Tazi", 18: "Tazakol", 19: "Tazirkent", 20: "Tazovskiy Rayon",
                             21: "Tazovskiy Poluostrov", 22: "Tazovsky", 23: "Tazovskaya Guba", 24: "Taz’min",
                             25: "Tazik", 26: "Taza", 27: "Taz", 28: "Taz", 29: "Urochishche Malyy Taz",
                             30: "Bol’shoy Taz", 31: "Urochishche Bol’shoy Taz", 32: "Ozero Bol’shoy Tazol’",
                             33: "Tazyrachevo", 34: "Poperechnyy Tazik", 35: "Prodol’nyy Tazik", 36: "Tazovo",
                             37: "Gora Tazagon", 38: "Gora Tazovskaya", 39: "Taza", 40: "Bukhta Malyy Tazgou",
                             41: "Bol'shoy Tazgou", 42: "Ozero Malyy Tazol’", 43: "Ozero Tazol’", 44: "Tazovka",
                             45: "Taza", 46: "Tazovka", 47: "Gora Bol’shoy Taz", 48: "Lesouchastok Chërnyy Taz",
                             49: "Chërnyy Taz", 50: "Tubyak-Tazlarovo", 51: "Taza-Chishma", 52: "Tazlovka",
                             53: "Tazyrbak", 54: "Urochishche Tazovskoye Boloto", 55: "Vostochnyy Tazmer",
                             56: "Zapadnyy Tazmer", 57: "Tazeya", 58: "Tazeya Pervaya", 59: "Tazeya Vtoraya",
                             60: "Malyy Taz", 61: "Tazlarovo", 62: "Tazhi Pervyye", 63: "Tazhi Vtoryye",
                             64: "Tazovskoye", 65: "Tazovskiy Northwest Airport", 66: "Liman Tazyna"}

        self.assertEqual(test_result, result)

    def test_search_cities_by_wrong_part_name(self):
        result = search_cities_by_part_name('Тазваыв')
        test_result: dict = {'Result': 'No city satisfying the request: Тазваыв'}
        self.assertEqual(test_result, result)
