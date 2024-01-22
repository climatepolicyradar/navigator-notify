import logging
import os

from slack_sdk.webhook import WebhookClient

logging.basicConfig(
    level="INFO",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(__file__)


def slack_message(message: str) -> None:
    ENDPOINT = os.environ["SLACK_WEBHOOK_URL"]

    client = WebhookClient(
        url=ENDPOINT,
        user_agent_prefix="Navigator Notify",
    )

    response = client.send(text=message)
    logger.info(f"{response.status_code} status code for sent message: '{message}'")
