import json
from datetime import datetime, timezone

class Message:
    """
    Base class for a message bus protocol object.
    Handles serialization and deserialization of the standard message wrapper.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a Message object. Can be used in two ways:
        1. To parse a message: Message(raw_json_string)
        2. To create a message: Message(type="...", content=...)
        """
        if args and isinstance(args[0], str):
            # Case 1: Parse a raw JSON string
            data = json.loads(args[0])
            self.type = data.get("type")
            self.timestamp = data.get("timestamp")
            self._raw_content = data.get("content")
            self.content = self._parse_content()

        else:
            # Case 2: Create a new message from keyword arguments
            self.type = kwargs.get("type")
            self.timestamp = kwargs.get("timestamp", datetime.now(timezone.utc).isoformat())
            self.content = kwargs.get("content")
            self._raw_content = None

    def _parse_content(self):
        """
        Parses the raw content dictionary into a specific content object.
        Subclasses should override this method.
        """
        return self._raw_content # Base implementation returns the dict

    def _content_to_dict(self):
        """
        Converts the content object to a dictionary for serialization.
        Subclasses should override this if content is an object.
        """
        return self.content # Assumes content is already a dict

    def to_json(self):
        """
        Generates the JSON string representation of the message.
        """
        payload = {
            "type": self.type,
            "content": self._content_to_dict()
        }
        return json.dumps(payload)

    def __repr__(self):
        return f'{self.__class__.__name__}(type={self.type})'