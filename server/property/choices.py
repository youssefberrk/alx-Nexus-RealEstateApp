from django.db import models

class Highlight(models.TextChoices):
    HIGH_SPEED_INTERNET = 'HighSpeedInternetAccess', 'High Speed Internet Access'
    WASHER_DRYER = 'WasherDryer', 'Washer/Dryer'
    AIR_CONDITIONING = 'AirConditioning', 'Air Conditioning'
    HEATING = 'Heating', 'Heating'
    SMOKE_FREE = 'SmokeFree', 'Smoke Free'
    CABLE_READY = 'CableReady', 'Cable Ready'
    SATELLITE_TV = 'SatelliteTV', 'Satellite TV'
    DOUBLE_VANITIES = 'DoubleVanities', 'Double Vanities'
    TUB_SHOWER = 'TubShower', 'Tub/Shower'
    INTERCOM = 'Intercom', 'Intercom'
    SPRINKLER_SYSTEM = 'SprinklerSystem', 'Sprinkler System'
    RECENTLY_RENOVATED = 'RecentlyRenovated', 'Recently Renovated'
    CLOSE_TO_TRANSIT = 'CloseToTransit', 'Close to Transit'
    GREAT_VIEW = 'GreatView', 'Great View'
    QUIET_NEIGHBORHOOD = 'QuietNeighborhood', 'Quiet Neighborhood'

class Amenity(models.TextChoices):
    WASHER_DRYER = 'WasherDryer', 'Washer/Dryer'
    AIR_CONDITIONING = 'AirConditioning', 'Air Conditioning'
    DISHWASHER = 'Dishwasher', 'Dishwasher'
    HIGH_SPEED_INTERNET = 'HighSpeedInternet', 'High Speed Internet'
    HARDWOOD_FLOORS = 'HardwoodFloors', 'Hardwood Floors'
    WALK_IN_CLOSETS = 'WalkInClosets', 'Walk-in Closets'
    MICROWAVE = 'Microwave', 'Microwave'
    REFRIGERATOR = 'Refrigerator', 'Refrigerator'
    POOL = 'Pool', 'Pool'
    GYM = 'Gym', 'Gym'
    PARKING = 'Parking', 'Parking'
    PETS_ALLOWED = 'PetsAllowed', 'Pets Allowed'
    WIFI = 'WiFi', 'WiFi'

class PropertyType(models.TextChoices):
    ROOMS = 'Rooms', 'Rooms'
    TINYHOUSE = 'Tinyhouse', 'Tiny House'
    APARTMENT = 'Apartment', 'Apartment'
    VILLA = 'Villa', 'Villa'
    TOWNHOUSE = 'Townhouse', 'Townhouse'
    COTTAGE = 'Cottage', 'Cottage'
