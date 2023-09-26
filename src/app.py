import logging
import signal
import chatbot

from slack_bolt import App

logging.basicConfig(level=logging.DEBUG)
app = App()


@app.event("app_mention")
def handle_command_app_mention(event, say):
    say(f"Hey there, <@{event['user']}>! :-)")

@app.command("/jump2")
async def handle_command_jump2(ack, say, command):
    logger.info("Hi there")
    await ack()
    await say(f"Received a command: {command['text']}")


@app.command("/verbose-level")
def handle_command_verbose_level(ack, say, command):
    messageFromHuman = command['text']
    wanted_level = string_to_level_0_9(messageFromHuman)

    logging.info(f"Set verbose level: {wanted_level}")
    ack()
    chatbot.setVerboseLevel(wanted_level)
    say(f"Set verbose level to {wanted_level}")

@app.command("/toxic-level")
def handle_command_toxic_level(ack, say, command):
    messageFromHuman = command['text']
    wanted_level = string_to_level_0_9(messageFromHuman)

    logging.info(f"Set toxic level: {wanted_level}")
    ack()
    chatbot.setToxicLevel(wanted_level)
    say(f"Set toxic level to {wanted_level}")

def string_to_level_0_9(s):
    if not isinstance(s, str):
        return None
    try:
        return max(min(int(s), 0), 9)
    except ValueError:
        return None
    
@app.event("message")
def handle_message(event, say, ack):
    # Ensure your bot has the channels:history (for public channels) 
    # or groups:history (for private channels) 
    # OAuth scope set in the Slack App settings. 
    # You might also need im:history if you want to get messages from direct message channels.
    channel_id = event["channel"]
    ack()
    messages = fetch_channel_messages(channel_id, 1)  # fetch the last 5 messages
    for message in messages:
        messageFromHuman = message['text']
        chatBotPrediction = chatbot.predictResponse(messageFromHuman) 
        say(chatBotPrediction)

def fetch_channel_messages(channel_id, count=100):
    # Use the conversations.history method to fetch messages
    response = app.client.conversations_history(
        channel=channel_id,
        limit=count
    )
    return response["messages"]


from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@flask_app.route("/", methods=["GET"])
def healthcheck():
    return "OK"

@flask_app.route("/pingchatbot/", methods=["GET"])
def ping_chatbot():
    return chatbot.predictResponse("I'm sending a ping message to see if you are ok")


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# Define the signal handler function
def sigint_handler(signal, frame):
    print("\nCtrl-C detected. Exiting gracefully...")
    sys.exit(0)

# Set the signal handler for SIGINT
signal.signal(signal.SIGINT, sigint_handler)