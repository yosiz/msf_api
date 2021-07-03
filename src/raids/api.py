from .classes import Raid, Room
from ..base import MsfBaseApi


class MsfRaidApi(MsfBaseApi):
    def __init__(self, api_key, cache_expiration=None, logger=None, proxy=None):
        super().__init__(api_key, "RaidsApi", cache_expiration or 86400, logger, proxy)

    def get_characters(self, filter=None):
        chars = self._get("characters")
        if filter is not None:
            pass
            # TODO apply filter
            # chars = [chars]
        return chars
