import sys
import time
import logging
import plugins
from slackclient import SlackClient
import settings


def dbg(debug_string):
    if settings.DEBUG:
        logging.info(debug_string)


class RtmBot(object):
    def __init__(self, token):
        self.last_ping = 0
        self.token = token
        self.slack_client = None
        self.plugins = []
        for name in plugins.__all__:
            plugin_cls = getattr(plugins, name)
            self.plugins.append(plugin_cls())

    def connect(self):
        """Convenience method that creates Server instance"""
        self.slack_client = SlackClient(self.token)
        self.slack_client.rtm_connect()

    def start(self):
        self.connect()
        while True:
            for reply in self.slack_client.rtm_read():
                self.input(reply)
            self.output()
            self.auto_ping()
            time.sleep(.1)

    def auto_ping(self):
        # hardcode the interval to 3 seconds
        now = int(time.time())
        if now > self.last_ping + 3:
            self.slack_client.server.ping()
            self.last_ping = now

    def input(self, data):
        print(data)
        for plugin in self.plugins:
            plugin.do(data)

    def output(self):
        for plugin in self.plugins:
            limiter = False
            for (channel_code, message) in plugin.outputs:
                channel = self.slack_client.server.channels.find(channel_code)
                if channel is not None and message is not None:
                    if limiter is True:
                        time.sleep(.1)
                        limiter = False
                    channel.send_message(message)
                    limiter = True
            plugin.outputs = []


if __name__ == '__main__':
    bot = RtmBot(settings.SLACK_TOKEN)

    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        logging.exception('OOPS')

