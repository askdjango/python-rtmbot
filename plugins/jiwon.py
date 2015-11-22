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
                    message = '오류) 숫자로 입력해주세요.'
                self.outputs.append([data['channel'], message])


def multiplication(x):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    result = []
    for n in numbers:
        result.append(x * n)
    return result

