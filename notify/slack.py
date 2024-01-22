import os

from slack_sdk.webhook import WebhookClient


def messager(message: str) -> None:
    ENDPOINT = os.getenv("SLACK_WEBHOOK_URL")
    client = WebhookClient(
        url=ENDPOINT,
        timeout=30,
        user_agent_prefix="Navigator Notify",
    )

    client.send(text=message)
