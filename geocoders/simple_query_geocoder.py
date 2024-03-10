from geocoders.geocoder import Geocoder
from api import API

api = API()


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Делать запросы к API для каждой area
            - Для каждого ответа формировать полный адрес
        """

        address = API.get_area(area_id).name
        while API.get_area(area_id).parent_id:
            area_id = API.get_area(area_id).parent_id
            address = API.get_area(area_id).name + ', ' + address

        return address
