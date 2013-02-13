from distutils.core import setup

setup(
    name='Gitetoscopio',
    version='1.0.0',
    author='Pablo Figue',
    author_email='pablo dot gfigue gmail com',
    packages=['gitetoscopio', 'gitetoscopio.test'],
    scripts=['bin/github-status.py', ],
    url='http://pypi.python.org/pypi/Gitetoscopio/',
    license='LICENSE.txt',
    description='A Python module to query status.github.com\'s API ',
    long_description=open('README.txt').read(),
    install_requires=[
        "iso8601 == 0.1.4",
    ],
)
