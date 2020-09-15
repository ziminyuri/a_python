from django.urls import path
from infotecs import views


urlpatterns = [
    path('api/v1/cities/<int:geonameid>', views.get_city_by_id),

    path('api/v1/cities/<str:city_1>&<str:city_2>', views.get_info_of_two_cities),
    path('api/v1/cities/<str:city_1>&<str:city_2>is_same_time_zone', views.get_info_of_two_cities_is_same_time_zone),
]
