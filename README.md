python-rtmbot
=============
A Slack bot written in python that connects via the RTM API.

Python-rtmbot is a callback based bot engine. The plugins architecture should be familiar to anyone with knowledge to the [Slack API](https://api.slack.com) and Python. The configuration file format is YAML.

Some differences to webhooks:

1. Doesn't require a webserver to receive messages
2. Can respond to direct messages from users
3. Logs in as a slack user (or bot)
4. Bot users must be invited to a channel

Dependencies
----------
* websocket-client https://pypi.python.org/pypi/websocket-client/
* python-slackclient https://github.com/slackhq/python-slackclient

Installation
-----------

1. Download the python-rtmbot code

        git clone https://github.com/askdjango/python-rtmbot.git
        cd python-rtmbot

2. Install dependencies ([virtualenv](http://virtualenv.readthedocs.org/en/latest/) is recommended.)

        pip install -r requirements.txt

3. Configure rtmbot (https://api.slack.com/bot-users)

        cp settings_sample.py settings.py
        vi settings.py
          SLACK_TOKEN = "xoxb-11111111111-222222222222222"

