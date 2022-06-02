"""
Public API methods for Picarto.tv 1.2.6

https://api.picarto.tv/
"""
from __future__ import annotations

import logging
from json import JSONDecodeError
from typing import Any

import httpx
from picartoapi.model.category import Category
from picartoapi.model.channel import Channel
from picartoapi.model.channel_stub import ChannelStub
from picartoapi.model.online import Online
from picartoapi.model.search_video import SearchVideo
from picartoapi.model.video import Video

HTTP_TIMEOUT = 10  # Seconds


class PublicClient:
    """Public API methods for Picarto.tv 1.2.6"""

    log = logging.getLogger(__name__)
    base_url = "https://api.picarto.tv/api/v1"

    def __init__(self) -> None:
        headers = {"content-type": "application/json", "accepts": "application/json"}
        self._http = httpx.Client(headers=headers, timeout=httpx.Timeout(HTTP_TIMEOUT))

    def _get(
        self,
        route: str,
        params: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]] | None:
        """Internal: Handle all HTTPS get calls, returns results if successful."""
        if not params:
            params = {}

        resp = self._http.get(f"{self.base_url}/{route}", params=params)

        if resp.status_code not in range(200, 300):
            self.log.error("Request error: %d: %s", resp.status_code, resp.text)

        try:
            results = resp.json()
            return results if isinstance(results, list) else [results]
        except JSONDecodeError:
            return None

    def categories(self) -> list[Category]:
        """
        Get information about all categories. Can return an empty list.

        Returns:
            List of Catagory objects
        """
        self.log.debug("Fetching catagories.")

        resp = self._get(f"{self.base_url}/categories")
        results = [Category.build_from(cat) for cat in resp] if resp else []

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

        params = {
            "adult": adult,
            "gaming": gaming,
            "category": ",".join(category) if category else "",
        }
        resp = self._get(f"{self.base_url}/online", params)
        results = [Online.build_from(chan) for chan in resp] if resp else []

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
        resp = self._get(f"{self.base_url}/channel/{subroute}/{channel}")

        self.log.debug("Discovered %d channel.", int(bool(resp)))

        return Channel.build_from(resp[0]) if resp else None

    def videos(self, channel: str | int) -> list[Video]:
        """
        Get all videos for a channel by numeric ID or by channel (member) name.

        Args:
            channel: Numeric channel ID or full name of channel (member name)

        Returns:
            List of Video objects, can be empty.
        """
        self.log.debug("Looking for videos of '%s' channel.", channel)

        subroute = "id" if isinstance(channel, int) else "name"
        resp = self._get(f"{self.base_url}/channel/{subroute}/{channel}/videos")
        results = [Video.build_from(video) for video in resp] if resp else []

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

        params = {"adult": adult, "page": page, "commissions": commissions}
        resp = self._get(f"{self.base_url}/search/channels", params)
        results = [ChannelStub.build_from(stub) for stub in resp] if resp else []

        self.log.debug("Discovered %d channels.", len(results))

        return results

    def search_videos(
        self,
        query: str,
        *,
        adult: bool = False,
        page: int = 1,
    ) -> list[SearchVideo]:
        """
        Get all videos with channels matching the given search criteria

        Args:
            query: The search query to use (does not support special qualifiers)
            adult: Whether or not to include adult channels
            page: The page to display

        Returns:
            List of ChannelVideo objects, can be empty.
        """
        self.log.debug("Searching for matches of `%s`", query)

        params = {"adult": adult, "page": page}
        resp = self._get(f"{self.base_url}/search/videos", params)
        results = [SearchVideo.build_from(stub) for stub in resp] if resp else []

        self.log.debug("Discovered %d videos.", len(results))

        return results
