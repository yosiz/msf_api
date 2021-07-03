from ..base import MsfBaseApi
from pydantic import BaseModel, create_model
from .classes import Character


class MsfCharApi(MsfBaseApi):
    def __init__(self, api_key, cache_expiration=None, logger=None, proxy=None):
        super().__init__(api_key, "CharacterApi", cache_expiration or 43200, logger, proxy)

    def get_characters(self, filter=None):
        chars = self._get("characters")
        if filter is not None:
            pass
            # TODO apply filter
            # chars = [chars]
        return chars

    def get_character_info(self, id, props=None):
        char_info = self._get(f"characters/{id}")
        # model_attrs = {k:(type(char_info['data'][k]),...)  for k in char_info['data'].keys()}
        # CharModel = create_model("Character",char_info['data'].keys())
        # print(model_attrs)
        # return char_info
        if 'data' in char_info:
            return Character.parse_obj(char_info['data'])
        else:
            raise Exception("error retrieving character info for {}. error:{}".format(id, char_info))
