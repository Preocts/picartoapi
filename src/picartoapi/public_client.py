"""
Public API methods for Picarto.tv 1.2.6

https://api.picarto.tv/
"""
from __future__ import annotations

import logging

from http_overeasy.http_client import HTTPClient
from picartoapi.model.category import Category
from picartoapi.model.channel import Channel
from picartoapi.model.channel_stub import ChannelStub
from picartoapi.model.online import Online
from picartoapi.model.video import Video


class PublicClient:
    """Public API methods for Picarto.tv 1.2.6"""

    log = logging.getLogger(__name__)
    base_url = "https://api.picarto.tv/api/v1"

    def __init__(self) -> None:
        headers = {"content-type": "application/json", "accepts": "application/json"}
        self.http = HTTPClient(headers=headers)

    def categories(self) -> list[Category]:
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

    def online(
        self,
        *,
        adult: bool = False,
        gaming: bool = False,
        category: list[str] | None = None,
    ) -> list[Online]:
        """
        Get all currently online channels.

        Args:
            adult: Whether or not to include adult channels (default False)
            gaming: Whether or not to include gaming channels (default False)
            category: List of categories to limit this search to (default None)

        Returns
            List of Online objects, can be empty.
        """
        self.log.debug("Fetching online channels.")
        results: list[Online] = []
        fields = {
            "adult": adult,
            "gaming": gaming,
            "category": ",".join(category) if category else "",
        }

        resp = self.http.get(f"{self.base_url}/online", fields)

        if resp.has_success() and resp.get_json():
            results = [Online.build_from(chan) for chan in resp.get_json()]
        else:
            self.log.error("Request error %s: %s", resp.get_status(), resp.get_body())

        self.log.debug("Discovered %d channels.", len(results))

        return results

    def channel(self, channel: str | int) -> Channel | None:
        """
        Get a specific channel by numeric ID or by channel (member) name.

        Args:
            channel: Numeric channel ID or full name of channel (member name)

        Returns:
            Channel object if found, otherwise `None`
        """
        self.log.debug("Looking for '%s' channel.", channel)

        subroute = "id" if isinstance(channel, int) else "name"

        resp = self.http.get(f"{self.base_url}/channel/{subroute}/{channel}")

        if not resp.has_success() or not resp.get_json():
            self.log.error("Request error %s: %s", resp.get_status(), resp.get_body())
            return None

        self.log.debug("Discovered channel.")

        return Channel.build_from(resp.get_json())

    def videos(self, channel: str | int) -> list[Video]:
        """
        Get all videos for a channel by numeric ID or by channel (member) name.

        Args:
            channel: Numeric channel ID or full name of channel (member name)

        Returns:
            List of Video objects, can be empty.
        """
        self.log.debug("Looking for videos of '%s' channel.", channel)

        results: list[Video] = []
        subroute = "id" if isinstance(channel, int) else "name"

        resp = self.http.get(f"{self.base_url}/channel/{subroute}/{channel}/videos")

        if resp.has_success() and resp.get_json():
            results = [Video.build_from(video) for video in resp.get_json()]
        else:
            self.log.error("Request error %s: %s", resp.get_status(), resp.get_body())

        self.log.debug("Discovered %d catagories.", len(results))

        return results

    def search_channels(
        self,
        query: str,
        *,
        adult: bool = False,
        page: int = 1,
        commissions: bool = False,
    ) -> list[ChannelStub]:
        """
        Get all channels matching the given search criteria (by name and tags)

        Args:
            query: The search query to use (does not support special qualifiers)
            adult: Whether or not to include adult channels
            page: The page to display
            commissions: Whether or not to filter by streams offering commissions

        Returns:
            List of ChannelStub objects, can be empty.
        """
        self.log.debug("Searching for matches of `%s`", query)

        results: list[ChannelStub] = []
        fields = {"adult": adult, "page": page, "commissions": commissions}

        resp = self.http.get(f"{self.base_url}/search/channels", fields=fields)

        if resp.has_success() and resp.get_json():
            results = [ChannelStub.build_from(stub) for stub in resp.get_json()]
        else:
            self.log.error("Request error %s: %s", resp.get_status(), resp.get_body())

        self.log.debug("Discovered %d channels.", len(results))

        return results
