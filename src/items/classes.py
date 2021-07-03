from pydantic import BaseModel
from typing import List, Optional


class Item(BaseModel):
    id: str
    name: str
    icon: Optional[str]
    tier: Optional[int]
    stats: Optional[dict]
    directCost: Optional[List[dict]]
    quantity: Optional[int] = 1

    def has_parts(self):
        return self.directCost is not None

    def get_parts(self, calc_quantity=False):
        if self.directCost is not None:
            quantity_mul = self.quantity if calc_quantity else 1
            return [Item.parse_obj({**x['item'], "quantity": x.get("quantity", 1) * quantity_mul}) for x in
                    self.directCost]
        else:
            return []
