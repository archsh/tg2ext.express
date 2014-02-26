# -*- coding: utf-8 -*-
from distutils.core import setup
from tg2ext.express import __version__

setup(name='tg2ext.express',
      version=__version__,
      description='tg2ext.express, a small extension for TurboGears2',
      long_description=open("README.md").read(),
      author='Mingcai SHEN',
      author_email='archsh@gmail.com',
      packages=['tg2ext'],
      package_dir={'tg2ext': 'tg2ext'},
      package_data={'tg2ext': ['stuff']},
      license="The MIT License (MIT)",
      platforms=["any"],
      install_requires=[
          'TurboGears2>=2.3.1',
          'SQLAlchemy>=0.8.2',
      ],
      url='https://github.com/archsh/tg2ext.express')
