from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _find_area(self, item: TreeNode, area_id: str):
        if item.id == area_id:
            return [item]
        for node in item.areas:
            tree = self._find_area(node, area_id)
            if tree:
                return [item, *tree]

    def _apply_geocoding(self, area_id: str) -> str:
        """
            TODO:
            - Сделать перебор дерева для каждого area_id
            - В ходе перебора возвращать массив элементов, состоящих из TreeNode необходимой ветки
            - Из массива TreeNode составить полный адрес
        """

        for item in self.__data:
            tree = self._find_area(item, area_id)
            if tree:
                return ', '.join([i.name for i in tree])
