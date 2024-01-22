import click

from notify.slack import slack_message


@click.command()
@click.option(
    "--target",
    required=True,
    help="The tool to send a message to",
)
@click.option(
    "--message",
    required=True,
    help="The text of the message to send",
)
def main(target: str, message: str):
    match target:
        case "slack":
            slack_message(message)
        case _:
            raise ValueError(f"Invalid Target: {target}")


if __name__ == "__main__":
    main()
