import requests
from utils import make_request


class TextResource():
    """
    Used to read an online resource or a local text file. For online resource, provide `online_resource=True`.\n
    Example:\n
    ```python
    t = TextResource("https://www.gutenberg.org/files/100/100-0.txt", online_resource=True)
    ```
    """

    def __init__(self, source: str, online_resource=False):
        if online_resource is True:
            self.text = make_request(source)
        else:
            with open(source, "r") as f:
                self.text = f.read()
