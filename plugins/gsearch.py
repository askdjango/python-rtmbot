import re
import requests
from .base import BasePlugin


TAG_PATTERN = re.compile(r'<[^>]+>')


class GoogleSearchPlugin(BasePlugin):
    def process_message(self, data):
        if ('text' in data) and ('subtype' not in data):
            matched = re.match(r'gsearch\?\s*(.*)', data['text'])
            if matched:
                q = matched.group(1)
                self.outputs.append([data['channel'], self.gsearch(q)])

    def gsearch(self, q, max_count=5, start=0):
        params = {
            'q': q,
            'v': '1.0',
            'start': start,
            'rsz': max_count,
        }

        url = 'http://ajax.googleapis.com/ajax/services/search/web'
        response = requests.get(url, params=params).json()

        lines = []
        for idx, result in enumerate(response['responseData']['results']):
            desc = re.sub(TAG_PATTERN, '', result['content'])
            desc = ' '.join(desc.splitlines())
            lines.append('{idx}) {titleNoFormatting}\n{desc}\n{url}'.format(idx=idx+1, desc=desc, **result))
        return '\n\n'.join(lines)
