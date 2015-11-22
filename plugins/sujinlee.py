import time
import re
from .base import BasePlugin


class SujinleePlugin(BasePlugin):
    PATTERN = re.compile(r'today\?(.*)')

    def process_message(self, data):
        if ('text' in data) and ('subtype' not in data):
            matched = re.match(self.PATTERN, data['text'])
            if matched:
                self.outputs.append([data['channel'], today()])


def today():
    weekday_ko = {
        'Monday': '월',
        'Tuesday': '화',
        'Wednesday': '수',
        'Thursday': '목',
        'Friday': '금',
        'Saturday': '토',
        'Sunday': '일',
    }

    weekday_today_ko = weekday_ko[time.strftime('%A')]
    message = time.strftime('오늘은 %Y년 %-m월 %d일') + ' %s요일 입니다.' % (weekday_today_ko)

    return message

