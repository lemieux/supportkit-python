
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'SupportKit Python SDK',
    'author': 'Marc-Antoine Lemieux',
    'url': 'https://github.com/lemieux/supportkit-python',
    'download_url': 'https://github.com/lemieux/supportkit-python',
    'author_email': 'marc@marcantoinelemieux.com',
    'version': '0.1',
    'install_requires': [
        'nose',
        'PyJWT',
        'cryptography',
        'requests'
    ],
    'packages': ['supportkit'],
    'scripts': [],
    'name': 'supportkit'
}

setup(**config)
