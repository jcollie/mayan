# -*- encoding:utf8 -*-
import os
from email.utils import parseaddr
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

author, author_email = parseaddr("Roberto Rosario <roberto.rosario.gonzalez@gmail.com>")
version = "0.13"
url = "http://www.mayan-edms.com/"

setup(name='mayan',
    url=url,
    version=version,
    description=README.split('\n\n')[0],
    long_description=README,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Communications :: File Sharing",

    ],
    author=author,
    author_email=author_email,
    packages=find_packages(),
    namespace_packages=['mayan'],
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    zip_safe=False,
)
