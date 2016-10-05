from setuptools import setup, find_packages

setup(
    name = 'dimsummary',
    version = '1.0.0',
    packages = find_packages(),
    install_requires = [
        "octopus==1.0.0",
        "esprit",
        "Flask"
    ],
    url = 'http://dimsummary.com/',
    author = 'Dim Summary',
    author_email = 'dimsummary@oneoverzero.com',
    description = 'Dim Summary Ratings App',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyheart',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
