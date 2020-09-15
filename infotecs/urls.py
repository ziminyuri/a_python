from django.urls import path
from infotecs import views


urlpatterns = [
    path('api/v1/cities/<int:geonameid>', views.city_by_id),
    path('api/v1/cities/', views.cities),
    path('api/v1/cities/<str:city_1>&<str:city_2>', views.info_of_two_cities)
]
