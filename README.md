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
Параметры:
* `page` – номер страницы
* `count` – количество результатов на страницу
* `filter` – поиск городов по части названия

> Внимание! Нельзя использовать параметр filter с другими параметрами.

### Пример запроса
`GET api/v1/cities/?page=2&count=3`

### Ответ
```json

{
    "previous": "127.0.0.1:8000/api/v1/cities/?page=1&count=3",
    "next": "127.0.0.1:8000/api/v1/cities/?page=3&count=3",
    "results": [
        {
            "geonameid": "451750",
            "name": "Zhitovo",
            "asciiname": "Zhitovo",
            "alternatenames": "",
            "latitude": "57.29693",
            "longitude ": "34.41848",
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
            "dem": "247",
            "timezone": "Europe/Moscow",
            "modification date": "2011-07-09"
        },
        {
            "geonameid": "451751",
            "name": "Zhitnikovo",
            "asciiname": "Zhitnikovo",
            "alternatenames": "",
            "latitude": "57.20064",
            "longitude ": "34.57831",
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
            "dem": "198",
            "timezone": "Europe/Moscow",
            "modification date": "2011-07-09"
        },
        {
            "geonameid": "451752",
            "name": "Zhelezovo",
            "asciiname": "Zhelezovo",
            "alternatenames": "",
            "latitude": "57.02591",
            "longitude ": "34.51886",
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
            "dem": "192",
            "timezone": "Europe/Moscow",
            "modification date": "2011-07-09"
        }
    ]
}
```
### Пример запроса
`GET api/v1/cities/?page=2&count=3`

```json
{
    "1": "Urochishche Tazhgul",
    "2": "Tazovo",
    "3": "Tazneyevo",
    "4": "Tazlud",
    "5": "Stantsiya Tazlarovo",
    "6": "Tazlarovo",
    "7": "Tazino",
    "8": "Tazen-Kala",
    "9": "Tazbichi",
    "10": "Taz",
    "11": "Taz Russkiy",
    "12": "Tazeyevo",
    "13": "Zimnik Tazhedenovskiy",
    "14": "Tazovo",
    "15": "Tazhbay",
    "16": "Letovka Tazeli",
    "17": "Balka Tazi",
    "18": "Tazakol",
    "19": "Tazirkent",
    "20": "Tazovskiy Rayon",
    "21": "Tazovskiy Poluostrov",
    "22": "Tazovsky",
    "23": "Tazovskaya Guba",
    "24": "Taz’min",
    "25": "Tazik",
    "26": "Taza",
    "27": "Taz",
    "28": "Taz",
    "29": "Urochishche Malyy Taz",
    "30": "Bol’shoy Taz",
    "31": "Urochishche Bol’shoy Taz",
    "32": "Ozero Bol’shoy Tazol’",
    "33": "Tazyrachevo",
    "34": "Poperechnyy Tazik",
    "35": "Prodol’nyy Tazik",
    "36": "Tazovo",
    "37": "Gora Tazagon",
    "38": "Gora Tazovskaya",
    "39": "Taza",
    "40": "Bukhta Malyy Tazgou",
    "41": "Bol'shoy Tazgou",
    "42": "Ozero Malyy Tazol’",
    "43": "Ozero Tazol’",
    "44": "Tazovka",
    "45": "Taza",
    "46": "Tazovka",
    "47": "Gora Bol’shoy Taz",
    "48": "Lesouchastok Chërnyy Taz",
    "49": "Chërnyy Taz",
    "50": "Tubyak-Tazlarovo",
    "51": "Taza-Chishma",
    "52": "Tazlovka",
    "53": "Tazyrbak",
    "54": "Urochishche Tazovskoye Boloto",
    "55": "Vostochnyy Tazmer",
    "56": "Zapadnyy Tazmer",
    "57": "Tazeya",
    "58": "Tazeya Pervaya",
    "59": "Tazeya Vtoraya",
    "60": "Malyy Taz",
    "61": "Tazlarovo",
    "62": "Tazhi Pervyye",
    "63": "Tazhi Vtoryye",
    "64": "Tazovskoye",
    "65": "Tazovskiy Northwest Airport",
    "66": "Liman Tazyna"
}
```

## Метод принимает названия двух городов (на русском языке) и получает информацию о найденных городах 
Параметр `?param=`:
* `is_north` – возвращает город, расположенный севернее
* `is_same_time_zone` – возвращает True, если у городов одинаковые временные зоны. Если разные временые зоны, то возвращает False и разницу между ними

### Пример запроса
`GET api/v1/cities/Тимошкино&Патраково`
### Ответ
```json
{
    "1": {
        "geonameid": "451811",
        "name": "Timoshkino",
        "asciiname": "Timoshkino",
        "alternatenames": "",
        "latitude": "57.19533",
        "longitude ": "34.87121",
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
        "dem": "176",
        "timezone": "Europe/Moscow",
        "modification date": "2011-07-09"
    },
    "2": {
        "geonameid": "451907",
        "name": "Patrakovo",
        "asciiname": "Patrakovo",
        "alternatenames": "Patrakovo,Патраково",
        "latitude": "56.75165",
        "longitude ": "34.69534",
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
        "dem": "202",
        "timezone": "Europe/Moscow",
        "modification date": "2012-01-16"
    }
}
```


### Пример запроса
`GET api/v1/cities/Тимошкино&Патраково?param=is_north`

### Ответ
```json
{
    "geonameid": "451811",
    "name": "Timoshkino",
    "asciiname": "Timoshkino",
    "alternatenames": "",
    "latitude": "57.19533",
    "longitude ": "34.87121",
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
    "dem": "176",
    "timezone": "Europe/Moscow",
    "modification date": "2011-07-09"
}
```

### Пример запроса
`GET api/v1/cities/Тимошкино&Таз?param=is_same_time_zone`

### Ответ
```json

{
    "Time zones the same": "False",
    "Time zone difference": -2
}
```