import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'repoze.zodbconn',
    'repoze.tm2>=1.0b1', # default_commit_veto
    'repoze.retry',
    'repoze.folder',
    'ZODB3',
    'WebError',
    ]

setup(name='spionisto.server',
      version='0.1',
      description='spionisto.server',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Other/Proprietary License",
        ],
      author='Noe Nieto',
      author_email='tzicatl@gmail.com',
      url='http://noenieto.com/spionisto',
      keywords='web pylons pyramid surveillance camera',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require= requires,
      test_suite="spionistoserver",
      entry_points = """\
      [paste.app_factory]
      main = spionistoserver:main
      """,
      paster_plugins=['pyramid'],
      )

