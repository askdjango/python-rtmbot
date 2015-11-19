
class BasePlugin(object):
    def __init__(self):
        self.crontable = []
        self.outputs = []

    def do(self, data):
        self.process_always(data)

        if 'type' in data:
            fn_name = 'process_' + data['type']
            if hasattr(self, fn_name):
                getattr(self, fn_name)(data)

    def process_always(self, data):
        pass

    def process_hello(self, data):
        pass

    def process_message(self, data):
        pass

    def process_presence_change(self, data):
        pass

    def process_user_typing(self, data):
        pass

