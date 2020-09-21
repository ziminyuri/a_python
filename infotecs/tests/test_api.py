from django.test import RequestFactory, TestCase

from infotecs.views import cities, city_by_id, info_of_two_cities


class CityApiTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_city_by_id(self):
        request = self.factory.get('api/v1/cities')
        response = city_by_id(request, 451773)
        self.assertEqual(response.status_code, 200)

    def test_city_by_wrong_id(self):
        request = self.factory.get('api/v1/cities')
        response = city_by_id(request, 451)
        self.assertEqual(response.status_code, 200)

    def test_cities_with_page_count(self):
        request = self.factory.get('api/v1/cities/?page=2&count=3')
        response = cities(request)
        self.assertEqual(response.status_code, 200)

    def test_cities_with__wrong_page_count(self):
        request = self.factory.get('api/v1/cities/?page=200000&count=3')
        response = cities(request)
        self.assertEqual(response.status_code, 406)

    def test_cities_by_part_name(self):
        request = self.factory.get('api/v1/cities/?filter=Таз')
        response = cities(request)
        self.assertEqual(response.status_code, 200)

    def test_info_of_two_cities(self):
        request = self.factory.get('api/v1/cities/')
        response = info_of_two_cities(request, 'Тимошкино', 'Патраково')
        self.assertEqual(response.status_code, 200)

    def test_info_of_two_cities_is_north(self):
        request = self.factory.get('api/v1/cities/?param=is_north')
        response = info_of_two_cities(request, 'Тимошкино', 'Патраково')
        self.assertEqual(response.status_code, 200)

    def test_info_of_two_cities_is_same_time_zone(self):
        request = self.factory.get('api/v1/cities/?param=is_same_time_zone')
        response = info_of_two_cities(request, 'Тимошкино', 'Патраково')
        self.assertEqual(response.status_code, 200)


