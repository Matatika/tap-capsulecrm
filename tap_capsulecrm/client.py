"""REST client handling, including CapsulecrmStream base class."""

import re
from typing import Any, Dict, Optional

import requests
from pendulum import parse
from singer_sdk.streams import RESTStream
from datetime import datetime, timedelta
from tap_capsulecrm.auth import CapsulecrmAuthenticator


class CapsulecrmStream(RESTStream):
    """Capsulecrm stream class."""

    url_base = "https://api.capsulecrm.com/api/v2"

    records_jsonpath = "$[*]"

    @property
    def authenticator(self) -> CapsulecrmAuthenticator:
        """Return a new authenticator object."""
        return CapsulecrmAuthenticator(
            self, self._tap.config, "https://api.capsulecrm.com/oauth/token"
        )

    @property
    def http_headers(self) -> dict:
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if response.headers.get("X-Pagination-Has-More") != "false":
            next_page_token = response.headers.get("Link", None)
            result = re.search("page=(.*)&", next_page_token)
            next_page_token = result.group(1)

        else:
            next_page_token = None

        return next_page_token

    def get_starting_time(self, context):
        start_date = self.config.get("start_date")
        if start_date:
            start_date = parse(self.config.get("start_date"))
        rep_key = self.get_starting_timestamp(context)
        return rep_key or start_date

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        params["perPage"] = 100
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            start_date = self.get_starting_time(context) + timedelta(seconds=1)
            if start_date:
                params["since"] = start_date.isoformat() 
        return params
