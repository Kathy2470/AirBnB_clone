from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from Basemodel."""
    city_id = ""
    user_id = ""
    name = ""
    descritpion = ""
    number_room = 0
    number_bathrooms = 0
    max_huest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
