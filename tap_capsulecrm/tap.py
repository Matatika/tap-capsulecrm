"""Capsulecrm tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_capsulecrm.streams import OpportunitiesStream, PartiesStream, ProjectsStream

STREAM_TYPES = [
    OpportunitiesStream,
    PartiesStream,
    ProjectsStream,
]


class TapCapsulecrm(Tap):
    """Capsulecrm tap class."""

    name = "tap-capsulecrm"

    config_jsonschema = th.PropertiesList(
        th.Property("client_id", th.StringType),
        th.Property("client_secret", th.StringType),
        th.Property("refresh_token", th.StringType),
        th.Property("expires_in", th.IntegerType),
        th.Property("access_token", th.StringType),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapCapsulecrm.cli()
