crontable = []
outputs = []


def process_message(data):
    if data['channel'].startswith("D"):  # DM channel
        outputs.append([data['channel'], data['text']])
    else:
        outputs.append([data['channel'], '난 DM 에만 메아리친다. :D'])

