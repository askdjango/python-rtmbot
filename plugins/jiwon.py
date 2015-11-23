import re
from .base import BasePlugin


class JiwonPlugin(BasePlugin):
    PATTERN = re.compile(r'jiwon\?\s*(.*)')

    def process_message(self, data):
        if ('text' in data) and ('subtype' not in data):
            matched = re.match(self.PATTERN, data['text'])
            if matched:
                try:
                    message = ' '.join(map(str, multiplication(int(matched.group(1)))))
                except ValueError:
                    message = '오류) 1 이상 19 이하의 숫자로 입력해주세요.'
                self.outputs.append([data['channel'], message])


def multiplication(x):
    if 1 <= x <= 19:
        result = []
        for n in range(1, 20):
            result.append(x * n)
        return result
    else:
        raise ValueError

