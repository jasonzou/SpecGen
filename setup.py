from setuptools import setup, find_packages

setup(
    name = 'specgen7',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        "Flask",
        "Flask-Script",
        "rdflib",
        "rdfextras",
    ],
    url = 'http://archdesc.info/specgen7/',
    author = 'Jason Zou',
    author_email = 'jason.zou@gmail.com',
    description = 'SpecGen7 is a documentation tool build on the specgen.',
    license = 'AGPL',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
