# Navigator Notifier 

Used to send programmatic notifications to the engineering team.

# Slack

Requires the environment variable `SLACK_WEBHOOK_URL`.

Webhooks target specific channels and so can be configured to run against a test channel.

See [Navigator Notifier slack app](https://api.slack.com/apps/A06EX8DTRSR/incoming-webhooks?) for current webhook endpoints and setup.

```
navigator-notify \
    --target slack \
    --message 'this is a test'
```

Or with docker:

```
make build
```

```
docker run -e SLACK_WEBHOOK_URL=${SLACK_WEBHOOK_URL} navigator-notify \
    --target slack \
    --message 'this is a test'
```
