# MONGODB
MONGODB_CONNECTION_STRING = "mongodb://127.0.0.1:27001/"
MONGODB_DB_NAME = "geo"
# GEO OBJECTS VIEWS
DYNAMIC = 'dynamic'
STATIC = 'static'
# GEO OBJECTS TYPES
POINT_OBJECT = "point"
LINE_STRING_OBJECT = "line_string"
POLYGON_OBJECT = "polygon"
DEFAULT_OBJECT_TYPE = POINT_OBJECT
# BUSINESS LOGIC
MONGODB_DB_COLLECTIONS = dict(
    static={
        "geo_wikimapia_polygons": {
            "area": POLYGON_OBJECT,
        },
        "meteorites": {
            "location": POINT_OBJECT,
        },
    },
    dynamic={
        "geo_yandex_taxi": {
            "last_point": POINT_OBJECT,
            "path": LINE_STRING_OBJECT,
        },
        # "geo_city_mobil": {
        #     "location": POINT_OBJECT,
        # },
    },
)
CONTAINS_DYNAMIC_DATA = True if len(MONGODB_DB_COLLECTIONS.get(DYNAMIC, '')) else False
# Сыктывкар Аэропорт
# LAT = 61.663917
# LON = 50.850578
# Район СПб
LAT = 59.97
LON = 30.33
