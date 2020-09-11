from django.urls import path
from infotecs import views


urlpatterns = [
    path('api/v1/cities/<int:geonameid>', views.get_city_by_id),
]
