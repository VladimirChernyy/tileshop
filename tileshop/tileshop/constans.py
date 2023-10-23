from enum import IntEnum


class CartLimit(IntEnum):
    ADD_QUANTITY = 0
    QUANTITY_INITIAL = 1


class CartValidate(IntEnum):
    QUANTITY_MIN_VALUE = 1
    QUANTITY_MAX_VALUE = 10


class OrderLimit(IntEnum):
    MAX_LEN_FIRST_NAME = 50
    MAX_LEN_LAST_NAME = 50
    MAX_LEN_ADDRESS = 250
    MAX_LEN_CITY = 180


class OrderItemLimit(IntEnum):
    MAX_DIGITS_PRICE = 10
    DECIMAL_PLACES_PRICE = 2
    DEFAULT_QUANTITY = 1


class CategoryLimit(IntEnum):
    MAX_LEN_TITLE = 100


class SubCategoryLimit(IntEnum):
    MAX_LEN_TITLE = 100


class ProductLimit(IntEnum):
    MAX_LEN_NAME = 155
    MAX_DIG_PRICE = 10
    DECIMAL_PLACES = 2
    DEFAULT_STOCK = 1
