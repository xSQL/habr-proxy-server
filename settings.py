"""Settings"""

from collections import OrderedDict

PORT = 8000

SITES_CONFIG = {
    '': {
        'url': 'https://habr.com',
    },
    'mobile': {
        'url': 'https://m.habr.com',
    },
    'cdn': {
        'url': 'https://dr.habracdn.net'
    },
    'storage': {
        'url': 'https://habrastorage.org'
    },
    'storage2': {
        'url': '//habrastorage.org',
        'origin': 'storage'
    }
}

SITES = OrderedDict(sorted(SITES_CONFIG.items(), key=lambda c: c[0]))
