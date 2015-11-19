import re
import requests
from bs4 import BeautifulSoup
from .base import BasePlugin


class MelonPlugin(BasePlugin):
    def process_always(self, data):
        pass

    def process_message(self, data):
        if data['channel'].startswith('D'):  # DM channel
            if 'text' in data:
                matched = re.match(r'멜론top(\d+)', data['text'])
                if matched:
                    max = int(matched.group(1))
                    response = self.parse_chart(max=max)
                    self.outputs.append([data['channel'], response])

    def parse_chart(self, max=None):
        chart_url = 'http://www.melon.com/chart/index.htm'

        html = requests.get(chart_url).text
        soup = BeautifulSoup(html, 'html.parser')

        lines = []
        for tr in soup.select('#frm .d_song_list tr'):
            rank_tags = tr.select('.rank')
            if not tr.select('.rank'):
                continue

            rank = int(rank_tags[0].text)
            info = ' '.join(tag.text for tag in tr.select('.wrap_song_info .ellipsis a')[:2])
            line = '[{}] {}'.format(rank, info)
            lines.append(line)

        if max:
            lines = lines[:max]

        return '\n'.join(lines)

