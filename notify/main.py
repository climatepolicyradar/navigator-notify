import click

from notify.slack import messager


@click.option(
    "--message",
    required=True,
    help="The text to send to slack channel",
)
def main(message: str):
    messager(message)


if __name__ == "__main__":
    main()
