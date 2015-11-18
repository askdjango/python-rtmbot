crontable = []
outputs = []


def process_message(data):
    if data['channel'].startswith('D'):  # DM channel
        if 'text' in data and data['text'].startswith('echo'):
            outputs.append([data['channel'], data['text']])

