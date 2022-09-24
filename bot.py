import slack
import ssl
import certifi
import os
from pathlib import Path

# from dotenv import load_dotenv

from leetcode import previewDateAndLevel, getLink
import schedule
import time

# env_path = Path(".") / ".env"
# load_dotenv(dotenv_path=env_path)

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


def job():
    client.chat_postMessage(
        channel="#leetcode",
        blocks=block,
    )


# Leetcode update daily question at 00:00 UTC
schedule.every().day.at("01:15").do(job)

t = 60 * 60 * 23

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(t)
