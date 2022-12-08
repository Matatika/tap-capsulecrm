"""Capsulecrm tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th

from tap_capsulecrm.streams import (
    CapsulecrmStream,
    PartiesStream,
    OpportunitiesStream,
)

STREAM_TYPES = [
    PartiesStream,
    OpportunitiesStream,
]


class TapCapsulecrm(Tap):
    """Capsulecrm tap class."""

    name = "tap-capsulecrm"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.capsulecrm.com/api/v2",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapCapsulecrm.cli()
