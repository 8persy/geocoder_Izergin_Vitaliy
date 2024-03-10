from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.__dict_data = {}
        self._add_to_dict(self.__data)

    def _add_to_dict(self, tree_areas: list[TreeNode], parent_str: str = ''):
        for item in tree_areas:
            address = f'{parent_str}, {item.name}' if parent_str else item.name
            self.__dict_data[item.id] = address
            self._add_to_dict(item.areas, address)

    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Возвращать данные из словаря с адресами
        """
        return self.__dict_data.get(str(area_id))
