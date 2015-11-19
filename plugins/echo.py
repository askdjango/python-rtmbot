from .base import BasePlugin


class EchoPlugin(BasePlugin):

    def process_message(self, data):
        if data['channel'].startswith('D'):  # DM channel
            if 'text' in data and data['text'].startswith('echo'):
                self.outputs.append([data['channel'], data['text']])

