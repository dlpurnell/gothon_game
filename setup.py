try:
    from setuptools import setuptools
except ImportError:
    from distulis.core import setup
	
config = {
    'description':  'My Project',
	'author': 'Daren Purnell',
	'url': 'where to get it',
	'download_url': Where to download it',
	'author_email': 'dlpurnell@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Name'],
	'scripts': [],
	'name': 'projectname',
}

setup(**config)