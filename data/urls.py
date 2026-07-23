class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    
    # Ручки для курьера
    COURIER_CREATE = '/api/v1/courier'
    COURIER_LOGIN = '/api/v1/courier/login'
    COURIER_DELETE = '/api/v1/courier/'
    
    # Ручки для заказов
    ORDERS_CREATE = '/api/v1/orders'
    ORDERS_LIST = '/api/v1/orders'
    ORDERS_CANCEL = '/api/v1/orders/cancel'
    ORDERS_ACCEPT = '/api/v1/orders/accept/'
    ORDERS_TRACK = '/api/v1/orders/track'