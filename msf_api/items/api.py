from ..base import MsfBaseApi
from pydantic import BaseModel, create_model
from .classes import Item
from typing import List


class MsfItemsApi(MsfBaseApi):
    def __init__(self, api_key, cache_expiration=None, logger=None, proxy=None):
        super().__init__(api_key, "ItemsApi", cache_expiration or 86400, logger, proxy)

    def get_item(self, item_id):
        item = self._get("items/{}?pieceDirectCost=full".format(item_id))
        return Item.parse_obj(item['data'])

    def get_total_material_cost(self, item_id) -> dict:
        mats = {}
        for mat in self.get_item_materials(item_id):
            if mat.id in mats:
                mats[mat.id].quantity = mats[mat.id].quantity + mat.quantity
            else:
                mats[mat.id] = mat
        return mats

    def get_item_materials(self, item_id) -> List[Item]:
        item = self.get_item(item_id)
        parts = []
        for item_part in self._get_parts(item):
            parts.append(item_part)
        return parts

    def _get_parts(self, item: Item):
        if item.has_parts():
            parts = [self._get_parts(x) for x in item.get_parts(calc_quantity=True)]
            # flattern list
            return [i for parts_list in parts for i in parts_list]
        else:
            return [item]
