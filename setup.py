#!/usr/bin/env python3
from setuptools import setup

import os, os.path
import sys

ver = "1.2"

def read(filename):
	return open(os.path.join(os.path.dirname(__file__), filename)).read()


if sys.version_info < (3,0):
	print('Oops, only python >= 3.0 supported!')
	sys.exit()

setup(name = 'pixelterm',
	version = ver,
	description = 'Render pixely images on your terminal. Now also with animated GIF support.',
	license ='Apache 2.0',
	author = 'povilas1565',
	author_email = 'paul156551@gmail.com',
	url = 'https://github.com/povilas1565/PixelTerm',
	packages = ['pixelterm'],
	install_requires=['pillow'],
	py_modules = [ 'commands' ],
	entry_points = {'console_scripts': [
				'pixelterm=commands:pixelterm',
				'unpixelterm=commands:unpixelterm',
				'gifterm=commands:gifterm',
				'colorcube=commands:colorcube',
				'resolvecolor=commands:resolvecolor',
				'pngmeta=commands:pngmeta']},
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Intended Audience :: End Users/Desktop',
		'License :: Freely Distributable',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python :: 3',
		'Topic :: Internet',
		'Topic :: Graphics',
		'Topic :: System :: Networking'
		'Topic :: Text Processing :: Filters',
		'Topic :: Utilities',
	],

	long_description = read('README.md'),
	dependency_links = [],
)
