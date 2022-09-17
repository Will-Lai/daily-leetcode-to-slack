import slack
import ssl
import certifi
import os
from pathlib import Path
from dotenv import load_dotenv

from leetcode import *

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token=os.environ["SLACK_TOKEN"], ssl=ssl_context)


block = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": previewDateAndLevel() + "\n" + getLink()
            # "<" + getLink() + "|" + previewTitle() + ">",
        },
    }
]

client.chat_postMessage(
    channel="#test-new-channel-1",
    blocks=block,
)
