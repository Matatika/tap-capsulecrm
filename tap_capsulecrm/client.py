"""REST client handling, including CapsulecrmStream base class."""

from __future__ import annotations

from datetime import timedelta
from functools import cached_property
from typing import Any, Dict, Optional
from urllib.parse import parse_qsl, urlsplit

import requests
from singer_sdk import typing as th
from singer_sdk.streams import RESTStream

from tap_capsulecrm.auth import CapsulecrmAuthenticator


class CapsulecrmStream(RESTStream):
    """Capsulecrm stream class."""

    url_base = "https://api.capsulecrm.com/api/v2"

    records_jsonpath = "$[*]"

    @cached_property
    def authenticator(self) -> CapsulecrmAuthenticator:
        """Return a new authenticator object."""
        return CapsulecrmAuthenticator(self)

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
            next_page_token = response.links.get("next")["url"]
        else:
            next_page_token = None

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        if next_page_token:
            return dict(parse_qsl(urlsplit(next_page_token).query))

        params: dict = {}
        params["perPage"] = 100

        if self.replication_key:
            # from state, or otherwise config
            start_date = self.get_starting_timestamp(context)
            if start_date:
                params["since"] = (start_date + timedelta(seconds=1)).isoformat()

        params["embed"] = ",".join(["tags", "fields"])
        return params

    @cached_property
    def schema(self):
        return th.PropertiesList(*self.get_properties()).to_dict()

    @classmethod
    def get_properties(cls) -> tuple[th.Property]:
        return (
            th.Property(
                "tags",
                th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.NumberType),
                        th.Property("name", th.StringType),
                        th.Property("dataTag", th.BooleanType),
                    ),
                ),
            ),
            th.Property(
                "fields",
                th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.NumberType),
                        th.Property(
                            "definition",
                            th.ObjectType(
                                th.Property("id", th.NumberType),
                                th.Property("name", th.StringType),
                            ),
                        ),
                        th.Property("value", th.AnyType),
                        th.Property("tagId", th.NumberType),
                    ),
                ),
            ),
        )
