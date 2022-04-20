"""
Public API methods for Picarto.tv 1.2.6

https://api.picarto.tv/
"""
from __future__ import annotations

import logging

from http_overeasy.http_client import HTTPClient
from picartoapi.model.category import Category


class PublicClient:
    """Public API methods for Picarto.tv 1.2.6"""

    log = logging.getLogger(__name__)
    base_url = "https://api.picarto.tv/api/v1"

    def __init__(self) -> None:
        headers = {"content-type": "application/json", "accepts": "application/json"}
        self.http = HTTPClient(headers=headers)

    def catagories(self) -> list[Category]:
        """
        Get information about all categories. Can return an empty list.

        Returns:
            List of Catagory objects
        """
        self.log.debug("Fetching catagories.")
        results: list[Category] = []
        resp = self.http.get(f"{self.base_url}/categories")

        if resp.has_success() and resp.get_json():
            results = [Category.build_from(cat) for cat in resp.get_json()]
        else:
            self.log.error("Request error %s: %s", resp.get_status(), resp.get_body())

        self.log.debug("Discovered %d catagories.", len(results))

        return results
