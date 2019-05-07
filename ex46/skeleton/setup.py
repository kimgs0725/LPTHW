try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = [
    'description': 'a tiny project',
    'author': 'gyeongsoo_kim',
    'url': 'url to get it at.',
    'download_url': 'where to download it.',
    'author_email': 'kimgs0725@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'a little bit game'
]
setup(**config)
