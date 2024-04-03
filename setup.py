import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' 
PACKAGE_NAME = 'pytest'
AUTHOR = 'Zombiegeek0' 
AUTHOR_EMAIL = '3xpl017.contact@proton.me'
URL = 'https://github.com/ZombieGeek0' 

LICENSE = 'MPL-2.0' 
DESCRIPTION = 'Librería para realizar pruebas de penetración a simples con Python'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = [
      'subprocess',
      'colorama',
      'os',
      'socket',
      'requests',
      'datetime',
      'platform'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
