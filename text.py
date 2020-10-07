import requests


def make_request(url) -> (int, str):
    response = requests.get(url, headers={"User-Agent": ""})
    return response.status_code, response.text


class TextResource():
    """
    Used to read an online resource or a local text file. For online resource, provide `online_resource=True`.\n
    Example:\n
    ```python
    t = TextResource("https://www.gutenberg.org/files/100/100-0.txt", online_resource=True)
    ```
    """

    def __init__(self, source, online_resource=False):
        if online_resource is True:
            self.status_code, self.text = make_request(source)
        else:
            self.status_code = None
            with open(source, "r") as f:
                self.text = f.read()
