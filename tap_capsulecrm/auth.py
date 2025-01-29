"""Capsulecrm Authentication."""

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta
from singer_sdk.streams.rest import _HTTPStream


class CapsulecrmAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for Capsulecrm."""

    def __init__(self, stream: _HTTPStream):
        super().__init__(stream, "https://api.capsulecrm.com/oauth/token")
        self.access_token = self.config.get("access_token")

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the hubspot API."""
        return {
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
            "refresh_token": self.config["refresh_token"],
            "grant_type": "refresh_token",
        }

    def is_token_valid(self):
        # assume access token is valid if set
        return bool(self.access_token)
