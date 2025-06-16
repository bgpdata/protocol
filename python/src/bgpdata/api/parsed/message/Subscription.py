import json
from datetime import datetime, timezone
from bgpdata.api.parsed.message.Message import Message

class SubscriptionContent:
    """
    Represents the 'content' block of a subscription message.
    """
    def __init__(self, resource, action="subscribe"):
        self.action = action
        self.resource = resource

    @classmethod
    def from_dict(cls, data):
        """Creates a SubscriptionContent object from a dictionary."""
        return cls(resource=data.get("resource"), action=data.get("action"))

    def to_dict(self):
        """Converts the SubscriptionContent object to a dictionary."""
        return {
            "action": self.action,
            "resource": self.resource
        }

    def __repr__(self):
        return f'SubscriptionContent(action={self.action}, resource={self.resource})'


class Subscription(Message):
    """
    Represents a full subscription message, including the standard wrapper.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a Subscription message. Can be used in two ways:
        1. To parse a message: Subscription(raw_message)
        2. To create a message: Subscription(resource="AS12345", action="subscribe")
        """
        if args and isinstance(args[0], str):
            # Case 1: Parse a raw message
            super().__init__(*args, **kwargs)
        else:
            # Case 2: Create a new message from keyword arguments
            content = SubscriptionContent(
                resource=kwargs.pop("resource"),
                action=kwargs.pop("action", "subscribe")
            )
            super().__init__(type="subscription", content=content, **kwargs)

    def _parse_content(self):
        """
        Overrides the base method to parse the content into a
        SubscriptionContent object.
        """
        if self._raw_content:
            return SubscriptionContent.from_dict(self._raw_content)
        return None

    def _content_to_dict(self):
        """
        Overrides the base method to convert the SubscriptionContent
        object to a dictionary for serialization.
        """
        if self.content:
            return self.content.to_dict()
        return None

    def to_json(self):
        """
        Generates the JSON string representation of the message.
        """
        payload = {
            "type": "subscription",
            "content": self._content_to_dict()
        }
        return json.dumps(payload)