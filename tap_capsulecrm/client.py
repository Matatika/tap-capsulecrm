"""REST client handling, including CapsulecrmStream base class."""

import re
from typing import Any, Dict, Optional

import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.streams import RESTStream


class CapsulecrmStream(RESTStream):
    """Capsulecrm stream class."""

    url_base = "https://api.capsulecrm.com/api/v2"

    records_jsonpath = "$[*]"
    next_page_token_jsonpath = "$.next_page"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self, token=self.config.get("auth_token")
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

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        params["perPage"] = 100
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params
