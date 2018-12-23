"""Project helpers & utilities"""

import re

from bs4 import BeautifulSoup

from settings import SITES


class HabrParser(object):
    """Text parsing & replacements"""

    @staticmethod
    def do_related(text):
        """Replace all links to local address"""

        for label, data in SITES.items():
            path_label = '/{0}'.format(label,) if label else ''
            text = text.replace(
                data['url'].encode('utf-8'), 
                path_label.encode('utf-8')
            )
        return text

    @staticmethod
    def mark_special_words(text):
        """Add &trade; to all 6-char words"""

        #'html.parse' not used because he have bug with html-entities (&plus;)
        soup = BeautifulSoup(text, features="lxml")
        to_replace = soup.find_all(text=re.compile(r'(\s|^)[A-z0-9А-я]{6}(\s|$)'))
        for line in to_replace:
            if line.parent.name not in ('script', 'style'):
                line.string.replace_with(
                    re.sub(
                        r'(^|\s)([a-zA-ZА-я0-9]{6})(\s|$)', 
                        r'\1\2&trade;\3', 
                        line.string
                    )
                )
        output = str(soup)
        output = output.replace('&amp;', '&')
        output = output.encode('utf-8')
        return output

    @classmethod
    def process_html(cls, text):
        """Apply all available methods"""

        text = cls.do_related(text)
        text = cls.mark_special_words(text)
        return text
