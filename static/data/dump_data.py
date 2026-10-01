import json
import qrcode
from urllib.parse import quote

DATA_FOLDER = "./static/data"
CHANNEL_DETAILS_FILE = "channels.json"
CHANNELS_QR_CODE_FOLDER = "./static/data/channels"


class Channel:
    name: str
    order: int
    description: str
    key: str
    url: str

    def __init__(self, data: dict):
        self.name = data["name"]
        self.description = data["description"]
        self.order = data["order"]
        self.key = data.get("key")
        self.calculate_details()

    def calculate_details(self):
        if not self.key:
            raise ValueError(f"Channel {self.name} is missing its documented key")
        self.url = f"meshcore://channel/add?name={quote(self.name, safe='')}&secret={self.key}"

    @property
    def as_json(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "order": self.order,
            "key": self.key,
            "url": self.url,
        }


def write_to_file(data: list[dict], filename):
    with open(f"{DATA_FOLDER}/{filename}", "w") as f:
        json.dump(data, f, indent=4)

def read_from_file(filename: str):
    with open(f"{DATA_FOLDER}/{filename}", "r") as f:
        return json.load(f)


def generate_channel_qr_code_image(channel: Channel):
    name = channel.name
    clean_name = name.replace("#", "")
    order = channel.order

    qr_code_image = qrcode.make(data=channel.url)
    qr_code_image.save(f"{CHANNELS_QR_CODE_FOLDER}/meshcore_channel_{order}_{clean_name}.png")


channels_data = read_from_file(filename=CHANNEL_DETAILS_FILE)
channels = [Channel(data=data) for data in channels_data]
for _channel in channels:
    generate_channel_qr_code_image(channel=_channel)
write_to_file(data=[_channel.as_json for _channel in channels], filename="channels.json")

