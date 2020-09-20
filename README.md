# Test task for Infortex

Реализовать HTTP-сервер для предоставления информации по географическим объектам.
Данные взять из географической базы данных GeoNames, по ссылке:

## Метод принимает идентификатор geonameid и возвращает информацию о городе

`GET api/v1/cities/geonameid` вернёт информацию о городе

### Пример запроса
`GET api/v1/cities/451773`

### Ответ

Успешный ответ приходит с кодом `200 OK` и содержит тело:

```json
{
    "geonameid": "451773",
    "name": "Yakshino",
    "asciiname": "Yakshino",
    "alternatenames": "",
    "latitude": "57.08518",
    "longitude ": "34.60433",
    "feature class": "P",
    "feature code": "PPL",
    "country code": "RU",
    "cc2": "",
    "admin1 code": "77",
    "admin2 code": "",
    "admin3 code": "",
    "admin4 code": "",
    "population": "0",
    "elevation": "",
    "dem": "188",
    "timezone": "Europe/Moscow",
    "modification date": "2011-07-09"
}
```

## Метод принимает страницу и количество отображаемых на странице городов и возвращает список городов с их информацией
`GET api/v1/cities` возвращает список городов с их информацией


## Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах 
