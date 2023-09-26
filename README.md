# A simple Slack bot

A simple Slack bot build on Bolt framework (https://slack.dev/bolt-python) and packaged in a Docker image.

## Prerequisites

1. Docker (Desktop) installed. 
2. Slack account - get free or paind from slack.com
3. An SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET - follow the instructions here https://api.slack.com/start/building/bolt-python . For this project you only have  to create and configure the Slack app, the python envirnoment is set up in the Dockerfile.

## Configure

Create `config.file` in project root with your API key:

```
SLACK_BOT_TOKEN={MY_SECRET_TOKEN_THAT_I_NEVER_EXPOSE}
SLACK_SIGNING_SECRET={MY_SECRET_TOKEN_THAT_I_NEVER_EXPOSE}
OPENAI_API_KEY={MY_SECRET_TOKEN_THAT_I_NEVER_EXPOSE}
```

## Start

    cd <project-root>
    docker-compose up
    
    Add --build if you want to build the image
    Add --detach if you want to run in detached mode, that is container runs in the background

## Use

Find you public IP and make sure port 3000 is accessible through the firewall
I Slack App:
* Open Event Substriptions page
Add the url to the Event Substriptions of you Slack app

<http://your-public-IP:3000/slack/events>

Add substription to these events

* Open Slash Commands page
Add the comman 'jump' with the same request url as above

## References

- Slack Bolt: https://api.slack.com/start/building/bolt-python
